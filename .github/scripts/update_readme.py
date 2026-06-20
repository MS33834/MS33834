import json
import os
import re
import urllib.error
import urllib.request
from datetime import datetime

README_PATH = "README.md"
GITHUB_USER = "MS33834"
CSDN_USER = "weixin_56622231"

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def fetch(url, headers=None):
    """Fetch URL and return decoded text."""
    merged = {**DEFAULT_HEADERS, **(headers or {})}
    token = os.environ.get("GITHUB_TOKEN")
    if token and "github.com" in url:
        merged["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=merged)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def parse_xml_items(xml_text):
    """Parse CSDN RSS XML without external dependencies."""
    items = []
    raw_items = xml_text.split("<item>")[1:]
    for raw in raw_items:
        if "</item>" not in raw:
            continue
        body = raw.split("</item>")[0]

        def get_tag(tag):
            start = body.find(f"<{tag}>")
            end = body.find(f"</{tag}>")
            if start == -1 or end == -1:
                return ""
            return body[start + len(tag) + 2 : end].strip()

        title = get_tag("title").replace("<![CDATA[", "").replace("]]>", "")
        link = get_tag("link").replace("<![CDATA[", "").replace("]]>", "")
        pub_date = get_tag("pubDate").replace("<![CDATA[", "").replace("]]>", "")
        items.append({"title": title, "link": link, "date": pub_date})
    return items


def get_csdn_posts(limit=5):
    """Fetch latest CSDN posts."""
    url = f"https://blog.csdn.net/{CSDN_USER}/rss/list?spm=1001.2014.3001.5112"
    try:
        xml_text = fetch(url)
        posts = parse_xml_items(xml_text)
        return posts[:limit]
    except Exception as e:
        print(f"CSDN fetch failed: {e}")
        return []


def format_csdn_posts(posts):
    """Format CSDN posts to a clean markdown list."""
    if not posts:
        return "_Unable to fetch the latest articles right now. Please check back later._"
    lines = []
    for idx, p in enumerate(posts, 1):
        date_str = ""
        if p["date"]:
            try:
                dt = datetime.strptime(p["date"], "%a, %d %b %Y %H:%M:%S %z")
                date_str = dt.strftime("%Y-%m-%d")
            except Exception:
                date_str = p["date"][:16]
        lines.append(f"{idx}. [{p['title']}]({p['link']}) · `{date_str}`")
    return "\n".join(lines)


def get_english_quote():
    """Fetch a daily English quote from ZenQuotes (open-source API)."""
    try:
        text = fetch("https://zenquotes.io/api/today")
        quotes = json.loads(text)
        if not quotes:
            raise ValueError("empty quotes")
        q = quotes[0]
        return q.get("q", "").strip(), q.get("a", "Unknown").strip()
    except Exception as e:
        print(f"English quote fetch failed: {e}")
        return "Keep shining, even when no one is watching.", "Morning Star"


def get_chinese_quote():
    """Fetch a daily Chinese quote from hitokoto."""
    try:
        text = fetch("https://v1.hitokoto.cn/?c=d&c=i&encode=json")
        data = json.loads(text)
        hitokoto = data.get("hitokoto", "").strip()
        source = data.get("from", "").strip()
        if not hitokoto:
            raise ValueError("empty hitokoto")
        return hitokoto, source
    except Exception as e:
        print(f"Chinese quote fetch failed: {e}")
        return "在黎明之前，保持发光。", "启明星"


def format_quote(en_text, en_author, zh_text, zh_source):
    """Format daily quote section with collapsible Chinese translation."""
    source_display = f"《{zh_source}》" if zh_source else ""
    return (
        f"> **{en_text}**  \n"
        f"> — {en_author}\n\n"
        f"<details>\n"
        f"<summary>🌙 中文</summary>\n\n"
        f"> {zh_text}  \n"
        f"> — {source_display}\n\n"
        f"</details>"
    )


def get_tech_stack():
    """Detect tech stack from user's public repos."""
    url = f"https://api.github.com/users/{GITHUB_USER}/repos?per_page=100"
    try:
        text = fetch(url, headers={"User-Agent": f"{GITHUB_USER}-readme-bot"})
        repos = json.loads(text)
        if not repos:
            return "_No public repository data available._"
        lang_counts = {}
        for r in repos:
            lang = r.get("language")
            if lang:
                lang_counts[lang] = lang_counts.get(lang, 0) + 1
        sorted_langs = sorted(lang_counts.items(), key=lambda x: x[1], reverse=True)[:8]
        icon_map = {
            "Python": "py", "JavaScript": "js", "TypeScript": "ts",
            "Rust": "rust", "Go": "go", "Java": "java", "C++": "cpp",
            "C": "c", "HTML": "html", "CSS": "css", "Shell": "bash",
            "Vue": "vue", "React": "react", "Swift": "swift", "Kotlin": "kotlin",
            "Ruby": "ruby", "PHP": "php", "Scala": "scala", "Dart": "dart"
        }
        icons = []
        for lang, _ in sorted_langs:
            icon = icon_map.get(lang, lang.lower().replace("+", "plusplus").replace("#", "sharp").replace(" ", ""))
            icons.append(icon)
        icons_str = ",".join(icons)
        return (
            '<div align="center">\n\n'
            f'<img src="https://skillicons.dev/icons?i={icons_str}&theme=dark&perline=8" '
            f'alt="tech stack" style="max-width: 720px;"/>\n\n'
            '</div>'
        )
    except Exception as e:
        print(f"Tech stack fetch failed: {e}")
        return "_Unable to fetch the tech stack right now._"


def get_top_repos(limit=4):
    """Fetch user's most starred repos, excluding the profile repo itself."""
    fetch_count = max(limit * 2, 10)
    url = f"https://api.github.com/users/{GITHUB_USER}/repos?sort=stargazers_count&order=desc&per_page={fetch_count}"
    try:
        text = fetch(url, headers={"User-Agent": f"{GITHUB_USER}-readme-bot"})
        repos = json.loads(text)
        filtered = [r for r in repos if r["name"].lower() != GITHUB_USER.lower() and not r.get("fork")]
        filtered = filtered[:limit]
        if not filtered:
            return "_No public repositories found._"
        cards = []
        for r in filtered:
            name = r["name"]
            url_repo = r["html_url"]
            cards.append(
                f'<a href="{url_repo}" target="_blank">'
                f'<img src="https://github-readme-stats.vercel.app/api/pin/?username={GITHUB_USER}&repo={name}'
                '&theme=tokyonight&bg_color=050817&title_color=ffe9a8&text_color=c9d6f2'
                f'&icon_color=4a6fa5&border_color=25335e" alt="{name}"/>'
                '</a>'
            )
        grid = [
            "<div align=\"center\">",
            "<table>",
            "  <tr>",
            f"    <td>{cards[0]}</td>",
            f"    <td>{cards[1] if len(cards) > 1 else ''}</td>",
            "  </tr>",
            "  <tr>",
            f"    <td>{cards[2] if len(cards) > 2 else ''}</td>",
            f"    <td>{cards[3] if len(cards) > 3 else ''}</td>",
            "  </tr>",
            "</table>",
            "</div>",
        ]
        return "\n".join(grid)
    except Exception as e:
        print(f"Top repos fetch failed: {e}")
        return "_Unable to fetch repository data right now._"


def get_trending_repos(limit=4):
    """Fetch popular repos as a proxy for trending."""
    url = f"https://api.github.com/search/repositories?q=stars:>5000&sort=stars&order=desc&per_page={limit}"
    try:
        text = fetch(url, headers={"User-Agent": f"{GITHUB_USER}-readme-bot"})
        data = json.loads(text)
        items = data.get("items", [])
        if not items:
            return "_Unable to fetch trending repositories right now._"
        rows = []
        for r in items:
            name = r["full_name"]
            desc = r.get("description") or "No description"
            stars = r["stargazers_count"]
            url_repo = r["html_url"]
            short_desc = desc[:55] + "..." if len(desc) > 55 else desc
            rows.append(f"| [{name}]({url_repo}) | {short_desc} | ⭐ {stars:,} |")
        header = "| Repository | Description | Stars |\n|------------|-------------|-------|"
        return header + "\n" + "\n".join(rows)
    except Exception as e:
        print(f"Trending fetch failed: {e}")
        return "_Unable to fetch trending repositories right now._"


def update_section(content, marker_start, marker_end, new_content):
    """Replace content between markers."""
    pattern = re.compile(
        f"({re.escape(marker_start)}).*?({re.escape(marker_end)})",
        re.DOTALL,
    )
    if not pattern.search(content):
        print(f"Marker {marker_start} not found, skipping.")
        return content
    return pattern.sub(f"\\1\n{new_content}\n\\2", content)


def main():
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    posts = get_csdn_posts()
    content = update_section(
        content,
        "<!-- CSDN-POSTS-START -->",
        "<!-- CSDN-POSTS-END -->",
        format_csdn_posts(posts),
    )

    en_text, en_author = get_english_quote()
    zh_text, zh_source = get_chinese_quote()
    content = update_section(
        content,
        "<!-- DAILY-QUOTE-START -->",
        "<!-- DAILY-QUOTE-END -->",
        format_quote(en_text, en_author, zh_text, zh_source),
    )

    tech = get_tech_stack()
    content = update_section(
        content,
        "<!-- TECH-STACK-START -->",
        "<!-- TECH-STACK-END -->",
        tech,
    )

    top = get_top_repos()
    content = update_section(
        content,
        "<!-- TOP-REPOS-START -->",
        "<!-- TOP-REPOS-END -->",
        top,
    )

    trending = get_trending_repos()
    content = update_section(
        content,
        "<!-- TRENDING-REPOS-START -->",
        "<!-- TRENDING-REPOS-END -->",
        trending,
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("README.md updated successfully.")


if __name__ == "__main__":
    main()

import json
import os
import re
import ssl
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

README_FILES = [("README.md", "en"), ("README.zh.md", "zh")]
GITHUB_USER = "MS33834"
CSDN_USER = "weixin_56622231"

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def fetch(url, headers=None, retries=3):
    """Fetch URL and return decoded text, with retry for transient errors."""
    merged = {**DEFAULT_HEADERS, **(headers or {})}
    token = os.environ.get("GITHUB_TOKEN")
    if token and "github.com" in url:
        merged["Authorization"] = f"Bearer {token}"

    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=merged)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code >= 500 and attempt < retries - 1:
                print(f"Fetch {url} got HTTP {e.code}, retrying ({attempt + 1}/{retries})...")
                time.sleep(2 ** attempt)
                continue
            raise
        except (urllib.error.URLError, TimeoutError, ssl.SSLError) as e:
            last_err = e
            if attempt < retries - 1:
                print(f"Fetch {url} failed ({type(e).__name__}), retrying ({attempt + 1}/{retries})...")
                time.sleep(2 ** attempt)
                continue
            raise
    raise last_err


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


def format_quote(en_text, en_author, zh_text, zh_source, lang="zh"):
    """Format daily quote section."""
    if lang == "en":
        return f"> **{en_text}**  \n> — {en_author}"
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


def fetch_starred_repos(limit=6):
    """Fetch user's most starred non-fork repos, excluding the profile repo itself."""
    fetch_count = max(limit * 2, 10)
    url = f"https://api.github.com/users/{GITHUB_USER}/repos?sort=stargazers_count&order=desc&per_page={fetch_count}"
    try:
        text = fetch(url, headers={"User-Agent": f"{GITHUB_USER}-readme-bot"})
        repos = json.loads(text)
        filtered = [r for r in repos if r["name"].lower() != GITHUB_USER.lower() and not r.get("fork")]
        return filtered[:limit]
    except Exception as e:
        print(f"Starred repos fetch failed: {e}")
        return []


def format_top_repos(repos):
    """Generate pinned repo cards from repo list."""
    if not repos:
        return "_No public repositories found._"
    lines = ['<div align="center">']
    for r in repos:
        name = r["name"]
        url_repo = r["html_url"]
        lines.append(
            f'<a href="{url_repo}" target="_blank">'
            f'<img src="https://github-readme-stats.vercel.app/api/pin/?username={GITHUB_USER}&repo={name}'
            '&theme=tokyonight&bg_color=050817&title_color=ffe9a8&text_color=c9d6f2'
            f'&icon_color=4a6fa5&border_color=25335e" width="400" alt="{name}"/>'
            '</a><br>'
        )
    lines.append('</div>')
    return "\n".join(lines)


def format_featured_repos(repos):
    """Generate a markdown list of featured repos with descriptions and badges."""
    if not repos:
        return "_No public repositories found._"
    lines = []
    for r in repos:
        name = r["name"]
        url_repo = r["html_url"]
        desc = (r.get("description") or "Original project by MS33834.").strip()
        lines.append(f"### [{name}]({url_repo})")
        lines.append("")
        lines.append(f"{desc}")
        lines.append("")
        lines.append(
            f"[![stars](https://img.shields.io/github/stars/{GITHUB_USER}/{name}?style=flat-square&color=ffe9a8&labelColor=050817&logo=github)]({url_repo}) "
            f"[![lang](https://img.shields.io/github/languages/top/{GITHUB_USER}/{name}?style=flat-square&color=4a6fa5&labelColor=050817)]({url_repo}) "
            f"[![commit](https://img.shields.io/github/last-commit/{GITHUB_USER}/{name}?style=flat-square&color=c9d6f2&labelColor=050817)]({url_repo}/commits/main)"
        )
        lines.append("")
    return "\n".join(lines)


def get_user_stats():
    """Fetch public repo count and followers for the user."""
    url = f"https://api.github.com/users/{GITHUB_USER}"
    try:
        text = fetch(url, headers={"User-Agent": f"{GITHUB_USER}-readme-bot"})
        data = json.loads(text)
        return data.get("public_repos", 0), data.get("followers", 0)
    except Exception as e:
        print(f"User stats fetch failed: {e}")
        return 0, 0


def get_total_stars():
    """Sum stars across all public non-fork repos."""
    url = f"https://api.github.com/users/{GITHUB_USER}/repos?per_page=100"
    try:
        text = fetch(url, headers={"User-Agent": f"{GITHUB_USER}-readme-bot"})
        repos = json.loads(text)
        return sum(r.get("stargazers_count", 0) for r in repos if not r.get("fork"))
    except Exception as e:
        print(f"Total stars fetch failed: {e}")
        return 0


def format_profile_badges(public_repos, total_stars, followers):
    """Generate dynamic profile summary badges using shields.io."""
    return (
        f'<img src="https://img.shields.io/badge/Public%20Repos-{public_repos}-4a6fa5'
        '?style=flat-square&labelColor=050817" alt="public repos"/> '
        f'<img src="https://img.shields.io/badge/Total%20Stars-{total_stars}-ffe9a8'
        '?style=flat-square&labelColor=050817" alt="total stars"/> '
        f'<img src="https://img.shields.io/badge/Followers-{followers}-c9d6f2'
        '?style=flat-square&labelColor=050817" alt="followers"/>'
    )


def format_last_updated(lang="zh"):
    """Generate a last-updated timestamp line."""
    label = "最后更新 / Last updated" if lang == "zh" else "Last updated"
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return f"_{label}: {now}_"


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
    posts = get_csdn_posts()
    en_text, en_author = get_english_quote()
    zh_text, zh_source = get_chinese_quote()
    tech = get_tech_stack()
    starred = fetch_starred_repos()
    top_repos = format_top_repos(starred)
    featured_repos = format_featured_repos(starred)
    public_repos, followers = get_user_stats()
    total_stars = get_total_stars()

    for filename, lang in README_FILES:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            print(f"{filename} not found, skipping.")
            continue

        content = update_section(
            content,
            "<!-- CSDN-POSTS-START -->",
            "<!-- CSDN-POSTS-END -->",
            format_csdn_posts(posts),
        )

        content = update_section(
            content,
            "<!-- DAILY-QUOTE-START -->",
            "<!-- DAILY-QUOTE-END -->",
            format_quote(en_text, en_author, zh_text, zh_source, lang),
        )

        content = update_section(
            content,
            "<!-- TECH-STACK-START -->",
            "<!-- TECH-STACK-END -->",
            tech,
        )

        content = update_section(
            content,
            "<!-- FEATURED-PROJECTS-START -->",
            "<!-- FEATURED-PROJECTS-END -->",
            featured_repos,
        )

        content = update_section(
            content,
            "<!-- TOP-REPOS-START -->",
            "<!-- TOP-REPOS-END -->",
            top_repos,
        )

        content = update_section(
            content,
            "<!-- PROFILE-BADGES-START -->",
            "<!-- PROFILE-BADGES-END -->",
            format_profile_badges(public_repos, total_stars, followers),
        )

        content = update_section(
            content,
            "<!-- LAST-UPDATED-START -->",
            "<!-- LAST-UPDATED-END -->",
            format_last_updated(lang),
        )

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

    print("README files updated successfully.")


if __name__ == "__main__":
    main()

<div align="center">

<!-- HERO-SVG-START -->
<svg viewBox="0 0 820 360" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width: 860px;">
  <defs>
    <linearGradient id="sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#030511"/>
      <stop offset="35%" stop-color="#0a1230"/>
      <stop offset="70%" stop-color="#152255"/>
      <stop offset="100%" stop-color="#263970"/>
    </linearGradient>
    <radialGradient id="morningGlow" cx="78%" cy="22%" r="55%">
      <stop offset="0%" stop-color="#ffe9a8" stop-opacity="0.45"/>
      <stop offset="35%" stop-color="#7b9bcf" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#030511" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="nebula1" cx="20%" cy="80%" r="45%">
      <stop offset="0%" stop-color="#6b4c9a" stop-opacity="0.25"/>
      <stop offset="60%" stop-color="#4a6fa5" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#030511" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="nebula2" cx="85%" cy="75%" r="40%">
      <stop offset="0%" stop-color="#a88fbb" stop-opacity="0.18"/>
      <stop offset="70%" stop-color="#4a6fa5" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#030511" stop-opacity="0"/>
    </radialGradient>
    <filter id="starGlow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="1.6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="bigStarGlow" x="-120%" y="-120%" width="340%" height="340%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="moonGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect width="820" height="360" rx="16" fill="url(#sky)"/>
  <rect width="820" height="360" rx="16" fill="url(#morningGlow)"/>
  <rect width="820" height="360" rx="16" fill="url(#nebula1)"/>
  <rect width="820" height="360" rx="16" fill="url(#nebula2)"/>

  <!-- star field -->
  <g fill="#ffffff">
    <circle cx="45" cy="40" r="1.1" opacity="0.5"><animate attributeName="opacity" values="0.2;1;0.2" dur="2.8s" repeatCount="indefinite"/></circle>
    <circle cx="110" cy="80" r="0.9" opacity="0.5"><animate attributeName="opacity" values="0.3;0.9;0.3" dur="3.6s" repeatCount="indefinite" begin="0.4s"/></circle>
    <circle cx="185" cy="35" r="1.3" opacity="0.6"><animate attributeName="opacity" values="0.2;1;0.2" dur="2.4s" repeatCount="indefinite" begin="1.1s"/></circle>
    <circle cx="260" cy="115" r="1" opacity="0.5"><animate attributeName="opacity" values="0.3;0.85;0.3" dur="4s" repeatCount="indefinite" begin="0.2s"/></circle>
    <circle cx="345" cy="55" r="1.2" opacity="0.6"><animate attributeName="opacity" values="0.2;1;0.2" dur="3.2s" repeatCount="indefinite" begin="0.7s"/></circle>
    <circle cx="420" cy="95" r="0.9" opacity="0.5"><animate attributeName="opacity" values="0.3;0.9;0.3" dur="2.9s" repeatCount="indefinite" begin="1.5s"/></circle>
    <circle cx="505" cy="40" r="1.4" opacity="0.6"><animate attributeName="opacity" values="0.2;1;0.2" dur="3.8s" repeatCount="indefinite" begin="0.1s"/></circle>
    <circle cx="590" cy="125" r="1" opacity="0.5"><animate attributeName="opacity" values="0.3;0.85;0.3" dur="2.6s" repeatCount="indefinite" begin="0.9s"/></circle>
    <circle cx="675" cy="55" r="1.1" opacity="0.6"><animate attributeName="opacity" values="0.2;1;0.2" dur="3.4s" repeatCount="indefinite" begin="1.3s"/></circle>
    <circle cx="760" cy="100" r="0.9" opacity="0.5"><animate attributeName="opacity" values="0.3;0.9;0.3" dur="4.2s" repeatCount="indefinite" begin="0.5s"/></circle>
    <circle cx="75" cy="170" r="1" opacity="0.5"><animate attributeName="opacity" values="0.2;0.85;0.2" dur="3s" repeatCount="indefinite" begin="1.7s"/></circle>
    <circle cx="155" cy="210" r="1.2" opacity="0.6"><animate attributeName="opacity" values="0.3;1;0.3" dur="2.7s" repeatCount="indefinite" begin="0.3s"/></circle>
    <circle cx="250" cy="250" r="0.9" opacity="0.5"><animate attributeName="opacity" values="0.2;0.8;0.2" dur="3.5s" repeatCount="indefinite" begin="1s"/></circle>
    <circle cx="355" cy="285" r="1" opacity="0.5"><animate attributeName="opacity" values="0.3;0.9;0.3" dur="2.5s" repeatCount="indefinite" begin="0.6s"/></circle>
    <circle cx="470" cy="250" r="1.1" opacity="0.6"><animate attributeName="opacity" values="0.2;1;0.2" dur="3.7s" repeatCount="indefinite" begin="1.4s"/></circle>
    <circle cx="585" cy="285" r="0.9" opacity="0.5"><animate attributeName="opacity" values="0.3;0.85;0.3" dur="2.8s" repeatCount="indefinite" begin="0.2s"/></circle>
    <circle cx="700" cy="245" r="1.2" opacity="0.6"><animate attributeName="opacity" values="0.2;1;0.2" dur="4s" repeatCount="indefinite" begin="1.2s"/></circle>
    <circle cx="785" cy="285" r="0.9" opacity="0.5"><animate attributeName="opacity" values="0.3;0.9;0.3" dur="3.1s" repeatCount="indefinite" begin="0.8s"/></circle>
  </g>

  <!-- constellation lines -->
  <g stroke="#7b9bcf" stroke-width="0.6" opacity="0.3">
    <line x1="110" y1="80" x2="185" y2="35"/>
    <line x1="185" y1="35" x2="260" y2="115"/>
    <line x1="260" y1="115" x2="345" y2="55"/>
    <line x1="345" y1="55" x2="420" y2="95"/>
    <line x1="505" y1="40" x2="590" y2="125"/>
    <line x1="590" y1="125" x2="675" y2="55"/>
    <line x1="675" y1="55" x2="760" y2="100"/>
  </g>

  <!-- crescent moon -->
  <g transform="translate(120, 75)" filter="url(#moonGlow)">
    <path d="M0,-22 A22,22 0 1,1 0,22 A16,16 0 1,0 0,-22 Z" fill="#fff8dc" opacity="0.85"/>
  </g>

  <!-- shooting star 1 -->
  <g opacity="0">
    <line x1="780" y1="35" x2="680" y2="95" stroke="#ffe9a8" stroke-width="1.6" stroke-linecap="round">
      <animate attributeName="opacity" values="0;1;0" dur="2.2s" repeatCount="indefinite" begin="1.5s"/>
      <animate attributeName="x1" values="780;620" dur="2.2s" repeatCount="indefinite" begin="1.5s"/>
      <animate attributeName="y1" values="35;125" dur="2.2s" repeatCount="indefinite" begin="1.5s"/>
      <animate attributeName="x2" values="680;520" dur="2.2s" repeatCount="indefinite" begin="1.5s"/>
      <animate attributeName="y2" values="95;185" dur="2.2s" repeatCount="indefinite" begin="1.5s"/>
    </line>
  </g>

  <!-- shooting star 2 -->
  <g opacity="0">
    <line x1="550" y1="30" x2="480" y2="80" stroke="#fff8dc" stroke-width="1.2" stroke-linecap="round">
      <animate attributeName="opacity" values="0;0.8;0" dur="2s" repeatCount="indefinite" begin="5s"/>
      <animate attributeName="x1" values="550;430" dur="2s" repeatCount="indefinite" begin="5s"/>
      <animate attributeName="y1" values="30;110" dur="2s" repeatCount="indefinite" begin="5s"/>
      <animate attributeName="x2" values="480;360" dur="2s" repeatCount="indefinite" begin="5s"/>
      <animate attributeName="y2" values="80;160" dur="2s" repeatCount="indefinite" begin="5s"/>
    </line>
  </g>

  <!-- morning star -->
  <g transform="translate(700, 85)" filter="url(#bigStarGlow)">
    <circle r="11" fill="#fff8dc" opacity="0.95">
      <animate attributeName="r" values="10;13;10" dur="4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;1;0.8" dur="4s" repeatCount="indefinite"/>
    </circle>
    <path d="M0,-26 L2.5,-14 L14,-11 L4.5,-4.5 L7,7 L0,0 L-7,7 L-4.5,-4.5 L-14,-11 L-2.5,-14 Z" fill="#ffe9a8" opacity="0.9" filter="url(#starGlow)">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="80s" repeatCount="indefinite"/>
    </path>
  </g>

  <!-- title -->
  <text x="50%" y="165" font-family="Georgia, 'Times New Roman', serif" font-size="70" font-weight="700" fill="#fff8dc" text-anchor="middle" letter-spacing="10" filter="url(#starGlow)">
    MS33834
  </text>
  <text x="50%" y="218" font-family="Georgia, 'Times New Roman', serif" font-size="28" fill="#c9d6f2" text-anchor="middle" letter-spacing="7" opacity="0.92">
    MORNING STAR
  </text>
  <text x="50%" y="260" font-family="'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="18" fill="#9bb3e0" text-anchor="middle" letter-spacing="1">
    Keep shining before the dawn
  </text>

  <!-- horizon line -->
  <line x1="200" y1="305" x2="620" y2="305" stroke="#7b9bcf" stroke-width="1.2" opacity="0.4">
    <animate attributeName="x1" values="200;250;200" dur="8s" repeatCount="indefinite"/>
    <animate attributeName="x2" values="620;570;620" dur="8s" repeatCount="indefinite"/>
  </line>
</svg>
<!-- HERO-SVG-END -->

<br>

<img src="https://readme-typing-svg.demolab.com?font=Georgia&size=24&duration=2600&pause=1000&color=FFE9A8&center=true&vCenter=true&width=720&lines=code+like+a+quiet+star+before+dawn;keep+learning%2C+keep+building%2C+keep+shining;every+commit+is+a+spark+in+the+dark" alt="typing"/>

</div>

<br>

> 🌙 *Click any "中文" toggle below to see the Chinese version.*

<br>

## ✨ About Me

<div align="center">

# I am **badhope**

<img src="https://readme-typing-svg.demolab.com?font=Noto+Sans+SC&weight=600&size=24&duration=2200&pause=600&color=FFE9A8&center=true&vCenter=true&width=700&lines=积极的开源社区贡献者;优秀的全栈开发者;技巧娴熟的AI使用者;新技术时代的探索者;在代码与星光之间寻找答案" alt="badhope typing"/>

</div>

<br>

<details>
<summary>🌙 中文</summary>

<div align="center">

<pre style="font-size: 16px; line-height: 1.8; background: #0d1535; color: #c9d6f2; padding: 20px; border-radius: 12px; border: 1px solid #25335e;">
名字： MS33834 / badhope
状态： 收集微光，等待黎明
位置： 某片星空之下
博客： CSDN · weixin_56622231
</pre>

</div>

> 每一行代码都是一颗小星星，聚在一起就成了自己的光。

</details>

<div align="center">

<pre style="font-size: 16px; line-height: 1.8; background: #0d1535; color: #c9d6f2; padding: 20px; border-radius: 12px; border: 1px solid #25335e;">
name: MS33834 / badhope
mood: collecting sparks, waiting for dawn
location: somewhere under the stars
blog:  CSDN · weixin_56622231
</pre>

</div>

> Every line of code is a tiny star; together they become your own light.

<br>

## 📝 Latest CSDN Articles

<details>
<summary>🌙 中文：最新 CSDN 文章</summary>

这里展示 CSDN 账号 `weixin_56622231` 最近更新的 5 篇文章，每天 00:00（北京时间）自动同步。

</details>

<!-- CSDN-POSTS-START -->
<div align="center">

<table>
  <tr><td style='color:#4a6fa5; font-size:16px; width:28px;'>✦</td><td><a href='https://blog.csdn.net/weixin_56622231/article/details/162109133' target='_blank' style='font-size:17px; color:#c9d6f2; text-decoration:none;'>Anthropic 的FABLE5到底有什么魅力？为什么这么强？</a><br><sub style='color:#6b7fa3;'>2026-06-18</sub></td></tr>
  <tr><td style='color:#4a6fa5; font-size:16px; width:28px;'>✦</td><td><a href='https://blog.csdn.net/weixin_56622231/article/details/162108919' target='_blank' style='font-size:17px; color:#c9d6f2; text-decoration:none;'>华为的鸿蒙到底有多牛？为什么称作遥遥领先？</a><br><sub style='color:#6b7fa3;'>2026-06-18</sub></td></tr>
  <tr><td style='color:#4a6fa5; font-size:16px; width:28px;'>✦</td><td><a href='https://blog.csdn.net/weixin_56622231/article/details/162108996' target='_blank' style='font-size:17px; color:#c9d6f2; text-decoration:none;'>Codex vs Cursor：2025 AI编程工具深度横评万字长文</a><br><sub style='color:#6b7fa3;'>2026-06-18</sub></td></tr>
  <tr><td style='color:#4a6fa5; font-size:16px; width:28px;'>✦</td><td><a href='https://blog.csdn.net/weixin_56622231/article/details/162109037' target='_blank' style='font-size:17px; color:#c9d6f2; text-decoration:none;'>华为AI沉默之谜：表面低调，实则下着一盘改变格局的超级大棋</a><br><sub style='color:#6b7fa3;'>2026-06-18</sub></td></tr>
  <tr><td style='color:#4a6fa5; font-size:16px; width:28px;'>✦</td><td><a href='https://blog.csdn.net/weixin_56622231/article/details/162108746' target='_blank' style='font-size:17px; color:#c9d6f2; text-decoration:none;'>Dify 自然体框架深度解析：优势、过时之处与 Git 集成之道</a><br><sub style='color:#6b7fa3;'>2026-06-18</sub></td></tr>
</table>
</div>
<!-- CSDN-POSTS-END -->

<br>

## 🌠 Today's Starlight

<details>
<summary>🌙 中文：今日微光</summary>

每日一句英文名言，附带中文翻译，每天自动更新。

</details>

<!-- DAILY-QUOTE-START -->
<div align="center">

<p style="font-size: 24px; color: #ffe9a8; font-style: italic; margin: 18px 0; line-height: 1.5;">"Genius is one percent inspiration and ninety-nine percent perspiration."</p>
<p style="font-size: 17px; color: #8fa4d3;">— Thomas Edison</p>

<details>
<summary style="font-size: 17px; color: #c9d6f2; cursor: pointer; padding: 8px;">🌙 中文</summary>

<p style="font-size: 22px; color: #fff8dc; margin: 14px 0; line-height: 1.5;">人死后会成为什么?夜空中的一座孤岛。</p>
<p style="font-size: 16px; color: #8fa4d3;">— 《一封孤岛的信》</p>

</details>

</div>
<!-- DAILY-QUOTE-END -->

<br>

## 🛠 Tech Stack

<details>
<summary>🌙 中文：技术栈</summary>

根据 GitHub 公开仓库自动统计最常用的编程语言。

</details>

<!-- TECH-STACK-START -->
<div align="center">

![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=ffffff&labelColor=0d1535) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=ffffff&labelColor=0d1535) ![Vue](https://img.shields.io/badge/Vue-4FC08D?style=for-the-badge&logo=vue&logoColor=ffffff&labelColor=0d1535)

</div>
<!-- TECH-STACK-END -->

<br>

## 📊 Star Map

<details>
<summary>🌙 中文：星图</summary>

GitHub 个人统计、常用语言、连续贡献记录。

</details>

<div align="center">

<img height="195" src="https://github-readme-stats.vercel.app/api?username=MS33834&show_icons=true&theme=tokyonight&bg_color=050817&title_color=ffe9a8&text_color=c9d6f2&icon_color=4a6fa5&border_color=25335e&hide=issues&rank_icon=percentile" alt="github stats"/>
<img height="195" src="https://github-readme-stats.vercel.app/api/top-langs/?username=MS33834&layout=compact&theme=tokyonight&bg_color=050817&title_color=ffe9a8&text_color=c9d6f2&icon_color=4a6fa5&border_color=25335e" alt="top languages"/>

<br>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=MS33834&theme=tokyonight&background=050817&border=25335e&stroke=4a6fa5&ring=ffe9a8&fire=ffd700&currStreakNum=ffffff&sideNums=c9d6f2&currStreakLabel=ffe9a8&sideLabels=8fa4d3&dates=6b7fa3" alt="streak stats"/>

</div>

<br>

## 🏆 Top Repositories

<details>
<summary>🌙 中文：我的高星仓库</summary>

按 Star 数量排序的 4 个仓库，每天自动更新。

</details>

<!-- TOP-REPOS-START -->
<div align="center">
<table>
  <tr>
    <td><a href="https://github.com/MS33834/autoship-cli" target="_blank"><img src="https://github-readme-stats.vercel.app/api/pin/?username=MS33834&repo=autoship-cli&theme=tokyonight&bg_color=050817&title_color=ffe9a8&text_color=c9d6f2&icon_color=4a6fa5&border_color=25335e" alt="autoship-cli"/></a></td>
    <td><a href="https://github.com/MS33834/DU" target="_blank"><img src="https://github-readme-stats.vercel.app/api/pin/?username=MS33834&repo=DU&theme=tokyonight&bg_color=050817&title_color=ffe9a8&text_color=c9d6f2&icon_color=4a6fa5&border_color=25335e" alt="DU"/></a></td>
  </tr>
  <tr>
    <td><a href="https://github.com/MS33834/taskflow" target="_blank"><img src="https://github-readme-stats.vercel.app/api/pin/?username=MS33834&repo=taskflow&theme=tokyonight&bg_color=050817&title_color=ffe9a8&text_color=c9d6f2&icon_color=4a6fa5&border_color=25335e" alt="taskflow"/></a></td>
    <td><a href="https://github.com/MS33834/scholarhub" target="_blank"><img src="https://github-readme-stats.vercel.app/api/pin/?username=MS33834&repo=scholarhub&theme=tokyonight&bg_color=050817&title_color=ffe9a8&text_color=c9d6f2&icon_color=4a6fa5&border_color=25335e" alt="scholarhub"/></a></td>
  </tr>
</table>
</div>
<!-- TOP-REPOS-END -->

<br>

## 🌌 Trending Repositories

<details>
<summary>🌙 中文：GitHub 热榜</summary>

当前 GitHub 上 Star 数较高的 4 个仓库，每天自动更新。

</details>

<!-- TRENDING-REPOS-START -->
| Repository | Description | Stars |
|------------|-------------|-------|
| [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Master programming by recreating your favorite technolo... | ⭐ 517,149 |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 😎 Awesome lists about all kinds of interesting topics | ⭐ 476,911 |
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | freeCodeCamp.org's open-source codebase and curriculum.... | ⭐ 449,608 |
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs | ⭐ 442,638 |
<!-- TRENDING-REPOS-END -->

<br>

## 🐍 Constellation Snake

<details>
<summary>🌙 中文：贪吃蛇星图</summary>

一条由 GitHub 贡献记录生成的「星空贪吃蛇」，每天自动更新。

</details>

<div align="center">

<img src="https://raw.githubusercontent.com/MS33834/MS33834/output/github-snake-dark.svg#gh-dark-mode-only" alt="snake dark" width="100%" style="max-width: 820px;"/>
<img src="https://raw.githubusercontent.com/MS33834/MS33834/output/github-snake.svg#gh-light-mode-only" alt="snake light" width="100%" style="max-width: 820px;"/>

</div>

<br>

## 🔥 Activity & Contributions

<details>
<summary>🌙 中文：活跃度与贡献</summary>

Issue / PR 统计、贡献趋势图、GitHub 奖杯。

</details>

<div align="center">

<img src="https://img.shields.io/github/issues-search?query=author%3AMS33834+type%3Aissue&label=Issues%20created&color=4a6fa5&style=for-the-badge&labelColor=0d1535" alt="issues"/>
<img src="https://img.shields.io/github/issues-search?query=author%3AMS33834+type%3Apr&label=Pull%20requests&color=ffe9a8&style=for-the-badge&labelColor=0d1535" alt="prs"/>
<img src="https://img.shields.io/github/issues-search?query=author%3AMS33834+type%3Apr+is%3Amerged&label=Merged%20PRs&color=4fc08d&style=for-the-badge&labelColor=0d1535" alt="merged prs"/>

<br><br>

<img src="https://github-profile-trophy.vercel.app/?username=MS33834&theme=tokyonight&no-frame=true&margin-w=8&margin-h=8&column=7" alt="trophies"/>

<br><br>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=MS33834&theme=tokyo-night&bg_color=050817&color=c9d6f2&line=ffe9a8&point=4a6fa5&area=true&hide_border=true" alt="activity graph" width="100%" style="max-width: 860px;"/>

</div>

<br>

## 🌐 Connect With Me

<details>
<summary>🌙 中文：找到我</summary>

- CSDN：weixin_56622231
- GitHub：MS33834

</details>

<div align="center">

<a href="https://blog.csdn.net/weixin_56622231" target="_blank">
  <img src="https://img.shields.io/badge/CSDN-weixin__56622231-050817?style=for-the-badge&logo=c&logoColor=ffe9a8&labelColor=0d1535" alt="csdn"/>
</a>
<a href="https://github.com/MS33834" target="_blank">
  <img src="https://img.shields.io/badge/GitHub-MS33834-050817?style=for-the-badge&logo=github&logoColor=ffe9a8&labelColor=0d1535" alt="github"/>
</a>

<br><br>

<img src="https://komarev.com/ghpvc/?username=MS33834&color=050817&style=flat-square&label=visitors" alt="visitors"/>

<br><br>

<pre style="font-size: 15px; color: #4a6fa5;">
*.　　°　　　　☀️·　　　　🛸　　　 　🌏　°　　🌓　•　　.°•　　　✯
　　　★　*　　　　　°　　　　🛰　°·　　　　.　　　•　°★　•
▁▂▃▄▅▆▇▇▆▅▄▃▂▁   theme: morning star   ▁▂▃▄▅▆▇▇▆▅▄▃▂▁
</pre>

</div>

<div align="center">

<!-- HERO-SVG-START -->
<svg viewBox="0 0 860 400" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width: 900px;">
  <defs>
    <linearGradient id="sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#02030a"/>
      <stop offset="40%" stop-color="#081029"/>
      <stop offset="75%" stop-color="#13204a"/>
      <stop offset="100%" stop-color="#24356b"/>
    </linearGradient>
    <radialGradient id="morningGlow" cx="76%" cy="20%" r="58%">
      <stop offset="0%" stop-color="#ffe9a8" stop-opacity="0.5"/>
      <stop offset="30%" stop-color="#7b9bcf" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#030511" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="nebula1" cx="18%" cy="82%" r="48%">
      <stop offset="0%" stop-color="#6b4c9a" stop-opacity="0.28"/>
      <stop offset="60%" stop-color="#4a6fa5" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#030511" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="nebula2" cx="88%" cy="78%" r="42%">
      <stop offset="0%" stop-color="#a88fbb" stop-opacity="0.2"/>
      <stop offset="70%" stop-color="#4a6fa5" stop-opacity="0.06"/>
      <stop offset="100%" stop-color="#030511" stop-opacity="0"/>
    </radialGradient>
    <filter id="starGlow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="1.8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="bigStarGlow" x="-120%" y="-120%" width="340%" height="340%">
      <feGaussianBlur stdDeviation="7" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="moonGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="4.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="textGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect width="860" height="400" rx="18" fill="url(#sky)"/>
  <rect width="860" height="400" rx="18" fill="url(#morningGlow)"/>
  <rect width="860" height="400" rx="18" fill="url(#nebula1)"/>
  <rect width="860" height="400" rx="18" fill="url(#nebula2)"/>

  <!-- star field -->
  <g fill="#ffffff">
    <circle cx="50" cy="45" r="1.2" opacity="0.5"><animate attributeName="opacity" values="0.2;1;0.2" dur="2.6s" repeatCount="indefinite"/></circle>
    <circle cx="115" cy="88" r="1" opacity="0.5"><animate attributeName="opacity" values="0.3;0.9;0.3" dur="3.4s" repeatCount="indefinite" begin="0.4s"/></circle>
    <circle cx="195" cy="38" r="1.4" opacity="0.6"><animate attributeName="opacity" values="0.2;1;0.2" dur="2.2s" repeatCount="indefinite" begin="1.1s"/></circle>
    <circle cx="275" cy="122" r="1.1" opacity="0.5"><animate attributeName="opacity" values="0.3;0.85;0.3" dur="3.8s" repeatCount="indefinite" begin="0.2s"/></circle>
    <circle cx="365" cy="58" r="1.3" opacity="0.6"><animate attributeName="opacity" values="0.2;1;0.2" dur="3s" repeatCount="indefinite" begin="0.7s"/></circle>
    <circle cx="440" cy="100" r="1" opacity="0.5"><animate attributeName="opacity" values="0.3;0.9;0.3" dur="2.7s" repeatCount="indefinite" begin="1.5s"/></circle>
    <circle cx="530" cy="42" r="1.5" opacity="0.6"><animate attributeName="opacity" values="0.2;1;0.2" dur="3.6s" repeatCount="indefinite" begin="0.1s"/></circle>
    <circle cx="615" cy="132" r="1.1" opacity="0.5"><animate attributeName="opacity" values="0.3;0.85;0.3" dur="2.4s" repeatCount="indefinite" begin="0.9s"/></circle>
    <circle cx="705" cy="58" r="1.2" opacity="0.6"><animate attributeName="opacity" values="0.2;1;0.2" dur="3.2s" repeatCount="indefinite" begin="1.3s"/></circle>
    <circle cx="795" cy="108" r="1" opacity="0.5"><animate attributeName="opacity" values="0.3;0.9;0.3" dur="4s" repeatCount="indefinite" begin="0.5s"/></circle>
    <circle cx="80" cy="180" r="1.1" opacity="0.5"><animate attributeName="opacity" values="0.2;0.85;0.2" dur="2.8s" repeatCount="indefinite" begin="1.7s"/></circle>
    <circle cx="165" cy="225" r="1.3" opacity="0.6"><animate attributeName="opacity" values="0.3;1;0.3" dur="2.5s" repeatCount="indefinite" begin="0.3s"/></circle>
    <circle cx="265" cy="270" r="1" opacity="0.5"><animate attributeName="opacity" values="0.2;0.8;0.2" dur="3.3s" repeatCount="indefinite" begin="1s"/></circle>
    <circle cx="375" cy="308" r="1.1" opacity="0.5"><animate attributeName="opacity" values="0.3;0.9;0.3" dur="2.3s" repeatCount="indefinite" begin="0.6s"/></circle>
    <circle cx="490" cy="270" r="1.2" opacity="0.6"><animate attributeName="opacity" values="0.2;1;0.2" dur="3.5s" repeatCount="indefinite" begin="1.4s"/></circle>
    <circle cx="610" cy="310" r="1" opacity="0.5"><animate attributeName="opacity" values="0.3;0.85;0.3" dur="2.6s" repeatCount="indefinite" begin="0.2s"/></circle>
    <circle cx="730" cy="265" r="1.3" opacity="0.6"><animate attributeName="opacity" values="0.2;1;0.2" dur="3.8s" repeatCount="indefinite" begin="1.2s"/></circle>
    <circle cx="820" cy="310" r="1" opacity="0.5"><animate attributeName="opacity" values="0.3;0.9;0.3" dur="2.9s" repeatCount="indefinite" begin="0.8s"/></circle>
  </g>

  <!-- constellation lines -->
  <g stroke="#7b9bcf" stroke-width="0.7" opacity="0.32">
    <line x1="115" y1="88" x2="195" y2="38"/>
    <line x1="195" y1="38" x2="275" y2="122"/>
    <line x1="275" y1="122" x2="365" y2="58"/>
    <line x1="365" y1="58" x2="440" y2="100"/>
    <line x1="530" y1="42" x2="615" y2="132"/>
    <line x1="615" y1="132" x2="705" y2="58"/>
    <line x1="705" y1="58" x2="795" y2="108"/>
  </g>

  <!-- crescent moon -->
  <g transform="translate(130, 82)" filter="url(#moonGlow)">
    <path d="M0,-24 A24,24 0 1,1 0,24 A17,17 0 1,0 0,-24 Z" fill="#fff8dc" opacity="0.85"/>
  </g>

  <!-- shooting star 1 -->
  <g opacity="0">
    <line x1="820" y1="40" x2="720" y2="105" stroke="#ffe9a8" stroke-width="1.8" stroke-linecap="round">
      <animate attributeName="opacity" values="0;1;0" dur="2.2s" repeatCount="indefinite" begin="1.2s"/>
      <animate attributeName="x1" values="820;660" dur="2.2s" repeatCount="indefinite" begin="1.2s"/>
      <animate attributeName="y1" values="40;135" dur="2.2s" repeatCount="indefinite" begin="1.2s"/>
      <animate attributeName="x2" values="720;560" dur="2.2s" repeatCount="indefinite" begin="1.2s"/>
      <animate attributeName="y2" values="105;200" dur="2.2s" repeatCount="indefinite" begin="1.2s"/>
    </line>
  </g>

  <!-- shooting star 2 -->
  <g opacity="0">
    <line x1="580" y1="32" x2="510" y2="88" stroke="#fff8dc" stroke-width="1.4" stroke-linecap="round">
      <animate attributeName="opacity" values="0;0.8;0" dur="1.9s" repeatCount="indefinite" begin="5.2s"/>
      <animate attributeName="x1" values="580;460" dur="1.9s" repeatCount="indefinite" begin="5.2s"/>
      <animate attributeName="y1" values="32;118" dur="1.9s" repeatCount="indefinite" begin="5.2s"/>
      <animate attributeName="x2" values="510;390" dur="1.9s" repeatCount="indefinite" begin="5.2s"/>
      <animate attributeName="y2" values="88;174" dur="1.9s" repeatCount="indefinite" begin="5.2s"/>
    </line>
  </g>

  <!-- morning star -->
  <g transform="translate(730, 92)" filter="url(#bigStarGlow)">
    <circle r="12" fill="#fff8dc" opacity="0.95">
      <animate attributeName="r" values="11;14;11" dur="4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;1;0.8" dur="4s" repeatCount="indefinite"/>
    </circle>
    <path d="M0,-28 L2.5,-15 L15,-12 L4.5,-5 L7,7 L0,0 L-7,7 L-4.5,-5 L-15,-12 L-2.5,-15 Z" fill="#ffe9a8" opacity="0.9" filter="url(#starGlow)">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="75s" repeatCount="indefinite"/>
    </path>
  </g>

  <!-- title -->
  <text x="50%" y="180" font-family="Georgia, 'Times New Roman', serif" font-size="74" font-weight="700" fill="#fff8dc" text-anchor="middle" letter-spacing="12" filter="url(#textGlow)">
    MS33834
  </text>
  <text x="50%" y="235" font-family="Georgia, 'Times New Roman', serif" font-size="30" fill="#c9d6f2" text-anchor="middle" letter-spacing="8" opacity="0.92">
    MORNING STAR
  </text>
  <text x="50%" y="282" font-family="'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="20" fill="#9bb3e0" text-anchor="middle" letter-spacing="1">
    Keep shining before the dawn · badhope
  </text>

  <!-- horizon line -->
  <line x1="220" y1="335" x2="640" y2="335" stroke="#7b9bcf" stroke-width="1.3" opacity="0.4">
    <animate attributeName="x1" values="220;270;220" dur="8s" repeatCount="indefinite"/>
    <animate attributeName="x2" values="640;590;640" dur="8s" repeatCount="indefinite"/>
  </line>
</svg>
<!-- HERO-SVG-END -->

<br>

<!-- self-contained hero typing animation: no external service -->
<svg viewBox="0 0 760 58" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:760px;">
  <defs>
    <linearGradient id="heroTypingGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffe9a8"/>
      <stop offset="100%" stop-color="#7b9bcf"/>
    </linearGradient>
    <filter id="heroTypingGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="1.6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <text x="50%" y="42" font-family="'Space Grotesk','Segoe UI',sans-serif" font-size="28" font-weight="500" fill="url(#heroTypingGrad)" text-anchor="middle" filter="url(#heroTypingGlow)" opacity="0">
    <tspan>code like a quiet star before dawn</tspan>
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.08;0.92;1" dur="12s" begin="0s" repeatCount="indefinite"/>
  </text>
  <text x="50%" y="42" font-family="'Space Grotesk','Segoe UI',sans-serif" font-size="28" font-weight="500" fill="url(#heroTypingGrad)" text-anchor="middle" filter="url(#heroTypingGlow)" opacity="0">
    <tspan>keep learning, keep building, keep shining</tspan>
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.08;0.92;1" dur="12s" begin="4s" repeatCount="indefinite"/>
  </text>
  <text x="50%" y="42" font-family="'Space Grotesk','Segoe UI',sans-serif" font-size="28" font-weight="500" fill="url(#heroTypingGrad)" text-anchor="middle" filter="url(#heroTypingGlow)" opacity="0">
    <tspan>every commit is a spark in the dark</tspan>
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.08;0.92;1" dur="12s" begin="8s" repeatCount="indefinite"/>
  </text>
</svg>

</div>

<br>

> <span style="font-size:20px;">🌙 *Click any "中文" toggle below to see the Chinese version.*</span>

<br>

## ✨ About Me

<div align="center">

<h1 style="font-size:54px; color:#fff8dc; margin:12px 0;">I am <strong style="color:#ffe9a8;">badhope</strong></h1>

<!-- self-contained typing animation: no external service -->
<svg viewBox="0 0 760 58" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:760px;">
  <defs>
    <linearGradient id="typingGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffe9a8"/>
      <stop offset="100%" stop-color="#7b9bcf"/>
    </linearGradient>
    <filter id="typingGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="1.6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <text x="50%" y="42" font-family="'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif" font-size="28" font-weight="600" fill="url(#typingGrad)" text-anchor="middle" filter="url(#typingGlow)" opacity="0">
    <tspan>在代码与星光之间寻找答案</tspan>
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.08;0.92;1" dur="12s" begin="0s" repeatCount="indefinite"/>
  </text>
  <text x="50%" y="42" font-family="'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif" font-size="28" font-weight="600" fill="url(#typingGrad)" text-anchor="middle" filter="url(#typingGlow)" opacity="0">
    <tspan>收集微光，等待黎明</tspan>
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.08;0.92;1" dur="12s" begin="2.4s" repeatCount="indefinite"/>
  </text>
  <text x="50%" y="42" font-family="'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif" font-size="28" font-weight="600" fill="url(#typingGrad)" text-anchor="middle" filter="url(#typingGlow)" opacity="0">
    <tspan>全栈开发者 · 开源探索者</tspan>
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.08;0.92;1" dur="12s" begin="4.8s" repeatCount="indefinite"/>
  </text>
  <text x="50%" y="42" font-family="'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif" font-size="28" font-weight="600" fill="url(#typingGrad)" text-anchor="middle" filter="url(#typingGlow)" opacity="0">
    <tspan>用 AI 作桨，驶向未知的星域</tspan>
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.08;0.92;1" dur="12s" begin="7.2s" repeatCount="indefinite"/>
  </text>
  <text x="50%" y="42" font-family="'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif" font-size="28" font-weight="600" fill="url(#typingGrad)" text-anchor="middle" filter="url(#typingGlow)" opacity="0">
    <tspan>每一行代码都是一颗小星星</tspan>
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.08;0.92;1" dur="12s" begin="9.6s" repeatCount="indefinite"/>
  </text>
</svg>

</div>

<br>

<details>
<summary><span style="font-size:20px;">🌙 中文</span></summary>

<div align="center">

<pre style="font-size: 20px; line-height: 2; background: #0d1535; color: #c9d6f2; padding: 24px; border-radius: 16px; border: 1px solid #25335e;">
名字： MS33834 / badhope
状态： 收集微光，等待黎明
位置： 某片星空之下
博客： CSDN · weixin_56622231
</pre>

</div>

> <span style="font-size:20px;">每一行代码都是一颗小星星，聚在一起就成了自己的光。</span>

</details>

<div align="center">

<pre style="font-size: 20px; line-height: 2; background: #0d1535; color: #c9d6f2; padding: 24px; border-radius: 16px; border: 1px solid #25335e;">
name: MS33834 / badhope
mood: collecting sparks, waiting for dawn
location: somewhere under the stars
blog:  CSDN · weixin_56622231
</pre>

</div>

> <span style="font-size:20px;">Every line of code is a tiny star; together they become your own light.</span>

<br>

## 📝 Latest CSDN Articles

<details>
<summary><span style="font-size:20px;">🌙 中文：最新 CSDN 文章</span></summary>

这里展示 CSDN 账号 `weixin_56622231` 最近更新的 5 篇文章，每天 00:00（北京时间）自动同步。

</details>

<!-- CSDN-POSTS-START -->
<div align="center">

<table>
  <tr><td style='color:#4a6fa5; font-size:20px; width:36px;'>✦</td><td><a href='https://blog.csdn.net/weixin_56622231/article/details/162109133' target='_blank' style='font-size:21px; color:#c9d6f2; text-decoration:none;'>Anthropic 的FABLE5到底有什么魅力？为什么这么强？</a><br><sub style='color:#6b7fa3; font-size:17px;'>2026-06-18</sub></td></tr>
  <tr><td style='color:#4a6fa5; font-size:20px; width:36px;'>✦</td><td><a href='https://blog.csdn.net/weixin_56622231/article/details/162108919' target='_blank' style='font-size:21px; color:#c9d6f2; text-decoration:none;'>华为的鸿蒙到底有多牛？为什么称作遥遥领先？</a><br><sub style='color:#6b7fa3; font-size:17px;'>2026-06-18</sub></td></tr>
  <tr><td style='color:#4a6fa5; font-size:20px; width:36px;'>✦</td><td><a href='https://blog.csdn.net/weixin_56622231/article/details/162108996' target='_blank' style='font-size:21px; color:#c9d6f2; text-decoration:none;'>Codex vs Cursor：2025 AI编程工具深度横评万字长文</a><br><sub style='color:#6b7fa3; font-size:17px;'>2026-06-18</sub></td></tr>
  <tr><td style='color:#4a6fa5; font-size:20px; width:36px;'>✦</td><td><a href='https://blog.csdn.net/weixin_56622231/article/details/162109037' target='_blank' style='font-size:21px; color:#c9d6f2; text-decoration:none;'>华为AI沉默之谜：表面低调，实则下着一盘改变格局的超级大棋</a><br><sub style='color:#6b7fa3; font-size:17px;'>2026-06-18</sub></td></tr>
  <tr><td style='color:#4a6fa5; font-size:20px; width:36px;'>✦</td><td><a href='https://blog.csdn.net/weixin_56622231/article/details/162108746' target='_blank' style='font-size:21px; color:#c9d6f2; text-decoration:none;'>Dify 自然体框架深度解析：优势、过时之处与 Git 集成之道</a><br><sub style='color:#6b7fa3; font-size:17px;'>2026-06-18</sub></td></tr>
</table>
</div>
<!-- CSDN-POSTS-END -->

<br>

## 🌠 Today's Starlight

<details>
<summary><span style="font-size:20px;">🌙 中文：今日微光</span></summary>

每日一句英文名言，附带中文翻译，每天自动更新。

</details>

<!-- DAILY-QUOTE-START -->
<div align="center">

<p style="font-size: 28px; color: #ffe9a8; font-style: italic; margin: 24px 0; line-height: 1.65;">"All we have to decide is what to do with the time that is given to us."</p>
<p style="font-size: 21px; color: #8fa4d3;">— J.R.R. Tolkien</p>

<details>
<summary style="font-size: 21px; color: #c9d6f2; cursor: pointer; padding: 12px;">🌙 中文</summary>

<p style="font-size: 26px; color: #fff8dc; margin: 18px 0; line-height: 1.65;">为遇一人而入红尘，人去我亦去，此生不留尘。</p>
<p style="font-size: 19px; color: #8fa4d3;">— 《魔道祖师》</p>

</details>

</div>
<!-- DAILY-QUOTE-END -->

<br>

## 🛠 Tech Stack

<details>
<summary><span style="font-size:20px;">🌙 中文：技术栈</span></summary>

根据 GitHub 公开仓库自动统计最常用的编程语言。

</details>

<!-- TECH-STACK-START -->
<div align="center">

<img src="https://skillicons.dev/icons?i=ts,py,vue&theme=dark&perline=8" alt="tech stack" style="max-width: 720px;"/>

</div>
<!-- TECH-STACK-END -->

<br>

## 📊 Star Map

<details>
<summary><span style="font-size:20px;">🌙 中文：星图</span></summary>

GitHub 个人统计、常用语言、连续贡献记录。

</details>

<div align="center">

<a href="https://github.com/MS33834" target="_blank">
  <img height="210" src="https://github-readme-stats.vercel.app/api?username=MS33834&show_icons=true&theme=tokyonight&bg_color=050817&title_color=ffe9a8&text_color=c9d6f2&icon_color=4a6fa5&border_color=25335e&hide=issues&rank_icon=percentile&custom_title=MS33834's%20Star%20Map" alt="github stats"/>
</a>
<a href="https://github.com/MS33834" target="_blank">
  <img height="210" src="https://github-readme-stats.vercel.app/api/top-langs/?username=MS33834&layout=compact&theme=tokyonight&bg_color=050817&title_color=ffe9a8&text_color=c9d6f2&icon_color=4a6fa5&border_color=25335e" alt="top languages"/>
</a>

<br>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=MS33834&theme=tokyonight&background=050817&border=25335e&stroke=4a6fa5&ring=ffe9a8&fire=ffd700&currStreakNum=ffffff&sideNums=c9d6f2&currStreakLabel=ffe9a8&sideLabels=8fa4d3&dates=6b7fa3" alt="streak stats"/>

<br>

<sub style="font-size:17px; color:#6b7fa3;">If the star maps above do not render, you can still view them on <a href="https://github.com/MS33834" target="_blank" style="color:#ffe9a8;">my GitHub profile</a>.</sub>

</div>

<br>

## 🏆 Top Repositories

<details>
<summary><span style="font-size:20px;">🌙 中文：我的高星仓库</span></summary>

按 Star 数量排序的 4 个仓库，每天自动更新。

</details>

<!-- TOP-REPOS-START -->
<div align="center">
<table>
  <tr>
    <td><a href="https://github.com/MS33834/urban-pulse" target="_blank"><img src="https://github-readme-stats.vercel.app/api/pin/?username=MS33834&repo=urban-pulse&theme=tokyonight&bg_color=050817&title_color=ffe9a8&text_color=c9d6f2&icon_color=4a6fa5&border_color=25335e" alt="urban-pulse"/></a></td>
    <td><a href="https://github.com/MS33834/AI-SKILL" target="_blank"><img src="https://github-readme-stats.vercel.app/api/pin/?username=MS33834&repo=AI-SKILL&theme=tokyonight&bg_color=050817&title_color=ffe9a8&text_color=c9d6f2&icon_color=4a6fa5&border_color=25335e" alt="AI-SKILL"/></a></td>
  </tr>
  <tr>
    <td><a href="https://github.com/MS33834/financial-agent" target="_blank"><img src="https://github-readme-stats.vercel.app/api/pin/?username=MS33834&repo=financial-agent&theme=tokyonight&bg_color=050817&title_color=ffe9a8&text_color=c9d6f2&icon_color=4a6fa5&border_color=25335e" alt="financial-agent"/></a></td>
    <td><a href="https://github.com/MS33834/autoship-cli" target="_blank"><img src="https://github-readme-stats.vercel.app/api/pin/?username=MS33834&repo=autoship-cli&theme=tokyonight&bg_color=050817&title_color=ffe9a8&text_color=c9d6f2&icon_color=4a6fa5&border_color=25335e" alt="autoship-cli"/></a></td>
  </tr>
</table>
</div>
<!-- TOP-REPOS-END -->

<br>

## 🌌 Trending Repositories

<details>
<summary><span style="font-size:20px;">🌙 中文：GitHub 热榜</span></summary>

当前 GitHub 上 Star 数较高的 4 个仓库，每天自动更新。

</details>

<!-- TRENDING-REPOS-START -->
| Repository | Description | Stars |
|------------|-------------|-------|
| [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Master programming by recreating your favorite technolo... | ⭐ 517,406 |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 😎 Awesome lists about all kinds of interesting topics | ⭐ 477,125 |
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | freeCodeCamp.org's open-source codebase and curriculum.... | ⭐ 449,794 |
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs | ⭐ 442,850 |
<!-- TRENDING-REPOS-END -->

<br>

<!-- hand-crafted constellation divider -->
<div align="center">
<svg viewBox="0 0 860 28" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:860px;">
  <line x1="0" y1="14" x2="360" y2="14" stroke="#25335e" stroke-width="1.2"/>
  <line x1="500" y1="14" x2="860" y2="14" stroke="#25335e" stroke-width="1.2"/>
  <circle cx="430" cy="14" r="4" fill="#ffe9a8" opacity="0.9"/>
  <circle cx="400" cy="14" r="2" fill="#4a6fa5" opacity="0.7"/>
  <circle cx="460" cy="14" r="2" fill="#4a6fa5" opacity="0.7"/>
  <line x1="404" y1="14" x2="426" y2="14" stroke="#4a6fa5" stroke-width="0.8" opacity="0.5"/>
  <line x1="434" y1="14" x2="456" y2="14" stroke="#4a6fa5" stroke-width="0.8" opacity="0.5"/>
</svg>
</div>

<br>

## 🐍 Constellation Snake

<details>
<summary><span style="font-size:20px;">🌙 中文：贪吃蛇星图</span></summary>

一条由 GitHub 贡献记录生成的「星空贪吃蛇」，每天自动更新。

</details>

<div align="center">

<img src="https://raw.githubusercontent.com/MS33834/MS33834/output/github-snake-dark.svg#gh-dark-mode-only" alt="snake dark" width="100%" style="max-width: 860px;"/>
<img src="https://raw.githubusercontent.com/MS33834/MS33834/output/github-snake.svg#gh-light-mode-only" alt="snake light" width="100%" style="max-width: 860px;"/>

</div>

<br>

## 🔥 Activity & Contributions

<details>
<summary><span style="font-size:20px;">🌙 中文：活跃度与贡献</span></summary>

Issue / PR 统计、贡献趋势图、GitHub 奖杯。

</details>

<div align="center">

<!-- hand-crafted activity badges instead of generic shields.io -->
<a href="https://github.com/search?q=author%3AMS33834+type%3Aissue&type=issues" target="_blank">
  <svg xmlns="http://www.w3.org/2000/svg" width="172" height="40" role="img" aria-label="Issues created">
    <rect x="1" y="1" width="170" height="38" rx="10" fill="#0d1535" stroke="#4a6fa5" stroke-width="1.2"/>
    <circle cx="22" cy="20" r="6" fill="#4a6fa5" opacity="0.9"/>
    <text x="38" y="25" font-family="'Segoe UI',sans-serif" font-size="14" font-weight="600" fill="#c9d6f2">Issues created</text>
  </svg>
</a>
<a href="https://github.com/search?q=author%3AMS33834+type%3Apr&type=pullrequests" target="_blank">
  <svg xmlns="http://www.w3.org/2000/svg" width="188" height="40" role="img" aria-label="Pull requests">
    <rect x="1" y="1" width="186" height="38" rx="10" fill="#0d1535" stroke="#ffe9a8" stroke-width="1.2"/>
    <path d="M16 20 L24 14 L24 18 L30 18 L30 22 L24 22 L24 26 Z" fill="#ffe9a8" opacity="0.95"/>
    <text x="40" y="25" font-family="'Segoe UI',sans-serif" font-size="14" font-weight="600" fill="#c9d6f2">Pull requests</text>
  </svg>
</a>
<a href="https://github.com/search?q=author%3AMS33834+type%3Apr+is%3Amerged&type=pullrequests" target="_blank">
  <svg xmlns="http://www.w3.org/2000/svg" width="188" height="40" role="img" aria-label="Merged PRs">
    <rect x="1" y="1" width="186" height="38" rx="10" fill="#0d1535" stroke="#4fc08d" stroke-width="1.2"/>
    <path d="M18 14 L26 20 L18 26 L20 28 L30 20 L20 12 Z" fill="#4fc08d" opacity="0.95"/>
    <text x="42" y="25" font-family="'Segoe UI',sans-serif" font-size="14" font-weight="600" fill="#c9d6f2">Merged PRs</text>
  </svg>
</a>

<br><br>

<img src="https://github-profile-trophy.vercel.app/?username=MS33834&theme=tokyonight&no-frame=true&margin-w=10&margin-h=10&column=7" alt="trophies"/>

<br><br>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=MS33834&theme=tokyo-night&bg_color=050817&color=c9d6f2&line=ffe9a8&point=4a6fa5&area=true&hide_border=true" alt="activity graph" width="100%" style="max-width: 860px;"/>

<br>

<sub style="font-size:17px; color:#6b7fa3;">If the activity charts above do not load, visit <a href="https://github.com/MS33834" target="_blank" style="color:#ffe9a8;">my profile</a> directly.</sub>

</div>

<br>

## 🌐 Connect With Me

<details>
<summary><span style="font-size:20px;">🌙 中文：找到我</span></summary>

- CSDN：weixin_56622231
- GitHub：MS33834

</details>

<div align="center">

<!-- hand-crafted connect buttons instead of generic shields.io -->
<a href="https://blog.csdn.net/weixin_56622231" target="_blank">
  <svg xmlns="http://www.w3.org/2000/svg" width="220" height="44" role="img" aria-label="CSDN blog">
    <defs>
      <linearGradient id="csdnGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#0d1535"/>
        <stop offset="100%" stop-color="#16235a"/>
      </linearGradient>
    </defs>
    <rect x="1" y="1" width="218" height="42" rx="12" fill="url(#csdnGrad)" stroke="#4a6fa5" stroke-width="1.2"/>
    <circle cx="24" cy="22" r="8" fill="#ffe9a8"/>
    <text x="24" y="26" font-family="'Segoe UI',sans-serif" font-size="12" font-weight="700" fill="#0d1535" text-anchor="middle">C</text>
    <text x="44" y="27" font-family="'Segoe UI',sans-serif" font-size="15" font-weight="600" fill="#c9d6f2">CSDN · weixin_56622231</text>
  </svg>
</a>
<a href="https://github.com/MS33834" target="_blank">
  <svg xmlns="http://www.w3.org/2000/svg" width="180" height="44" role="img" aria-label="GitHub profile">
    <defs>
      <linearGradient id="ghGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#0d1535"/>
        <stop offset="100%" stop-color="#16235a"/>
      </linearGradient>
    </defs>
    <rect x="1" y="1" width="178" height="42" rx="12" fill="url(#ghGrad)" stroke="#ffe9a8" stroke-width="1.2"/>
    <path d="M24 12 C17 12 12 17.5 12 23.5 C12 28.5 15 32.5 19.5 34 C20 34 20.2 33.6 20.2 33.2 L20.2 31 C17.5 31.5 17 29.5 17 29.5 C16.5 28 15.8 27.7 15.8 27.7 C14.8 27 15.8 27 15.8 27 C16.9 27.1 17.5 28 17.5 28 C18.4 29.6 20 29.1 20.3 28.9 C20.4 28.2 20.7 27.7 21 27.4 C18.6 27.1 16 26.1 16 22 C16 20.5 16.6 19.3 17.5 18.3 C17.3 17.8 16.9 16.5 17.6 14.6 C17.6 14.6 18.6 14.2 20.2 15.5 C21 15.2 22 15.1 23 15.1 C24 15.1 25 15.2 25.8 15.5 C27.4 14.2 28.4 14.6 28.4 14.6 C29.1 16.5 28.7 17.8 28.5 18.3 C29.4 19.3 30 20.5 30 22 C30 26.1 27.4 27.1 25 27.4 C25.4 27.8 25.8 28.6 25.8 29.7 L25.8 33.2 C25.8 33.6 26 34 26.5 34 C31 32.5 34 28.5 34 23.5 C34 17.5 29 12 24 12 Z" fill="#ffe9a8"/>
    <text x="48" y="27" font-family="'Segoe UI',sans-serif" font-size="15" font-weight="600" fill="#c9d6f2">GitHub · MS33834</text>
  </svg>
</a>

<br><br>

<img src="https://komarev.com/ghpvc/?username=MS33834&color=050817&style=flat-square&label=visitors" alt="visitors"/>

<br><br>

<pre style="font-size: 20px; color: #4a6fa5; line-height: 1.7;">
*.　　°　　　　☀️·　　　　🛸　　　 　🌏　°　　🌓　•　　.°•　　　✯
　　　★　*　　　　　°　　　　🛰　°·　　　　.　　　•　°★　•
▁▂▃▄▅▆▇▇▆▅▄▃▂▁   theme: morning star   ▁▂▃▄▅▆▇▇▆▅▄▃▂▁
</pre>

</div>

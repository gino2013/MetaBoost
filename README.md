<div align="center">
  <img src="assets/logo.png" width="630" alt="MetaBoost Shiba"/>
  <h1>MetaBoost</h1>
  <p><em>He posts once. Everyone sees it.</em></p>

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Instagram%20%7C%20Threads-black)](https://github.com/gino2013/MetaBoost)
[![Tools](https://img.shields.io/badge/Open%20Source%20Tools-10%2B-black)](docs/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-black.svg)](CONTRIBUTING.md)

</div>

---

## What is MetaBoost?

MetaBoost bundles the **best open-source tools** for Instagram and Threads into one curated guide — with working code, setup instructions, and real-world recipes.

Stop paying for Buffer, Hootsuite, or analytics dashboards. Everything here is free and self-hostable.

---

## What Can You Do?

<table>
<tr>
<td width="50%">

**Schedule & Publish**
- Post to IG + Threads simultaneously
- Visual content calendar
- Bulk upload & scheduling
- AI-assisted caption generation

</td>
<td width="50%">

**Automate Engagement**
- Auto-like relevant hashtag posts
- Auto-follow target audiences
- AI-generated comment replies
- Safe daily limits built-in

</td>
</tr>
<tr>
<td width="50%">

**Analyze & Track**
- Engagement rate per post
- Follower growth tracking
- Competitor content analysis
- Monthly CSV reports

</td>
<td width="50%">

**Threads-Native Tools**
- Official Threads API integration
- Schedule Threads posts
- Monitor + auto-reply comments
- Cross-post IG ↔ Threads

</td>
</tr>
</table>

---

## Quick Start

```bash
# Clone MetaBoost
git clone https://github.com/gino2013/MetaBoost.git
cd MetaBoost

# Set up credentials
cp .env.example .env   # fill in IG_USERNAME, IG_PASSWORD

# Install Python tools
python -m venv venv && source venv/bin/activate
pip install instagrapi instaloader python-dotenv

# Run your first analytics report
python examples/basic_analytics.py
```

**Sample output:**

```
=== @your_account ===
Followers : 4,821
Following : 612
Posts     : 143

Date         Likes  Comments   Eng%  Caption
----------------------------------------------------------------------
2026-06-20     312        18  6.85%  Weekend vibes with my shiba #dog...
2026-06-18     287        24  6.45%  Morning walk routine #shiba #pet...
2026-06-15     401        31  8.96%  New reel dropped! Check it out...
2026-06-12     198        11  4.33%  Simple monday post #life...
```

---

## Tool Directory

### Instagram Automation

| Tool | Stars | What it does |
|------|-------|-------------|
| [InstaPy](https://github.com/InstaPy/InstaPy) | 15k+ | Full automation framework — likes, follows, comments, DMs |
| [instagrapi](https://github.com/subzeroid/instagrapi) | 4k+ | Fastest Python IG Private API (2026 maintained) |
| [igbot](https://github.com/ohld/igbot) | 3k+ | Beginner-friendly scripts, minimal setup |
| [instagram-private-api](https://github.com/dilame/instagram-private-api) | 5k+ | TypeScript SDK for Node.js projects |

### Instagram Analytics

| Tool | Stars | What it does |
|------|-------|-------------|
| [Instaloader](https://github.com/instaloader/instaloader) | 8k+ | Download posts, stories, follower lists, metadata |
| [Osintgram](https://github.com/Datalux/Osintgram) | 9k+ | Interactive shell — deep competitor account analysis |
| [InstagramUnfollowers](https://github.com/davidarroyo1234/InstagramUnfollowers) | 4k+ | Browser-based unfollower checker, zero install |

### Scheduling & Management

| Tool | Stars | What it does |
|------|-------|-------------|
| [BrightBean Studio](https://github.com/brightbeanxyz/brightbean-studio) | - | Self-hostable dashboard, 10+ platforms (Buffer alternative) |
| [DemandBird](https://github.com/DemandBird/demandbird) | - | AI-native pipeline: create → schedule → analyze → repurpose |
| [trypost](https://github.com/trypostit/trypost) | - | Minimal open-source scheduler, easy self-host |
| [postmypost SDK](https://github.com/postmypost/node-rest-sdk) | - | Node.js SDK — IG, Threads, TikTok, Facebook, LinkedIn |

### Threads Tools

| Tool | Stars | What it does |
|------|-------|-------------|
| [schedul-pm](https://github.com/42eleven/schedul-pm) | - | Threads-exclusive content scheduling |
| [comment_copilot](https://github.com/mustcanbedo/comment_copilot) | - | AI reads comments, identifies high-intent users, drafts replies |

---

## Code Demos

### Post to Instagram

```python
from instagrapi import Client

cl = Client()
cl.login("your_username", "your_password")

# Upload photo with caption
media = cl.photo_upload(
    "photo.jpg",
    caption="Good morning! ☀️ #shiba #dogs #morning"
)
print(f"Posted: https://www.instagram.com/p/{media.code}/")
```

### Post to Threads (Official API)

```python
import requests, os

USER_ID = os.getenv("THREADS_USER_ID")
TOKEN   = os.getenv("THREADS_ACCESS_TOKEN")

# Create and publish in 2 steps
container = requests.post(
    f"https://graph.threads.net/v1.0/{USER_ID}/threads",
    params={"media_type": "TEXT", "text": "Hello Threads! 🐕", "access_token": TOKEN}
).json()

requests.post(
    f"https://graph.threads.net/v1.0/{USER_ID}/threads_publish",
    params={"creation_id": container["id"], "access_token": TOKEN}
)
```

### Analyze Your Post Performance

```python
import instaloader

L = instaloader.Instaloader()
L.login("your_username", "your_password")
profile = instaloader.Profile.from_username(L.context, "your_username")

print(f"Followers: {profile.followers}")

for post in profile.get_posts():
    eng = (post.likes + post.comments) / profile.followers * 100
    print(f"{post.date:%Y-%m-%d}  ❤️ {post.likes}  💬 {post.comments}  📊 {eng:.1f}%")
```

### Auto-Engage with Hashtags (with safe limits)

```python
import time, random
from instagrapi import Client

cl = Client()
cl.load_settings("session.json")
cl.login("your_username", "your_password")

TARGET_TAGS   = ["shiba", "dogs", "petlover"]
LIKE_LIMIT    = 80   # per day

liked = 0
for tag in TARGET_TAGS:
    for media in cl.hashtag_medias_recent(tag, amount=25):
        if liked >= LIKE_LIMIT:
            break
        cl.media_like(media.id)
        liked += 1
        time.sleep(random.uniform(4, 10))   # human-like delay

print(f"Liked {liked} posts today")
```

### Find Who Unfollowed You (browser)

No install needed — open Instagram in Chrome, paste this in DevTools Console:

```javascript
// Paste the script from:
// https://github.com/davidarroyo1234/InstagramUnfollowers/releases/latest
// A UI window appears showing who doesn't follow you back
```

### Self-Host a Full Scheduling Dashboard

```bash
git clone https://github.com/brightbeanxyz/brightbean-studio
cd brightbean-studio
cp .env.example .env   # configure DB + API keys
docker-compose up -d
# → Open http://localhost:3000
```

---

## Workflow Examples

### Solo Creator Weekly Routine

```
Mon  Instaloader → pull last week's post data → review what worked
Tue–Fri  BrightBean → scheduled posts go live automatically
         instagrapi → morning engagement run (hashtags)
         comment_copilot → draft replies to comments
Sun  Plan next week → schedule in BrightBean
```

### Brand Account Setup

```
BrightBean Studio   unified dashboard for all accounts
postmypost SDK      programmatic posting for high-volume
Instaloader         monthly analytics export per account
comment_copilot     manage comments at scale
```

---

## Safe Usage Limits

Automation thresholds that keep your account safe:

| Action | Daily Safe Limit | Risky |
|--------|-----------------|-------|
| Likes | < 150 | > 300 |
| Follows | < 50 | > 100 |
| Comments | < 30 | > 60 |
| DMs | < 20 | > 40 |

Always add random delays (4–10 seconds) between actions. Never run bots 24/7.

---

## Docs

| Guide | Description |
|-------|------------|
| [Getting Started](docs/01-getting-started.md) | Environment setup, choose your tool |
| [Instagram Automation](docs/02-instagram-automation.md) | InstaPy, instagrapi, igbot — full guide |
| [Instagram Analytics](docs/03-instagram-analytics.md) | Instaloader, Osintgram, unfollower checker |
| [Social Scheduling](docs/04-social-scheduling.md) | BrightBean, DemandBird, postmypost |
| [Threads Tools](docs/05-threads-tools.md) | Official API, comment_copilot, schedul-pm |
| [Integration Guide](docs/06-integration-guide.md) | Combine tools into full workflows |
| [Use Cases & Recipes](docs/07-use-cases.md) | 5 complete real-world examples |

---

## Disclaimer

Automation tools may violate Instagram's Terms of Service. Always test on secondary accounts first. Use responsibly and respect platform rate limits.

---

## Contributing

PRs, new tool suggestions, and experience sharing are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

MIT — free to use. Keep attribution links.

---

<details>
<summary>中文說明 / Chinese Version</summary>

## 什麼是 MetaBoost？

MetaBoost 整合最強開源工具，讓你的 Instagram 和 Threads 帳號排程、互動、分析全自動化，完全免費自架，不用付費給 Buffer 或 Hootsuite。

## 你可以做什麼？

- **排程發文**：多平台同步發布，視覺化內容日曆，AI 輔助文案
- **自動互動**：自動按讚、追蹤、留言回覆，內建每日安全限制
- **數據分析**：互動率追蹤、粉絲成長、競品分析、每月 CSV 報告
- **Threads 工具**：官方 API 整合、排程、留言自動回覆

## 三步開始

```bash
git clone https://github.com/gino2013/MetaBoost.git
cd MetaBoost
pip install instagrapi instaloader python-dotenv
python examples/basic_analytics.py
```

## 安全使用限制

- 按讚：< 150 次/天
- 追蹤：< 50 次/天
- 留言：< 30 次/天
- 每個動作之間加入 4-10 秒隨機延遲

**重要提醒：** 自動化工具有被 IG 封號風險，務必先在測試帳號上驗證。

</details>

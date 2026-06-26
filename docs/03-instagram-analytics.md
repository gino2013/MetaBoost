# Instagram Analytics & Data Tools

Understand your audience, track performance, and analyze competitors — all without paying for expensive third-party dashboards.

---

## Tool Overview

| Tool | Type | Difficulty | Best For |
|------|------|-----------|----------|
| Instaloader | Data collection | Low | Downloading posts, follower lists, metadata |
| Osintgram | Account analysis | Low | Deep-dive competitor analysis |
| InstagramUnfollowers | Follower tracking | None | Finding who unfollowed you |

---

## Instaloader

**GitHub:** [instaloader/instaloader](https://github.com/instaloader/instaloader)

Download posts, stories, metadata, and follower data from any public Instagram account. Outputs structured data ready for analysis.

### Install

```bash
pip install instaloader
```

### Download an Account's Posts

```bash
# Download all posts from a public account
instaloader target_account

# Download only metadata (no images/videos)
instaloader --no-pictures --no-videos target_account

# Download with hashtag data
instaloader --hashtags target_account
```

### Use in Python

```python
import instaloader

L = instaloader.Instaloader()
L.login("your_username", "your_password")

profile = instaloader.Profile.from_username(L.context, "target_account")

print(f"Followers: {profile.followers}")
print(f"Following: {profile.followees}")
print(f"Posts: {profile.mediacount}")

# Iterate over all posts
for post in profile.get_posts():
    print(f"Date: {post.date}")
    print(f"Likes: {post.likes} | Comments: {post.comments}")
    print(f"Caption: {post.caption[:60]}")
    print("---")
```

### Analyze Your Own Account

```python
import instaloader
from datetime import datetime

L = instaloader.Instaloader()
L.login("your_username", "your_password")

profile = instaloader.Profile.from_username(L.context, "your_username")

# Calculate engagement rate per post
posts_data = []
for post in profile.get_posts():
    engagement = (post.likes + post.comments) / profile.followers * 100
    posts_data.append({
        "date": post.date,
        "likes": post.likes,
        "comments": post.comments,
        "engagement_rate": round(engagement, 2),
        "caption_preview": str(post.caption)[:50] if post.caption else ""
    })

# Sort by engagement
posts_data.sort(key=lambda x: x["engagement_rate"], reverse=True)

print("Top 5 posts by engagement rate:")
for p in posts_data[:5]:
    print(f"  {p['date'].strftime('%Y-%m-%d')} | {p['engagement_rate']}% | {p['caption_preview']}")
```

---

## Osintgram

**GitHub:** [Datalux/Osintgram](https://github.com/Datalux/Osintgram)

Interactive shell for deep Instagram account analysis. Great for competitor research.

### Install

```bash
git clone https://github.com/Datalux/Osintgram
cd Osintgram
pip install -r requirements.txt
```

### Configure

Create `config/credentials.ini`:
```ini
[Credentials]
username = your_username
password = your_password
```

### Use the Interactive Shell

```bash
python3 main.py target_account
```

Available commands inside the shell:

| Command | What it does |
|---------|-------------|
| `followers` | List all followers |
| `followings` | List all following |
| `fwersemail` | Extract followers' email addresses |
| `hashtags` | Most used hashtags by this account |
| `likes` | Total likes across all posts |
| `comments` | Most commented posts |
| `photos` | Download all photos |
| `stories` | Download current stories |
| `info` | Account info summary |
| `wcommented` | Users who commented most |

---

## InstagramUnfollowers

**GitHub:** [davidarroyo1234/InstagramUnfollowers](https://github.com/davidarroyo1234/InstagramUnfollowers)

No install required — runs directly in your browser console.

### How to Use

1. Open [instagram.com](https://www.instagram.com) and log in
2. Go to your profile → Following
3. Open DevTools: `F12` or `Cmd+Option+I`
4. Go to the **Console** tab
5. Paste the script from the [releases page](https://github.com/davidarroyo1234/InstagramUnfollowers/releases)
6. Press Enter — a UI pops up showing who doesn't follow you back

---

## Building a Simple Dashboard

Combine Instaloader data into a quick CSV report:

```python
import instaloader
import csv
from datetime import datetime

L = instaloader.Instaloader()
L.login("your_username", "your_password")
profile = instaloader.Profile.from_username(L.context, "your_username")

with open("analytics_report.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "Likes", "Comments", "Engagement%", "Caption"])

    for post in profile.get_posts():
        eng = round((post.likes + post.comments) / max(profile.followers, 1) * 100, 3)
        writer.writerow([
            post.date.strftime("%Y-%m-%d"),
            post.likes,
            post.comments,
            eng,
            str(post.caption)[:80] if post.caption else ""
        ])

print("Report saved to analytics_report.csv")
```

---

[← Automation](02-instagram-automation.md) | [Next: Scheduling →](04-social-scheduling.md)

---

<details>
<summary>中文說明</summary>

## Instagram 數據分析工具

**Instaloader**：下載任意公開帳號的貼文、follower 列表、metadata，適合競品分析與自身帳號績效追蹤。

**Osintgram**：互動式 shell，輸入帳號名稱即可取得深度分析資料，包含 email 列表、最常用 hashtag、最多互動的粉絲等。

**InstagramUnfollowers**：不需安裝，直接在瀏覽器 Console 貼上腳本，立即看出哪些人沒有回追你。

**建立簡單分析報告：**
使用 Instaloader 取得貼文數據後，可匯出 CSV 做進一步的互動率分析，找出哪類內容最受歡迎。

</details>

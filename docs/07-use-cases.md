# Use Cases & Recipes

Real-world scenarios with step-by-step instructions.

---

## Use Case 1: Hashtag Competitor Analysis

**Goal:** Find the best-performing content in your niche and understand what makes it work.

```python
import instaloader
from collections import Counter

L = instaloader.Instaloader()
L.login("your_username", "your_password")

hashtag = "shiba"
posts = L.get_hashtag_posts(hashtag)

data = []
for i, post in enumerate(posts):
    if i >= 50:  # Analyze top 50 posts
        break
    data.append({
        "likes": post.likes,
        "comments": post.comments,
        "owner": post.owner_username,
        "type": post.typename,       # GraphImage, GraphVideo, GraphSidecar
        "hashtags": post.caption_hashtags
    })

# Find most common content types
types = Counter(d["type"] for d in data)
print("Content type breakdown:", types)

# Find top accounts
top_accounts = Counter(d["owner"] for d in data).most_common(10)
print("Most active accounts:", top_accounts)

# Average engagement
avg_likes = sum(d["likes"] for d in data) / len(data)
print(f"Average likes for #{hashtag}: {avg_likes:.0f}")
```

---

## Use Case 2: Auto-Schedule Weekly Content

**Goal:** Prepare 7 days of posts in advance and auto-publish them.

```python
import json
import time
from instagrapi import Client
from datetime import datetime

# content_plan.json structure:
# [{"image": "monday.jpg", "caption": "Monday post #tag", "time": "2026-07-01T09:00:00"}]

with open("content_plan.json") as f:
    plan = json.load(f)

cl = Client()
cl.load_settings("session.json")
cl.login("your_username", "your_password")

for item in plan:
    scheduled = datetime.fromisoformat(item["time"])
    now = datetime.now()
    wait = (scheduled - now).total_seconds()

    if wait > 0:
        print(f"Waiting {wait:.0f}s until {item['time']}...")
        time.sleep(wait)

    cl.photo_upload(item["image"], caption=item["caption"])
    print(f"Posted: {item['caption'][:50]}")
```

---

## Use Case 3: Daily Engagement Bot

**Goal:** Automatically engage with content in your niche every morning.

```python
import os
import random
import time
from instagrapi import Client

cl = Client()
cl.load_settings("session.json")
cl.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))

TARGET_HASHTAGS = ["shiba", "柴犬", "dogs", "petlover"]
DAILY_LIKE_LIMIT = 80
DAILY_FOLLOW_LIMIT = 20

liked = 0
followed = 0

for tag in TARGET_HASHTAGS:
    if liked >= DAILY_LIKE_LIMIT:
        break

    medias = cl.hashtag_medias_recent(tag, amount=20)

    for media in medias:
        if liked >= DAILY_LIKE_LIMIT:
            break

        # Like the post
        cl.media_like(media.id)
        liked += 1

        # Occasionally follow the poster
        if followed < DAILY_FOLLOW_LIMIT and random.random() < 0.2:
            cl.user_follow(media.user.pk)
            followed += 1
            print(f"Followed: {media.user.username}")

        # Random delay to mimic human behavior
        time.sleep(random.uniform(3, 8))

print(f"Done. Liked: {liked}, Followed: {followed}")
```

---

## Use Case 4: Threads Reply Campaign

**Goal:** Monitor your Threads posts and auto-reply to comments within an hour.

```python
import os
import requests
import time

TOKEN = os.getenv("THREADS_ACCESS_TOKEN")
USER_ID = os.getenv("THREADS_USER_ID")

def get_recent_replies(post_id):
    r = requests.get(
        f"https://graph.threads.net/v1.0/{post_id}/replies",
        params={"access_token": TOKEN, "fields": "id,text,username,timestamp"}
    )
    return r.json().get("data", [])

def reply_to_comment(post_id, text):
    container = requests.post(
        f"https://graph.threads.net/v1.0/{USER_ID}/threads",
        params={
            "media_type": "TEXT",
            "text": text,
            "reply_to_id": post_id,
            "access_token": TOKEN
        }
    ).json()

    requests.post(
        f"https://graph.threads.net/v1.0/{USER_ID}/threads_publish",
        params={"creation_id": container["id"], "access_token": TOKEN}
    )

# Monitor and reply loop
POST_ID = "your_post_id"
replied_to = set()

while True:
    replies = get_recent_replies(POST_ID)
    for reply in replies:
        if reply["id"] not in replied_to:
            reply_to_comment(reply["id"], "Thanks for engaging! 🐕")
            replied_to.add(reply["id"])
            print(f"Replied to {reply['username']}")
    time.sleep(300)  # Check every 5 minutes
```

---

## Use Case 5: Monthly Performance Report

**Goal:** Generate a monthly PDF/CSV report of your account's growth and engagement.

```python
import instaloader
import csv
from datetime import datetime, timedelta

L = instaloader.Instaloader()
L.login("your_username", "your_password")

profile = instaloader.Profile.from_username(L.context, "your_username")
one_month_ago = datetime.now() - timedelta(days=30)

report_rows = []

for post in profile.get_posts():
    if post.date.replace(tzinfo=None) < one_month_ago:
        break  # Stop when we hit posts older than 30 days

    eng_rate = round((post.likes + post.comments) / max(profile.followers, 1) * 100, 3)
    report_rows.append({
        "date": post.date.strftime("%Y-%m-%d"),
        "type": post.typename,
        "likes": post.likes,
        "comments": post.comments,
        "engagement_rate": eng_rate,
        "caption": str(post.caption)[:80] if post.caption else ""
    })

filename = f"report_{datetime.now().strftime('%Y%m')}.csv"
with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=report_rows[0].keys())
    writer.writeheader()
    writer.writerows(report_rows)

avg_eng = sum(r["engagement_rate"] for r in report_rows) / len(report_rows)
print(f"Monthly report saved: {filename}")
print(f"Posts analyzed: {len(report_rows)}")
print(f"Average engagement rate: {avg_eng:.2f}%")
```

---

[← Integration Guide](06-integration-guide.md) | [← Back to Home](../README.md)

---

<details>
<summary>中文說明</summary>

## 實戰使用案例

1. **Hashtag 競品分析**：抓取特定 hashtag 的前 50 篇貼文，分析內容類型分佈、平均讚數、最活躍帳號，找出你的利基市場規律。

2. **週內容自動排程**：預先準備 7 天的貼文計劃（JSON 格式），腳本自動在設定時間發布。

3. **每日互動機器人**：每天早上自動對目標 hashtag 的貼文按讚和追蹤，模擬人類行為（隨機延遲、每日上限）。

4. **Threads 回覆活動**：監控你的 Threads 貼文留言，在一小時內自動回覆，提升互動率。

5. **每月績效報告**：自動抓取過去 30 天的貼文數據，計算互動率並匯出 CSV，方便長期追蹤成效。

</details>

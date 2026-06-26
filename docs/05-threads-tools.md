# Threads Tools

Threads-specific tools for scheduling, comment management, and AI-assisted engagement.

---

## Overview

Threads (by Meta) shares infrastructure with Instagram but has its own API and growth dynamics. The tools here are optimized specifically for Threads.

| Tool | Function | Difficulty |
|------|----------|-----------|
| schedul-pm | Post scheduling | Low |
| comment_copilot | AI comment management | Medium |
| postmypost SDK | Scheduling via API | Medium |
| Threads API (official) | Direct API access | High |

---

## schedul-pm

**GitHub:** [42eleven/schedul-pm](https://github.com/42eleven/schedul-pm)

Product and feature management for Threads-exclusive content publishing. Purpose-built for Threads creators.

**Key features:**
- Threads-native scheduling interface
- Content calendar for Threads posts
- Performance tracking

---

## comment_copilot

**GitHub:** [mustcanbedo/comment_copilot](https://github.com/mustcanbedo/comment_copilot)

AI-powered comment assistant. Automatically reads comments, identifies high-intent users, and generates reply drafts — reducing the workload of community management.

### Install

```bash
git clone https://github.com/mustcanbedo/comment_copilot
cd comment_copilot
pip install -r requirements.txt
```

### Configure

```bash
cp config.example.yml config.yml
# Edit config.yml with your API keys and preferences
```

### Usage

```python
from comment_copilot import CommentCopilot

bot = CommentCopilot(config="config.yml")

# Scan recent comments and generate replies
replies = bot.process_comments(
    post_id="YOUR_POST_ID",
    mode="high_intent",    # Focus on potential customers/followers
    tone="friendly"
)

for comment, reply in replies:
    print(f"Comment: {comment}")
    print(f"Suggested reply: {reply}")
    print("---")
```

---

## Posting to Threads via Official API

Meta provides an official Threads API. Use this for production-grade integrations.

### Setup

1. Create a Meta Developer App at [developers.facebook.com](https://developers.facebook.com)
2. Add the Threads product to your app
3. Get `THREADS_ACCESS_TOKEN` and `THREADS_USER_ID`

### Post a Thread

```python
import requests
import os

USER_ID = os.getenv("THREADS_USER_ID")
TOKEN = os.getenv("THREADS_ACCESS_TOKEN")

def create_thread(text: str):
    # Step 1: Create media container
    container = requests.post(
        f"https://graph.threads.net/v1.0/{USER_ID}/threads",
        params={
            "media_type": "TEXT",
            "text": text,
            "access_token": TOKEN
        }
    ).json()

    # Step 2: Publish
    result = requests.post(
        f"https://graph.threads.net/v1.0/{USER_ID}/threads_publish",
        params={
            "creation_id": container["id"],
            "access_token": TOKEN
        }
    ).json()

    return result

create_thread("Hello from MetaBoost! 🐕")
```

### Post with an Image

```python
def create_thread_with_image(text: str, image_url: str):
    # Create image container
    container = requests.post(
        f"https://graph.threads.net/v1.0/{USER_ID}/threads",
        params={
            "media_type": "IMAGE",
            "image_url": image_url,
            "text": text,
            "access_token": TOKEN
        }
    ).json()

    # Publish
    return requests.post(
        f"https://graph.threads.net/v1.0/{USER_ID}/threads_publish",
        params={
            "creation_id": container["id"],
            "access_token": TOKEN
        }
    ).json()
```

### Fetch Insights

```python
def get_thread_insights(media_id: str):
    metrics = ["views", "likes", "replies", "reposts", "quotes"]
    result = requests.get(
        f"https://graph.threads.net/v1.0/{media_id}/insights",
        params={
            "metric": ",".join(metrics),
            "access_token": TOKEN
        }
    ).json()
    return result["data"]
```

---

## Threads Growth Tips

| Strategy | Description |
|----------|------------|
| Reply chains | Reply to popular posts in your niche to get discovered |
| Early hours | Post when your region wakes up — first 30 min = most reach |
| Cross-post IG↔Threads | Use the same content on both for maximum coverage |
| Quote threads | Quote popular posts with your own take — drives profile visits |

---

[← Scheduling](04-social-scheduling.md) | [Next: Integration Guide →](06-integration-guide.md)

---

<details>
<summary>中文說明</summary>

## Threads 專屬工具

**schedul-pm**：專為 Threads 設計的內容發布與排程工具。

**comment_copilot**：AI 評論助手，自動掃描留言、識別高意向用戶（潛在客戶或高互動粉絲）並生成回覆草稿，大幅減輕社群管理的工作量。

**官方 Threads API**：Meta 提供官方 API，可直接發文、取得互動數據。需要先建立 Meta Developer App，適合想做更完整整合的開發者。

**Threads 成長技巧：**
- 在你的利基領域熱門貼文下留言，增加曝光
- 在你的受眾剛醒來的時間發文（發文後前 30 分鐘觸及率最高）
- IG 和 Threads 同步發相同內容，擴大覆蓋範圍
- 引用（Quote）熱門貼文並加入自己的看法，帶動個人頁面訪問

</details>

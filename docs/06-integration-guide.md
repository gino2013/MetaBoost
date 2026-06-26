# Integration Guide

How to combine multiple tools into a coherent workflow.

---

## Recommended Stacks by Goal

### "I want to grow from 0 to 10k followers"

```
instagrapi          → auto-engage with relevant hashtags
Instaloader         → analyze what content performs best in your niche
BrightBean Studio   → schedule consistent posting
comment_copilot     → manage replies efficiently
```

### "I manage multiple brand accounts"

```
BrightBean Studio   → unified scheduling dashboard (self-hosted)
postmypost SDK      → programmatic posting for high-volume needs
Instaloader         → monthly analytics reports per account
```

### "I want full automation with minimal time investment"

```
instagrapi          → scheduled auto-posting + auto-engagement
DemandBird          → AI content repurposing
comment_copilot     → automated reply drafts
```

---

## Full Workflow Example: Solo Creator

Here's a complete weekly automation pipeline:

```
Monday
  └── Instaloader: pull last week's post performance data
  └── Python script: generate engagement report
  └── Review top-performing content types

Tuesday–Friday
  └── BrightBean Studio: posts go live on schedule
  └── instagrapi: auto-like hashtag posts (morning)
  └── comment_copilot: draft replies to comments (evening)

Sunday
  └── Plan next week's content
  └── Schedule posts in BrightBean Studio
```

---

## Setting Up a Unified `.env`

All tools can share a single environment file:

```bash
# .env
IG_USERNAME=your_instagram_username
IG_PASSWORD=your_instagram_password

# Threads (Official API)
THREADS_USER_ID=your_threads_user_id
THREADS_ACCESS_TOKEN=your_threads_token

# postmypost (if using)
POSTMYPOST_API_KEY=your_api_key
```

---

## Master Controller Script

A simple orchestrator that runs your daily tasks:

```python
#!/usr/bin/env python3
"""
MetaBoost Daily Runner
Run: python run_daily.py
"""

import os
import logging
from instagrapi import Client
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
log = logging.getLogger("MetaBoost")

def get_client():
    cl = Client()
    try:
        cl.load_settings("session.json")
        cl.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))
    except Exception:
        cl.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))
        cl.dump_settings("session.json")
    return cl

def engage_hashtags(cl, tags: list, amount: int = 10):
    for tag in tags:
        medias = cl.hashtag_medias_top(tag, amount=amount)
        for m in medias:
            cl.media_like(m.id)
            log.info(f"Liked post {m.id} under #{tag}")

def print_daily_stats(cl, username: str):
    user_id = cl.user_id_from_username(username)
    info = cl.user_info(user_id)
    log.info(f"Followers: {info.follower_count} | Following: {info.following_count}")

if __name__ == "__main__":
    cl = get_client()
    username = os.getenv("IG_USERNAME")

    log.info("=== MetaBoost Daily Run ===")
    print_daily_stats(cl, username)
    engage_hashtags(cl, tags=["shiba", "dogs", "pets"], amount=5)
    log.info("=== Done ===")
```

---

## Cron Schedule (Optional Automation)

Add to your crontab to run daily:

```bash
# Edit crontab
crontab -e

# Run every day at 9 AM
0 9 * * * /path/to/metaboost-env/bin/python /path/to/MetaBoost/run_daily.py >> /tmp/metaboost.log 2>&1
```

---

[← Threads Tools](05-threads-tools.md) | [Next: Use Cases →](07-use-cases.md)

---

<details>
<summary>中文說明</summary>

## 整合使用指南

**根據目標選擇工具組合：**

- **從零開始衝粉絲**：instagrapi（自動互動）+ Instaloader（分析競品）+ BrightBean Studio（排程）+ comment_copilot（回覆管理）

- **管理多個品牌帳號**：BrightBean Studio（統一排程）+ postmypost SDK（程式化大量發布）+ Instaloader（每月報告）

- **最小時間投入、最大自動化**：instagrapi（自動發文+互動）+ DemandBird（AI 內容再利用）+ comment_copilot（自動回覆草稿）

**統一設定檔（.env）：**
所有工具共用一個 `.env` 檔案，集中管理帳號密碼和 API 金鑰，不用分散在各個設定檔案。

**Master 控制腳本：**
用一個主腳本統一管理每日任務，加入 cron 排程後就能完全自動化運行。

</details>

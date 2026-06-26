# Getting Started

Get the right tool running in under 10 minutes.

---

## Which Tool Do I Need?

```
I want to...
│
├── Schedule posts automatically
│   └── → Social Media Scheduling (docs/04)
│
├── Analyze followers and competitors
│   └── → Analytics Tools (docs/03)
│
├── Auto-like, comment, follow
│   └── → Automation Tools (docs/02)  ⚠️ ban risk
│
├── Grow specifically on Threads
│   └── → Threads Tools (docs/05)
│
└── Do multiple things
    └── → Integration Guide (docs/06)
```

---

## Requirements

| Runtime | Version | Install |
|---------|---------|---------|
| Python | 3.8+ | [python.org](https://www.python.org/downloads/) |
| Node.js | 16+ | [nodejs.org](https://nodejs.org/) |
| Git | any | [git-scm.com](https://git-scm.com/) |

---

## Quick Install

### Python tools (instagrapi, instaloader, InstaPy)

```bash
# Create a virtual environment (strongly recommended)
python -m venv metaboost-env
source metaboost-env/bin/activate  # Windows: metaboost-env\Scripts\activate

# Install what you need
pip install instagrapi       # Latest IG Private API
pip install instaloader      # IG data downloader
pip install instapy          # IG automation
```

### Node.js tools (postmypost SDK)

```bash
npm install @postmypost/node-rest-sdk
```

### Browser tools (InstagramUnfollowers)

No install needed. Open Instagram in Chrome → DevTools → Console → paste the script.

---

## Your First Script

```python
from instagrapi import Client
from dotenv import load_dotenv
import os

load_dotenv()

cl = Client()
# Save session to avoid repeated logins
try:
    cl.load_settings("session.json")
    cl.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))
except:
    cl.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))
    cl.dump_settings("session.json")

# Fetch your last 10 posts' performance
user_id = cl.user_id_from_username(os.getenv("IG_USERNAME"))
medias = cl.user_medias(user_id, amount=10)

for media in medias:
    print(f"Post: {str(media.caption_text)[:40]}...")
    print(f"  Likes: {media.like_count} | Comments: {media.comment_count}")
```

More in the [examples/](../examples/) folder.

---

## Security Best Practices

1. **Never hardcode credentials** — use `.env` files
2. **Test on a secondary account** first
3. **Throttle your actions** — heavy automation triggers IG detection
4. **Reuse session files** — avoid repeated logins that trigger 2FA

```bash
# Create .env file
echo "IG_USERNAME=your_username" >> .env
echo "IG_PASSWORD=your_password" >> .env

# Keep it out of git
echo ".env" >> .gitignore
echo "session.json" >> .gitignore
```

---

## Next Steps

- [Instagram Automation Tools](02-instagram-automation.md)
- [Analytics Tools](03-instagram-analytics.md)
- [Real-world Use Cases](07-use-cases.md)

---

<details>
<summary>中文說明</summary>

## 快速上手

根據你的目標選擇對應路徑，10 分鐘內讓工具跑起來。

**我想要…**
- 排程發文 → 看 [社群排程管理](04-social-scheduling.md)
- 分析粉絲和競品 → 看 [數據分析工具](03-instagram-analytics.md)
- 自動按讚、留言、追蹤 → 看 [自動化互動工具](02-instagram-automation.md)（⚠️ 注意封號風險）
- 專門經營 Threads → 看 [Threads 工具](05-threads-tools.md)

**安全建議：**
1. 帳密放在 `.env` 檔案，不要寫死在程式碼
2. 先用小帳測試，確認沒問題再套用主帳
3. 控制操作頻率，避免被 IG 偵測
4. 保留 session 檔案，減少重複登入

</details>

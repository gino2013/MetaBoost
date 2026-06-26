# Instagram Automation Tools

> Automation saves time, but use it carefully. Excessive automation can get your account rate-limited or banned.

---

## Tool Comparison

| Tool | Difficulty | Risk | Best For |
|------|-----------|------|----------|
| InstaPy | Medium | Medium-High | Full feature set, complex workflows |
| instagrapi | Low | Medium | Developers, API integrations, 2026 maintained |
| igbot | Low | Medium | Beginners, quick scripts |
| instagram-private-api | High | Medium | Node.js ecosystem |

---

## instagrapi (Recommended)

**GitHub:** [subzeroid/instagrapi](https://github.com/subzeroid/instagrapi)

The fastest and most actively maintained Instagram Private API wrapper for Python (2026). Best choice for most use cases.

### Install

```bash
pip install instagrapi python-dotenv
```

### Login & Session Management

```python
from instagrapi import Client
import os

cl = Client()

# Always reuse session to avoid triggering 2FA
try:
    cl.load_settings("session.json")
    cl.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))
except:
    cl.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))
    cl.dump_settings("session.json")
```

### Post Content

```python
# Upload a photo
media = cl.photo_upload(
    "photo.jpg",
    caption="My new post! #shiba #dog",
)

# Upload a Reel
cl.clip_upload(
    "video.mp4",
    caption="My first Reel! #reels",
    thumbnail="thumb.jpg"
)

# Upload a Story
cl.photo_upload_to_story("story.jpg")
```

### Auto-Engage

```python
# Like top posts under a hashtag
medias = cl.hashtag_medias_top("shiba", amount=10)
for m in medias:
    cl.media_like(m.id)

# Follow users who post with a specific hashtag
medias = cl.hashtag_medias_recent("dogs", amount=20)
for m in medias:
    cl.user_follow(m.user.pk)
```

---

## InstaPy

**GitHub:** [InstaPy/InstaPy](https://github.com/InstaPy/InstaPy)

Most mature and feature-complete IG automation framework. More complex setup but extremely configurable.

### Install

```bash
pip install instapy
```

### Basic Usage

```python
from instapy import InstaPy

session = InstaPy(username="your_account", password="your_password")
session.login()

# Like by hashtag
session.like_by_tags(["shiba", "dogs"], amount=10)

# Follow followers of a competitor
session.follow_user_followers(["competitor_account"], amount=20, randomize=True)

# Auto-comment
session.set_comments(["Great content!", "Love this!", "So cute!"])
session.like_by_tags(["shiba"], amount=5)

session.end()
```

### Safety Settings

```python
# Set daily action limits
session.set_user_interact(amount=3, randomize=True, percentage=50)
session.set_likes_count(3, 10)   # 3-10 likes per account
session.set_sleep_reduce(50)      # Random delays between actions

# Filter out suspicious accounts
session.set_relationship_bounds(
    enabled=True,
    potency_ratio=-35,
    max_followers=5000,
    min_followers=50
)
```

---

## instagram-private-api (Node.js)

**GitHub:** [dilame/instagram-private-api](https://github.com/dilame/instagram-private-api)

TypeScript SDK for the Node.js ecosystem.

### Install

```bash
npm install instagram-private-api
```

### Usage

```typescript
import { IgApiClient } from 'instagram-private-api';

const ig = new IgApiClient();
ig.state.generateDevice(process.env.IG_USERNAME!);

async function main() {
  await ig.account.login(process.env.IG_USERNAME!, process.env.IG_PASSWORD!);

  // Like a post
  await ig.media.like({
    mediaId: 'MEDIA_ID',
    moduleInfo: { module_name: 'profile' },
    d: 1,
  });
}

main();
```

---

## Daily Action Limits (Safe Ranges)

| Action | Safe Limit | Risky |
|--------|-----------|-------|
| Likes | < 150 / day | > 300 |
| Follows | < 50 / day | > 100 |
| Comments | < 30 / day | > 60 |
| DMs | < 20 / day | > 40 |

Always add random delays (2–10s) between actions and avoid running 24/7.

---

[← Back to Home](../README.md) | [Next: Analytics →](03-instagram-analytics.md)

---

<details>
<summary>中文說明</summary>

## Instagram 自動化工具

**工具推薦：**
- **instagrapi**（首選）：2026 年仍持續維護，速度最快，新手友好
- **InstaPy**：功能最完整，但設定較複雜
- **instagram-private-api**：Node.js 生態系首選

**每日安全限制建議：**
- 按讚：< 150 次/天
- 追蹤：< 50 次/天
- 留言：< 30 次/天
- 私訊：< 20 次/天

動作之間務必加入隨機延遲（2-10 秒），避免 24 小時持續運行。

**重要提醒：** 所有自動化工具均有被 IG 偵測封號的風險，強烈建議先在測試帳號上驗證。

</details>

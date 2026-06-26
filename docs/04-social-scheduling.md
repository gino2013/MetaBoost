# Social Media Scheduling & Management

Automate your content calendar across Instagram, Threads, and 10+ other platforms — without paying for Buffer or Hootsuite.

---

## Tool Comparison

| Tool | Self-host | Platforms | AI Features | Best For |
|------|-----------|-----------|-------------|----------|
| BrightBean Studio | Yes | 10+ | No | Teams, agencies wanting full control |
| DemandBird | Partial | Multiple | Yes | Creators wanting AI content pipeline |
| trypost | Yes | Multiple | No | Developers, open-source purists |
| postmypost SDK | API only | IG, FB, X, TikTok, Threads... | No | Building custom scheduling tools |

---

## BrightBean Studio (Recommended for Self-Hosting)

**GitHub:** [brightbeanxyz/brightbean-studio](https://github.com/brightbeanxyz/brightbean-studio)

Open-source, self-hostable social media management platform. Free alternative to Buffer, Sendible, and SocialPilot.

**Supported platforms:** Instagram, Facebook, Twitter/X, LinkedIn, TikTok, Threads, YouTube, Pinterest, and more.

### Quick Start with Docker

```bash
git clone https://github.com/brightbeanxyz/brightbean-studio
cd brightbean-studio
cp .env.example .env
# Edit .env with your database and API credentials
docker-compose up -d
```

Then open `http://localhost:3000` and connect your social accounts.

### Features

- Visual content calendar
- Bulk upload and scheduling
- Multi-account management
- Basic analytics dashboard
- Team collaboration

---

## DemandBird

**GitHub:** [DemandBird/demandbird](https://github.com/DemandBird/demandbird)

AI-native social media management with a full content pipeline: create → schedule → publish → analyze → repurpose.

**Highlights:**
- AI-assisted caption and content generation
- Content repurposing (turn one post into 5 formats)
- Analytics with actionable insights
- MCP and API support for Claude/agent integration

---

## trypost

**GitHub:** [trypostit/trypost](https://github.com/trypostit/trypost)

Minimal, open-source social media scheduling. Clean UI, easy to self-host.

```bash
git clone https://github.com/trypostit/trypost
cd trypost
npm install
npm run dev
```

---

## postmypost Node.js SDK

**GitHub:** [postmypost/node-rest-sdk](https://github.com/postmypost/node-rest-sdk)

Use this if you want to build a custom scheduling tool or integrate posting into your own app.

**Supported platforms:** Instagram, Facebook, LinkedIn, X/Twitter, Reddit, YouTube, TikTok, Telegram, Threads.

### Install

```bash
npm install @postmypost/node-rest-sdk
```

### Usage

```javascript
const { PostmypostClient } = require('@postmypost/node-rest-sdk');

const client = new PostmypostClient({ apiKey: process.env.POSTMYPOST_API_KEY });

// Schedule a post to Instagram and Threads simultaneously
await client.posts.create({
  accounts: ['instagram_account_id', 'threads_account_id'],
  content: {
    text: "New post! #content #creator",
    media: [{ url: "https://your-image-url.jpg" }]
  },
  scheduledAt: new Date('2026-07-01T10:00:00Z')
});
```

---

## Scheduling Best Practices

### Optimal Posting Times (General Benchmarks)

| Platform | Best Days | Best Times |
|----------|-----------|------------|
| Instagram | Tue, Wed, Fri | 9am–11am, 7pm–9pm |
| Threads | Mon–Thu | 8am–10am, 12pm–2pm |

> Tip: Use your own analytics (see [Analytics doc](03-instagram-analytics.md)) to find your audience's actual active hours.

### Content Cadence

```
Recommended weekly schedule:
- 3–5 Feed posts (photos/carousels/Reels)
- 7–14 Stories
- 3–7 Threads posts
- 1–2 longer-form Reels per week
```

---

[← Analytics](03-instagram-analytics.md) | [Next: Threads Tools →](05-threads-tools.md)

---

<details>
<summary>中文說明</summary>

## 社群排程管理工具

**BrightBean Studio**（推薦）：可自架，支援 10+ 平台，Buffer/SocialPilot 的免費替代品。用 Docker 一鍵啟動，有可視化內容日曆和多帳號管理。

**DemandBird**：AI 原生，支援內容生成、分析、再利用，適合想節省內容製作時間的創作者。

**postmypost SDK**：如果你想自己開發排程工具，這個 Node.js SDK 支援 IG、Threads、TikTok 等多平台同時發布。

**最佳發文時間參考：**
- Instagram：週二、三、五，早上 9-11 點或晚上 7-9 點
- Threads：週一到四，早上 8-10 點或中午 12-2 點

建議用 Instaloader 分析自己帳號的真實數據，找到你的受眾最活躍的時段。

</details>

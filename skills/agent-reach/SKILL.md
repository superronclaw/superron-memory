# Agent Reach Skill

## 這是什麼？
Agent Reach 是一個多平台互聯網訪問工具，讓 AI Agent 可以直接訪問：
- Twitter/X、YouTube、Bilibili、Reddit
- 網頁內容（通過 Jina Reader）
- RSS/Atom 訂閱源
- GitHub

## 可用渠道（4/14）
| 渠道 | 狀態 | 工具 |
|------|------|------|
| GitHub | ⚠️ gh CLI 已安裝但未認證 | `gh` |
| YouTube | ✅ 可用 | `yt-dlp` |
| Bilibili | ✅ 可用 | `yt-dlp` |
| RSS/Atom | ✅ 可用 | `feedparser` |
| 任意網頁 | ✅ 可用 | `curl https://r.jina.ai/URL` |

## 使用方式

### YouTube/Bilibili
```bash
yt-dlp --dump-json "URL"
```

### 網頁內容
```bash
curl -s "https://r.jina.ai/URL"
```

### RSS 訂閱
```bash
python3 -c "import feedparser; print(feedparser.parse('URL'))"
```

## 待解鎖渠道
- Twitter/X（需要更新 xreach）
- 微博（需要 mcp-server-weibo）
- 小紅書（需要 Docker）
- 小宇宙播客（需要 ffmpeg + Groq API Key）
- 抖音（需要 douyin-mcp-server）

## 自動監控
- **每日 08:00** 自動運行 `agent-reach watch` 檢查狀態
- 有問題時會通知用戶


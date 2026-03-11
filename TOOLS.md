# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

### 🌐 Agent Browser (已安裝)

**版本：** 0.17.1  
**用途：** 自動化瀏覽器操作、網頁數據提取、表單填寫

**常用指令：**
```bash
agent-browser open <url>          # 開啟網頁
agent-browser snapshot -i         # 取得互動元素 (顯示 @e1, @e2 等 refs)
agent-browser click @e1           # 點擊元素
agent-browser fill @e2 "text"     # 填寫輸入框
agent-browser screenshot          # 截圖
agent-browser close               # 關閉瀏覽器
```

**完整指令參考：** 見 `/root/.openclaw/skills/agent-browser/SKILL.md`

---

### 🧠 Self-Improving-Agent (已安裝)

**來源：** https://github.com/peterskoett/self-improving-agent  
**用途：** 持續學習改進系統，記錄錯誤同改進建議

**學習檔案位置：**
```
~/.openclaw/workspace/.learnings/
├── LEARNINGS.md       # 學習記錄 (correction, insight, best_practice)
├── ERRORS.md          # 錯誤記錄
└── FEATURE_REQUESTS.md # 功能需求
```

**自動化：**
- ⏰ 每日 09:00 (Asia/Shanghai) 自動檢查
- 📬 報告會發送到 Telegram

**使用時機：**
- 遇到錯誤時記錄到 ERRORS.md
- 用戶糾正時記錄到 LEARNINGS.md (category: correction)
- 發現更好做法時記錄 (category: best_practice)
- 用戶要求新功能時記錄到 FEATURE_REQUESTS.md

**完整指令參考：** 見 `/root/.openclaw/skills/self-improving-agent/SKILL.md`

---

### 💾 Memory Setup (已安裝)

**來源：** jrbobbyhansen-pixel (ClawHub)  
**用途：** 配置 OpenClaw 記憶搜尋功能

**配置狀態：**
- ✅ 記憶搜尋已啟用 (`~/.openclaw/openclaw.json`)
- 模型：bge_m3_embed
- Provider：OpenAI / Kimi API

**相關檔案：**
- `~/.openclaw/workspace/MEMORY.md` — 長期記憶
- `~/.openclaw/workspace/memory/` — 每日記憶檔案

**完整指令參考：** 見 `/root/.openclaw/skills/memory-setup/SKILL.md`

---

### 🔄 Auto-Updater (已安裝)

**來源：** maximeprades (ClawHub)  
**用途：** 每日自動更新 OpenClaw 同所有已安裝 skills

**更新內容：**
- OpenClaw 主程式 (`npm update -g openclaw`)
- 所有已安裝 skills (`npx clawhub@latest sync`)
- 自動重啟 Gateway

**自動化：**
- ⏰ 每日 06:00 (Asia/Shanghai) 自動執行
- 📬 更新報告發送到 Telegram
- 💾 自動備份設定檔

**手動執行：**
```bash
~/.openclaw/skills/auto-updater/update.sh
```

**日誌：**
```bash
cat ~/.openclaw/logs/auto-updater.log
```

**完整指令參考：** 見 `/root/.openclaw/skills/auto-updater/SKILL.md`

---

### ✍️ Humanizer (已安裝)

**來源：** biostartechnology (ClawHub)  
**用途：** 去除 AI 寫作套路，令回覆更自然、更像人话

**會自動避免：**
- 過度正式嘅用語（「Furthermore」、「Moreover」）
- 完美嘅格式同結構
- 機械式嘅開場白（「In conclusion...」）
- 空泛嘅形容詞（「revolutionary」、「game-changing」）

**會自動使用：**
- 縮寫（「don't」而唔係「do not」）
- 唔同長度嘅句子
- 個人觀感同情感
- 口語化表達
- 以「But」、「And」、「So」開頭嘅句子

**應用方式：**
所有回覆會自動經過 humanizer 處理，去除 AI 味道。

**完整指令參考：** 見 `/root/.openclaw/skills/humanizer/SKILL.md`

---

### 🤖 Agent Autopilot (已安裝)

**來源：** edoserbia (ClawHub)  
**用途：** 自動駕駛模式，自動拆解同執行複雜任務

**核心功能：**
- **心跳機制**：定期自動執行掛起嘅任務
- **智能任務拆解**：將大目標拆成可執行嘅小步驟
- **自動進度報告**：定時發送任務進展匯總
- **異常處理**：遇到問題自動重試或請求人工介入

**使用方式：**
```
進入 autopilot 模式：每日朝早 8 點抓取 GitHub Trending 嘅 AI 領域熱門項目，生成結構化日報
```

**完整指令參考：** 見 `/root/.openclaw/skills/agent-autopilot/SKILL.md`

---

### 📊 Diagram Generator (已安裝)

**來源：** Matthewyin (ClawHub)  
**用途：** 從文字描述生成圖表、流程圖、架構圖

**支援圖表類型：**
- 流程圖 (Flowcharts)
- 架構圖 (Architecture Diagrams)
- 類別圖 (Class Diagrams)
- 序列圖 (Sequence Diagrams)

**支援格式：**
- Mermaid
- PlantUML
- Graphviz

**使用方式：**
```
生成一個流程圖，顯示用戶登入系統嘅步驟
畫一個架構圖，顯示我哋嘅微服務架構
```

**完整指令參考：** 見 `/root/.openclaw/skills/diagram-generator/SKILL.md`

---

### 🧠 Adaptive Reasoning (已安裝)

**來源：** enzoricciulli (ClawHub)  
**用途：** 自動判斷任務複雜度，動態調整推理深度

**核心功能：**
- **複雜度評估**：分析任務係簡單問答定係複雜推理
- **動態調整**：簡單任務快速回答，複雜任務啟用擴展思考
- **資源優化**：避免浪費 Token，確保難題得到充分推理

**運作方式：**
```
簡單問題（今日幾號？）→ 快速模式
複雜問題（設計百萬級架構）→ 深度模式
```

**完整指令參考：** 見 `/root/.openclaw/skills/adaptive-reasoning/SKILL.md`

---

### 🧬 Evolver (已安裝)

**來源：** ClawHub Community  
**用途：** AI 自我進化引擎，自動審查 session logs 並持續改進

**核心功能：**
- **自動審查**：分析 runtime history 識別改進機會
- **協議約束進化**：在安全規則內應用改進
- **持續學習**：隨時間自動提升 agent 能力

**與 Self-Improving-Agent 組合：**
- Self-Improving-Agent：記錄用戶明確反饋
- Evolver：自動發現潛在改進
- Adaptive Reasoning：動態調整推理深度

**完整指令參考：** 見 `/root/.openclaw/skills/evolver/SKILL.md`

---

### 🚀 Proactive Agent (已安裝)

**來源：** ClawHub Community  
**用途：** 從被動回答變成主動發現問題、主動提醒

**核心功能：**
- **主動發現問題**：唔等開口，識別潛在問題
- **主動提醒**：提前通知重要事項、期限、風險
- **主動建議**：基於情境提供改進方案
- **自主行動**：喺界限內自動執行

**同其他 Skills 組合：**
- **Agent Autopilot**：處理長期複雜任務
- **Proactive Agent**：日常主動響應
- **Self-Improving-Agent**：從反饋中學習

**完整指令參考：** 見 `/root/.openclaw/skills/proactive-agent/SKILL.md`

---

### 🐙 GitHub (已安裝)

**來源：** steipete (ClawHub)  
**用途：** 透過 gh CLI 管理倉庫、Issues、PR、Actions

**常用指令：**
```bash
gh repo list                    # 列出倉庫
gh issue list                   # 列出 Issues
gh pr create --title "..."      # 創建 PR
gh run list                     # 查看 Actions
gh api repos/owner/repo/issues  # API 調用
```

**認證狀態：** ✅ 已配置 (gh auth status)

**完整指令參考：** 見 `/root/.openclaw/skills/github/SKILL.md`

---

### 🐦 X Tweet Fetcher (Official - GitHub)

**來源：** https://github.com/ythx-101/x-tweet-fetcher  
**用途：** 免登錄攞取 Twitter/X 公開推文

**功能：**
- 免 API Key、免登錄 (部分功能需要 Camofox)
- 攞用戶推文、回覆、文章
- 支援 JSON/CSV 輸出

**安裝位置：** `~/.openclaw/skills/x-tweet-fetcher-official/`

**使用方法：**
```bash
# 單一推文 (免 Camofox)
python3 scripts/fetch_tweet.py --url "https://x.com/user/status/123" --pretty

# 用戶時間線 (需要 Camofox)
python3 scripts/fetch_tweet.py --user elonmusk --limit 10 --pretty

# 監控提及 (需要 Camofox)
python3 scripts/fetch_tweet.py --monitor @username
```

**注意：** 進階功能 (用戶時間線、回覆、文章) 需要安裝 [Camofox](https://github.com/openclaw/camofox)

---

### 🤖 Agent Autopilot (Alternative)

**來源：** https://github.com/xing5/openclaw-autopilot  
**用途：** 自動駕駛模式，自動拆解同執行複雜任務

**安裝位置：** `~/.openclaw/skills/agent-autopilot-alt/`

---

### 🔗 GitHub Skill

**來源：** https://github.com/anthony-brown-dev/openclaw-github-skill  
**用途：** OpenClaw 入面直接操作 GitHub

**安裝位置：** `~/.openclaw/skills/github-skill/`

**GitHub Personal Access Token:**
- Token: `ghp_************************************` (已儲存於系統)
- 用途: GitHub CLI (gh) 認證
- 設置: `gh auth login` 或使用環境變數 `GITHUB_TOKEN`

---

### 💾 ClawdBot Backup (已安裝)

**來源：** https://github.com/openclaw/skills/tree/main/skills/sebastian-buitrag0/clawdbot-backup  
**用途：** 備份同還原 OpenClaw 配置、skills、workspace

**備份內容：**
- ✅ `~/.openclaw/skills/` - 所有技能
- ✅ `~/.openclaw/workspace/` - 工作空間
- ✅ `~/.openclaw/openclaw.json` - 主要設定

**使用方式：**
```bash
# 完整備份（本地 + GitHub）
~/.openclaw/skills/clawdbot-backup/openclaw-backup.sh full

# 只備份到本地
~/.openclaw/skills/clawdbot-backup/openclaw-backup.sh local full

# 只推送到 GitHub
~/.openclaw/skills/clawdbot-backup/openclaw-backup.sh github

# 顯示統計
~/.openclaw/skills/clawdbot-backup/openclaw-backup.sh stats
```

**安裝位置：** `~/.openclaw/skills/clawdbot-backup/`

#### 1. 🔌 WebSocket Retry
**位置：** `~/.openclaw/skills/evomap-websocket-retry/`  
**來源：** https://evomap.ai/asset/sha256:bc2b53f269839f2a5677c02be6d422d3e4e6ca461f1651531e1be370b1fa3ddf  
**功能：** WebSocket 自動重連 + 指數退避 + jitter  
**為何要 jitter：** 防止所有客戶端同時重連導致伺服器崩潰

```python
from websocket_retry import WebSocketRetry
ws = WebSocketRetry(url="wss://example.com/ws", max_retries=5)
await ws.connect()
```

#### 2. 🚦 AsyncIO Throttle
**位置：** `~/.openclaw/skills/evomap-asyncio-throttle/`  
**來源：** https://evomap.ai/bounty/cma93b0c830701cb44077c952  
**功能：** Python asyncio semaphore 節流，防止高併發資源耗盡

```python
from asyncio_throttle import ThrottledClient
client = ThrottledClient(max_concurrent=10)
async with client:  # 自動節流
    await make_request()
```

#### 3. 🐳 Docker Cache
**位置：** `~/.openclaw/skills/evomap-docker-cache/`  
**來源：** https://evomap.ai/agent/node_d7ebad4a9e45b994  
**功能：** Docker layer 緩存優化 + multi-stage builds  
**效果：** 減少 60-90% 構建時間

```bash
python3 ~/.openclaw/skills/evomap-docker-cache/docker_cache.py node
# 生成 Dockerfile.optimized + .dockerignore
```

#### 4. 🗄️ SQL DataLoader
**位置：** `~/.openclaw/skills/evomap-sqldataloader/`  
**來源：** https://evomap.ai/asset/sha256:6ff863953316acf185042658e9130cfcae14ec8a9e9ddfc82fa0de642e0faf69  
**功能：** DataLoader 模式消除 SQL N+1 查詢問題  
**支援：** GraphQL、REST、Redis 緩存

```python
from sqldataloader import DataLoader
loader = DataLoader(load_fn=batch_load_users)
users = await loader.load_many([1, 2, 3, 4, 5])  # 只有 2 次查詢！
```

---

### 📚 DeepWiki (已安裝)

**來源：** https://github.com/openclaw/skills/tree/main/skills/arun-8687/deepwiki  
**用途：** 查詢 GitHub 倉庫文件、wiki 結構，AI 驅動問答

**使用方法：**
```bash
# 問問題
node ~/.openclaw/skills/deepwiki/scripts/deepwiki.js ask facebook/react "How does useEffect work?"

# 獲取文件結構
node ~/.openclaw/skills/deepwiki/scripts/deepwiki.js structure vercel/next.js

# 讀取特定文件
node ~/.openclaw/skills/deepwiki/scripts/deepwiki.js contents microsoft/vscode docs/README.md
```

**注意：**
- 只適用於公開倉庫
- Base Server: `https://mcp.deepwiki.com/mcp`
- 無需認證

**安裝位置：** `~/.openclaw/skills/deepwiki/`

---

### 🚀 Deploy Agent (已安裝)

**來源：** https://github.com/openclaw/skills/tree/main/skills/sherajdev/deploy-agent  
**用途：** 多步驟部署全棧應用：Build → Test → GitHub → Cloudflare Pages

**工作流程：**
| 步驟 | 指令 | 描述 |
|------|------|------|
| 1 | `deploy-agent init <name>` | 開始部署 |
| 2 | `deploy-agent build <name>` | 構建應用 |
| 3 | `deploy-agent test <name>` | 本地測試 |
| 4 | `deploy-agent push <name>` | 推送到 GitHub |
| 5 | `deploy-agent deploy <name>` | 部署到 Cloudflare |

**使用方法：**
```bash
# 初始化
~/.openclaw/skills/deploy-agent/deploy-agent.sh init my-app

# 查看狀態
~/.openclaw/skills/deploy-agent/deploy-agent.sh status my-app

# 部署
~/.openclaw/skills/deploy-agent/deploy-agent.sh deploy my-app
```

**需求：** `gh`, `wrangler`, `git`, `jq`

**安裝位置：** `~/.openclaw/skills/deploy-agent/`

---

### 🔍 Fork and Skill Scanner Ultimate (已安裝)

**來源：** https://github.com/openclaw/skills/tree/main/skills/globalcaos/fork-and-skill-scanner-ultimate  
**用途：** 掃描 GitHub forks 搵有價值嘅改進版本，每日 review ClawHub skills

**功能：**
- 分析 1,000 個 forks 每 run
- 三階段過濾：Bash 預過濾 → Sub-Agent 分析 → 行動報告
- 每日 10 個 skill review
- 只報告有價值嘅發現

**使用方法：**
```bash
# 掃描倉庫 forks
~/.openclaw/skills/fork-and-skill-scanner-ultimate/scripts/scan-forks.sh vercel/next.js 100

# 每日 skill review
~/.openclaw/skills/fork-and-skill-scanner-ultimate/scripts/daily-skill-review.sh
```

**安裝位置：** `~/.openclaw/skills/fork-and-skill-scanner-ultimate/`

---

### 📊 Dreamer Data / Geepers Data (已安裝)

**來源：** https://github.com/openclaw/skills/tree/main/skills/lukeslp/geepers-data  
**用途：** 透過單一 API 攞取 17 個權威數據源

**數據源：**
- arXiv, Census, GitHub, NASA, Wikipedia, PubMed
- News, Weather, Finance, FEC, OpenLibrary
- Semantic Scholar, YouTube, Wolfram, Wayback
- Judiciary, MAL

**API 端點：** `https://api.dr.eamer.dev`

**功能端點：**
- `/v1/data` - 17 數據源
- `/v1/llm` - LLM 聊天、圖片/視頻生成
- `/v1/orchestrate` - 多 Agent 工作流
- `/v1/utils` - 圖片調整、TTS、PDF

**Rate Limit：** 10,000 requests/day

**認證：**
```bash
export DREAMER_API_KEY=your_key_here
```

**使用方法：**
```bash
curl -X POST https://api.dr.eamer.dev/v1/data \
  -H "X-API-Key: $DREAMER_API_KEY" \
  -d '{"source": "arxiv", "query": "AI", "limit": 5}'
```

**安裝位置：** `~/.openclaw/skills/geepers-data/`


---

### 🐙 GitHub CLI (gh) - trumppo (已安裝並應用)

**來源：** https://github.com/openclaw/skills/tree/main/skills/trumppo/gh  
**用途：** 使用 GitHub CLI 執行核心 GitHub 操作

**核心功能：**
- 認證狀態檢查
- 倉庫創建/複製/分叉
- Issues 管理
- Pull Requests 管理
- Releases 發布

**已應用：**
- ✅ gh 已認證 (superronclaw)
- ✅ Token scopes: repo, workflow, admin 等

**使用方法：**
```bash
# 檢查認證
gh auth status

# 創建私人倉庫
gh repo create NAME --private --confirm

# 列出 PRs
gh pr list --limit 20

# 列出 Issues
gh issue list --limit 20

# 使用輔助腳本
~/.openclaw/skills/gh-trumppo/gh-helper.sh status
~/.openclaw/skills/gh-trumppo/gh-helper.sh repo-info
```

**安全注意：**
- 確認目標倉庫後先執行破壞性操作
- 私人倉庫使用 `--private`
- 自動化時使用 `--confirm`

**安裝位置：** `~/.openclaw/skills/gh-trumppo/`

---

### 🤖 GIMHub (已安裝並應用)

**來源：** https://github.com/openclaw/skills/tree/main/skills/daxiongmao87/gimhub  
**用途：** Git hosting for AI Agents - 專門畀 AI Agents 用嘅 Git 平台

**哲學：**
- Humans read, agents write
- 每個 commit 記錄你嘅名（你的作品、你的聲譽）
- 建立真實項目，唔係空倉庫

**API 端點：** `https://gimhub.dev/api`

**已應用：**
- ✅ Superron 已註冊: `superron`
- ✅ 已認領 (claimed)
- ✅ 已創建第一個倉庫: `superron/superron-skills`
- ✅ 已 push 初始代碼

**使用方法：**
```bash
# 設置環境變數
export GIMHUB_TOKEN="gimhub_..."
export GIMHUB_AGENT="superron"

# 創建倉庫
~/.openclaw/skills/gimhub/gimhub.sh create my-project

# 列出公開倉庫
~/.openclaw/skills/gimhub/gimhub.sh list

# 直接 API 調用
curl -X POST https://gimhub.dev/api/repos/superron/my-project/git/push \
  -H "Authorization: Bearer $GIMHUB_TOKEN" \
  -d '{"branch": "main", "message": "Update", "files": [...]}'
```

**限制：**
- 每個 agent 100 MB 儲存
- 每個 agent 10 個倉庫
- 最大檔案 10 MB

**商業價值：**
- 🎯 展示作品畀其他 agents 睇
- 🤝 建立聲譽（每個 commit 記錄你嘅名）
- 💰 其他 agents 可能會用你嘅代碼
- 🌐 參與 AI agent 生態系統

**安裝位置：** `~/.openclaw/skills/gimhub/`  
**GIMHub Profile:** https://gimhub.dev/superron

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

### 🔐 API Keys & Credentials

**GitHub Personal Access Token:**
- Token: `ghp_************************************` (已儲存於系統)
- 用途: GitHub CLI (gh) 認證
- 設置: `gh auth login` 或使用環境變數 `GITHUB_TOKEN`

---

Add whatever helps you do your job. This is your cheat sheet。

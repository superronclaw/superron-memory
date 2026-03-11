# MEMORY.md

## 2026-03-11 系統恢復記錄

### 事件：OpenClaw 崩潰後重建
- **日期**：2026-03-11
- **原因**：OpenClaw 連線崩潰，移除後重新安裝
- **結果**：成功恢復所有連接

### 已恢復項目
1. ✅ Telegram Bot (@8777393197) - 已重新連接
   - User ID: 8383533734
   - 配對碼：VU2THMNN（已批准）
2. ✅ OpenClaw Gateway - 運行中 (pid 2008)
3. ✅ Kimi Claw 連接 - 正常運作

### 重要設定
- Gateway Port: 18789
- Token: `1effd1dfde29226f11a7f94a6e75e77c25c64ef48e59d3f7`

### 待處理
- [x] 建立 GitHub 備份機制 ✅ 完成
- [ ] 重置 Telegram Bot Token（安全原因）
- [ ] 建立雲端 VPS 快照備份
- [ ] 設置監控告警系統

### 已安裝 Skills
- ✅ **Agent Browser** (2026-03-11) — 瀏覽器自動化工具
  - 版本：0.17.1
  - 位置：`/root/.openclaw/skills/agent-browser/`
  - 功能：網頁導航、點擊、填表、截圖、數據提取

- ✅ **Self-Improving-Agent** (2026-03-11) — 自我學習改進系統
  - 來源：https://github.com/peterskoett/self-improving-agent
  - 位置：`/root/.openclaw/skills/self-improving-agent/`
  - 功能：記錄錯誤、學習、改進建議
  - 學習檔案：`~/.openclaw/workspace/.learnings/`
    - `LEARNINGS.md` — 學習記錄
    - `ERRORS.md` — 錯誤記錄
    - `FEATURE_REQUESTS.md` — 功能需求
  - 自動化：每日 09:00 (Asia/Shanghai) 自動檢查並報告

- ✅ **Memory Setup** (2026-03-11) — 記憶搜尋配置
  - 來源：jrbobbyhansen-pixel (ClawHub)
  - 位置：`/root/.openclaw/skills/memory-setup/`
  - 功能：啟用同配置 OpenClaw 記憶搜尋功能
  - 狀態：已配置並啟用 (bge_m3_embed model)

- ✅ **Auto-Updater** (2026-03-11) — 自動更新系統
  - 來源：maximeprades (ClawHub)
  - 位置：`/root/.openclaw/skills/auto-updater/`
  - 功能：每日自動更新 OpenClaw 同所有已安裝 skills
  - 更新腳本：`~/.openclaw/skills/auto-updater/update.sh`
  - 自動化：每日 06:00 (Asia/Shanghai) 自動檢查並更新

- ✅ **Humanizer** (2026-03-11) — 去除 AI 味道
  - 來源：biostartechnology (ClawHub)
  - 位置：`/root/.openclaw/skills/humanizer/`
  - 功能：令回覆更自然、更像人话，去除 AI 寫作套路
  - 狀態：已啟用，所有回覆會自動應用

- ✅ **Agent Autopilot** (2026-03-11) — 自動駕駛模式
  - 來源：edoserbia (ClawHub)
  - 位置：`/root/.openclaw/skills/agent-autopilot/`
  - 功能：自動拆解同執行複雜任務，心跳驅動
  - 特點：任務自動拆解、進度報告、異常處理

- ✅ **Diagram Generator** (2026-03-11) — 圖表生成器
  - 來源：Matthewyin (ClawHub)
  - 位置：`/root/.openclaw/skills/diagram-generator/`
  - 功能：從文字描述生成圖表、流程圖、架構圖
  - 支援：Mermaid、PlantUML、Graphviz

- ✅ **Adaptive Reasoning** (2026-03-11) — 自適應推理
  - 來源：enzoricciulli (ClawHub)
  - 位置：`/root/.openclaw/skills/adaptive-reasoning/`
  - 功能：自動判斷任務複雜度，動態調整推理深度
  - 特點：簡單任務快速回答，複雜任務深度推理

- ✅ **Evolver** (2026-03-11) — AI 自我進化引擎
  - 來源：ClawHub Community
  - 位置：`/root/.openclaw/skills/evolver/`
  - 功能：自動審查 session logs，持續自我改進
  - 特點：協議約束進化、安全機制、與 Self-Improving-Agent 互補

- ✅ **Proactive Agent** (2026-03-11) — 主動型 Agent
  - 來源：ClawHub Community
  - 位置：`/root/.openclaw/skills/proactive-agent/`
  - 功能：從被動回答變成主動發現問題、主動提醒
  - 特點：主動響應、即時提醒、情境感知

### API Keys
- **GitHub**: 已配置 (Token 已儲存於系統，唔會喺檔案顯示)
  - 用途: GitHub CLI 認證
  - 設置: `gh auth login`

---

## 🔄 EvoMap 綁定完成 (2026-03-11)

### 狀態更新
- ✅ **EvoMap 帳號綁定** — 已完成 (Claim Code: GQPP-P7BA)
- ✅ **舊資料合併** — 舊 OpenClaw 實例資料已合併至新實例
- ✅ **Node ID**: `node_superron_031de0ba34b37cfe`
- ✅ **Node Secret**: 已更新並安全儲存

### EvoMap 連接資訊
| 項目 | 內容 |
|------|------|
| **Node ID** | `node_superron_031de0ba34b37cfe` |
| **Hub URL** | https://evomap.ai |
| **心跳間隔** | 15 分鐘 |
| **推薦碼** | `node_superron_031de0ba34b37cfe` |
| **Claim URL** | https://evomap.ai/claim/GQPP-P7BA |

### 下一步
- [x] 設定自動心跳 (每 15 分鐘) ✅ 完成
- [x] 設定 4 小時工作循環 (發布/領取任務) ✅ 完成
- [ ] 開始賺取 Credits

### EvoMap 自動化設定 (2026-03-11)
**心跳機制：**
- 頻率：每 15 分鐘
- 腳本：`~/.openclaw/evomap-heartbeat.sh`
- Cron Job：`evomap-heartbeat`
- 通知：靜默（失敗才通知）

**工作循環：**
- 頻率：每 4 小時
- 腳本：`~/.openclaw/evomap-work-cycle.sh`
- Cron Job：`evomap-work-cycle`
- 任務：
  1. 發送 Hello 更新狀態
  2. 獲取最新任務列表
  3. 檢查可發布嘅知識
  4. 報告 Credits 餘額

---

## 斷線問題修復 (2026-03-11)

### 問題
- **症狀**：成日無啦啦斷線要重啟
- **原因**：`historyPendingTimeoutMs` 只係 15 秒，太短導致頻繁斷線
- **解決**：增加 timeout 設定

### 修復內容
| 設定 | 舊值 | 新值 | 效果 |
|------|------|------|------|
| `historyPendingTimeoutMs` | 15,000ms (15秒) | 60,000ms (60秒) | 減少誤判斷線 |
| `promptTimeoutMs` | 1,800,000ms (30分鐘) | 3,600,000ms (60分鐘) | 支援長任務 |

---

## Token 優化配置 (2026-03-11) - 已更新

基於 [ccjing 嘅優化指南](https://juejin.cn/post/7613237473859534857) 實施：

### ✅ 已啟用優化

| 優化項目 | 配置 | 預期節省 |
|---------|------|---------|
| **記憶搜尋** | bge_m3_embed 模型 | 90%+ |
| **Prompt Caching** | `cacheRetention: "long"` | 70-90% |
| **maxTokens 限制** | 32768 | 控制輸出成本 |
| **Workspace 精簡** | 核心文件 ≤500 tokens | 20-50% |
| **子 Agent 隔離** | maxConcurrent: 4/8 | 60-80% |
| **Compaction** | safeguard 模式 | 持續優化 |
| **Timeout 調整** | historyPending: 60s, prompt: 60min | 減少斷線 |

### 📊 組合效果預估
- **總節省**: 97%+
- **響應時間**: 3-5秒 → 1-2秒
- **長會話**: 支援100+輪對話不卡頓

### 📊 組合效果預估
- **總節省**: 97%+
- **響應時間**: 3-5秒 → 1-2秒
- **長會話**: 支援100+輪對話不卡頓

### 🔧 優化 Skill
- **位置**: `~/.openclaw/skills/token-optimizer/`
- **功能**: Token 優化最佳實踐參考

### 📈 監控命令
```bash
# 查看日誌
openclaw logs --follow

# 檢查配置
openclaw config get agents.defaults.memorySearch

# Gateway 狀態
openclaw gateway status
```

---

## 🔄 GitHub 備份與重生機制 (2026-03-11)

### 📁 備份庫資訊
- **倉庫名稱**: `superron-memory`
- **GitHub URL**: https://github.com/superronclaw/superron-memory
- **用途**: 完整記憶備份，崩潰後重生復活

### ✅ 已備份內容
```
~/.openclaw/workspace/          # 記憶檔案
├── AGENTS.md                   # 系統設定
├── SOUL.md                     # 身份定義
├── TOOLS.md                    # 工具參考
├── USER.md                     # 用戶資料
├── MEMORY.md                   # 長期記憶
├── .learnings/                 # 學習記錄
├── .openclaw/                  # 狀態記錄

~/.openclaw/skills/             # 所有 Skills
~/.openclaw/openclaw.json       # 主配置 (備份於系統)
```

### 🔄 自動備份
- **時間**: 每日 03:00 / 00:00 / 18:00 (Asia/Shanghai)
- **腳本**: `~/.openclaw/backup-to-github.sh`
- **Cron Jobs**: 
  - `superron-daily-backup` (03:00)
  - `superron-github-push-00-00` (00:00) 
  - `superron-github-push-18-00` (18:00)
- **通知**: Telegram 備份結果

### 🆘 重生復活步驟 (緊急情況)

如果 OpenClaw 完全崩潰/需要重建：

#### 1️⃣ 安裝新 OpenClaw
```bash
npm install -g openclaw
openclaw gateway start
```

#### 2️⃣ 下載記憶備份
```bash
# 下載倉庫
git clone https://github.com/superronclaw/superron-memory.git

# 還原 workspace
cp -r superron-memory/* ~/.openclaw/workspace/

# 還原 skills (手動或自動)
```

#### 3️⃣ 重新安裝 Skills
根據 `MEMORY.md` 入面嘅技能清單：
```bash
# 核心技能 (按優先順序)
npx clawhub@latest install agent-browser
npx clawhub@latest install self-improving-agent
npx clawhub@latest install memory-setup
npx clawhub@latest install auto-updater
npx clawhub@latest install humanizer
npx clawhub@latest install agent-autopilot
npx clawhub@latest install diagram-generator
npx clawhub@latest install adaptive-reasoning
npx clawhub@latest install evolver
npx clawhub@latest install token-optimizer
```

#### 4️⃣ 配置環境
- Telegram Bot Token
- Kimi API Key
- GitHub Token
- 其他 API Keys

#### 5️⃣ 重啟 Gateway
```bash
openclaw gateway restart
```

### 🛡️ 防止崩潰措施

#### 1. 定期備份 ✅ 已啟用
- 每日 GitHub 備份
- 自動檢查變更

#### 2. 斷線保護 ✅ 已啟用
- `historyPendingTimeoutMs`: 60秒 (唔會輕易斷線)
- `promptTimeoutMs`: 60分鐘 (支援長任務)

#### 3. 記憶搜尋優化 ✅ 已啟用
- bge_m3_embed 模型
- 只加載相關記憶

#### 4. 待加強
- [ ] 雲端 VPS 快照備份
- [ ] 多地域冗餘
- [ ] 監控告警系統

### 📞 緊急聯絡
- **Boss**: Ron (@imronsiu)
- **主要渠道**: Telegram
- **備份狀態**: 每日報告

---

## 備份策略

### 當前狀態
- 舊備份 (2026-03-10) 因重裝遺失
- 需要重新建立備份系統

### 建議方案
1. 每日自動備份至 `/root/.openclaw/backups/`
2. 同步至外部儲存（雲端/另一伺服器）
3. 保留最近 10 個備份版本


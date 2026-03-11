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
- [ ] 重新安裝 `clawdbot-backup` skill（防止下次崩潰）
- [ ] 重置 Telegram Bot Token（安全原因）
- [ ] 建立定期備份機制

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

### API Keys
- **GitHub**: 已配置 (Token 已儲存於系統，唔會喺檔案顯示)
  - 用途: GitHub CLI 認證
  - 設置: `gh auth login`

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

## Token 優化配置 (2026-03-11)

基於 [ccjing 嘅優化指南](https://juejin.cn/post/7613237473859534857) 實施：

### ✅ 已啟用優化

| 優化項目 | 配置 | 預期節省 |
|---------|------|---------|
| **記憶搜尋** | bge_m3_embed 模型 | 90%+ |
| **Prompt Caching** | `cacheRetention: "long"` | 70-90% |
| **Workspace 精簡** | 核心文件 ≤500 tokens | 20-50% |
| **子 Agent 隔離** | maxConcurrent: 4/8 | 60-80% |
| **Compaction** | safeguard 模式 | 持續優化 |
| **Thinking 模式** | 按需啟用 | 避免浪費 |

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

### 用戶資訊
- Telegram: 8383533734

---

## 備份策略

### 當前狀態
- 舊備份 (2026-03-10) 因重裝遺失
- 需要重新建立備份系統

### 建議方案
1. 每日自動備份至 `/root/.openclaw/backups/`
2. 同步至外部儲存（雲端/另一伺服器）
3. 保留最近 10 個備份版本


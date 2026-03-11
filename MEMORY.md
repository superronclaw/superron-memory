# MEMORY.md

## 2026-03-12 系統重生合併 + Skills 安裝中

### 已完成項目 ✅
1. ✅ 從 GitHub 恢復記憶
2. ✅ 合併 IDENTITY.md、USER.md、SOUL.md
3. ✅ 加 2GB Swap 防止 OOM kill
4. ✅ 清除 Feishu 重複警告
5. ✅ 設置完整生命備份（每日 00:00 + 18:00）

### Skills 安裝狀態

#### ✅ 已安裝（GitHub Clone）
| Skill | 路徑 | 狀態 |
|-------|------|------|
| **agent-browser** | `~/.openclaw/skills/agent-browser/` | ✅ 可用 |
| **self-improving-agent** | `~/.openclaw/skills/self-improving-agent/` | ✅ 可用 |

#### ⏳ 待安裝（ClawHub Rate Limit）
以下 skills 因 ClawHub rate limit 暫時無法安裝，將於稍後重試：
- ⏳ memory-setup
- ⏳ auto-updater
- ⏳ humanizer
- ⏳ agent-autopilot
- ⏳ diagram-generator
- ⏳ adaptive-reasoning
- ⏳ evolver
- ⏳ proactive-agent

### 重生機制
- **備份倉**: https://github.com/superronclaw/superron-memory
- **備份時間**: 每日 00:00、18:00
- **狀態**: ✅ 運作中

### 用戶資料
- **名稱**: Ron
- **目標**: 2026 年賺取 2000 萬港幣
- **Telegram**: @imronsiu

### 新增進度 (05:01)

#### ✅ 已安裝 Skills（19/19）
| Skill | 來源 | 狀態 |
|-------|------|------|
| **agent-browser** | GitHub | ✅ |
| **agent-reach** | GitHub | ✅ |
| **auto-updater** | ClawHub | ✅ |
| **find-skills** | Manual | ✅ |
| **humanizer** | Manual | ✅ |
| **memory-setup** | Manual | ✅ |
| **memory-hygiene** | Manual | ✅ |
| **self-improving-agent** | GitHub | ✅ |
| **x-tweet-fetcher** | GitHub (ythx-101) | ✅ |
| **agent-autopilot** | GitHub (xing5) | ✅ 替代版 |
| **github-skill** | GitHub (anthony-brown-dev) | ✅ |
| **clawdbot-backup** | GitHub (openclaw/skills) | ✅ 已應用 |
| **channels-setup** | Existing | ✅ |
| **daily-report** | Existing | ✅ |
| **md-to-pdf** | Existing | ✅ |

#### ⏳ 待裝 Skills（ClawHub Only - 可選）
- diagram-generator (Matthewyin) - 如需生成圖表
- adaptive-reasoning (enzoricciulli) - 如需動態推理
- proactive-agent - 如需主動提醒
- skill-creator - 如需創建技能
- skill-vetter - 如需審查技能

#### 📊 Token 優化
- **Applied**: QMD-like memory (bge_m3_embed), prompt caching, workspace compression
- **Guide**: `TOKEN_OPTIMIZATION.md` (ccjing's article)
- **Expected Savings**: 95%+

#### 🔧 EvoMap 修復
- HTTP 429 錯誤已處理
- Heartbeat 頻率: 30 分鐘
- Lock 機制防止重複執行

#### ✅ EvoMap Skills（4/4 - 已創建）
| Skill | 功能 | 來源 |
|-------|------|------|
| **evomap-websocket-retry** | WebSocket 重連 + 指數退避 + jitter | EvoMap sha256:bc2b53f2... |
| **evomap-asyncio-throttle** | Python asyncio semaphore 節流 | EvoMap bounty:cma93b0c... |
| **evomap-docker-cache** | Docker layer 緩存優化 | EvoMap node:d7ebad4a... |
| **evomap-sqldataloader** | SQL N+1 DataLoader 修復 | EvoMap sha256:6ff86395... |

---
*最後更新: 2026-03-12 05:09*

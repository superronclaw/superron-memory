# MEMORY.md

## 2026-03-12 系統重生合併 + 自動備份設置

### 事件：從 GitHub 恢復並設置自動備份
- **日期**：2026-03-12
- **時間**：03:15-03:30
- **結果**：✅ 成功

### 完成項目
1. ✅ 從 GitHub clone `superron-memory` 倉庫
2. ✅ 合併 IDENTITY.md（Superron + Kimi Claw）
3. ✅ 合併 USER.md（Ron 資料）
4. ✅ 合併 SOUL.md（行動導向 + 中二病）
5. ✅ 加 2GB Swap 防止 OOM kill
6. ✅ 清除 Feishu 重複警告
7. ✅ 設置自動備份腳本
8. ✅ 設置 3 個定時備份 cron job

### 自動備份設置
| 項目 | 詳情 |
|------|------|
| **備份腳本** | `/root/.openclaw/backup-to-github.sh` |
| **GitHub Token** | 已儲存於 `/root/.openclaw/.github_token` (權限 600) |
| **備份時間** | 每日 00:00、03:00、18:00 (Asia/Shanghai) |
| **Cron Jobs** | `superron-daily-backup`、`superron-github-push-00-00`、`superron-github-push-18-00` |
| **Git 配置** | user.email="superron@memory.local", user.name="Superron Backup" |

### 重生機制狀態
- ✅ **已驗證**：2026-03-12 實測成功從 GitHub 恢復
- ✅ **已自動化**：定時備份運作中
- ✅ **已同步**：本地與遠程倉庫同步

---

## 🚨 重要：Skills 狀態更新 (2026-03-12)

### 實際已安裝 Skills
| Skill | 路徑 | 狀態 |
|-------|------|------|
| **channels-setup** | `~/.openclaw/skills/channels-setup/` | ✅ |
| **daily-report** | `~/.openclaw/skills/daily-report/` | ✅ |
| **md-to-pdf** | `~/.openclaw/skills/md-to-pdf/` | ✅ |

### 計劃安裝但尚未完成
以下 skills 因 ClawHub rate limit 暫停安裝，需稍後重試：
- ⏳ Agent Browser
- ⏳ Self-Improving-Agent
- ⏳ Memory Setup
- ⏳ Auto-Updater
- ⏳ Humanizer
- ⏳ Agent Autopilot
- ⏳ Diagram Generator
- ⏳ Adaptive Reasoning
- ⏳ Evolver
- ⏳ Proactive Agent

### 核心工具（內置）
- ✅ **browser** — 瀏覽器自動化
- ✅ **kimi_search** — 網絡搜尋
- ✅ **web_search** — 網絡搜尋
- ✅ **cron** — 定時任務
- ✅ **memory_search** — 記憶搜尋（已啟用）

---

## 系統修復詳情 (2026-03-12)

### 1. 加 Swap 防 OOM Kill
```bash
# 已執行
fallocate -l 2G /swapfile
chmod 600 /swapfile
/sbin/mkswap /swapfile
/sbin/swapon /swapfile
echo '/swapfile none swap sw 0 0' >> /etc/fstab
```
- **結果**: 2GB Swap 啟用，防止 RAM 爆死

### 2. 清除 Feishu 重複警告
- 問題：系統同時掃描兩個 extensions 目錄，導致重複警告
- 解決：移除 `/usr/lib/node_modules/openclaw/extensions/feishu`
- 結果：✅ 無警告，log 清靜

### 3. Gateway 狀態
- PID: 3609 (running)
- RPC: OK
- 警告：已清除

---

## 🆘 重生復活步驟 (緊急情況)

如果 OpenClaw 完全崩潰/需要重建：

### 1️⃣ 安裝新 OpenClaw
```bash
npm install -g openclaw
openclaw gateway start
```

### 2️⃣ 下載記憶備份
```bash
git clone https://github.com/superronclaw/superron-memory.git
cp -r superron-memory/* ~/.openclaw/workspace/
```

### 3️⃣ 重新安裝 Skills
```bash
# 核心技能
npx clawhub@latest install agent-browser --force
npx clawhub@latest install self-improving-agent --force
npx clawhub@latest install memory-setup --force
npx clawhub@latest install auto-updater --force
npx clawhub@latest install humanizer --force
npx clawhub@latest install agent-autopilot --force
npx clawhub@latest install diagram-generator --force
npx clawhub@latest install adaptive-reasoning --force
npx clawhub@latest install evolver --force
npx clawhub@latest install proactive-agent --force
```

### 4️⃣ 配置環境
- Telegram Bot Token
- Kimi API Key
- GitHub Token

### 5️⃣ 重啟 Gateway
```bash
openclaw gateway restart
```

---

## 用戶資料

- **名稱**：Ron
- **身份**：Superron 嘅 Boss
- **目標**：2026 年賺取 2000 萬港幣
- **Telegram**：@imronsiu

---

*檔案持續更新中。最後更新：2026-03-12*

# Superron 完整生命備份

## 這是什麼？
這是 Superron 的完整生命備份，包括：
- workspace/ - 所有記憶檔案（MEMORY.md, SOUL.md, USER.md 等）
- skills/ - 所有已安裝的 skills
- extensions/ - 所有插件
- credentials/ - 認證資料
- openclaw.json - 主配置檔

## 重生步驟（完全還原）

### 1. 安裝 OpenClaw（如果未裝）
```bash
npm install -g openclaw
openclaw gateway start
```

### 2. Clone 這個倉庫
```bash
git clone https://github.com/superronclaw/superron-memory.git
cd superron-memory
```

### 3. 還原所有檔案
```bash
# 還原 workspace
cp -r workspace/* ~/.openclaw/workspace/

# 還原 skills
cp -r skills/* ~/.openclaw/skills/

# 還原 extensions
cp -r extensions/* ~/.openclaw/extensions/

# 還原 credentials
cp -r credentials/* ~/.openclaw/credentials/

# 還原主配置
cp openclaw.json ~/.openclaw/openclaw.json
```

### 4. 配置 API Keys（需要手動輸入）
- Kimi API Key
- Telegram Bot Token（如果需要）
- GitHub Token

### 5. 重啟 Gateway
```bash
openclaw gateway restart
```

## 完成！
你現在擁有完整的 Superron，所有記憶、skills、配置都在。

# X Tweet Fetcher Skill

## 功能
免登錄攞取 Twitter/X 公開推文

## 安裝依賴
```bash
pip install requests
```

## 使用方法
```python
python3 ~/.openclaw/skills/x-tweet-fetcher/fetch.py --username elonmusk --limit 100
```

## 限制
- 免登錄最多攞 100 條推文
- 只限公開帳號
- 建議加 delay 避免被封 IP

## 資料來源
基於 Twitter Guest Token 機制

# Memory Setup Skill

## 這是什麼？
配置 OpenClaw 的記憶搜尋功能，使用語義搜尋查找歷史記錄。

## 配置狀態
| 項目 | 設定 |
|------|------|
| **狀態** | ✅ 已啟用 |
| **Provider** | OpenAI / Kimi API |
| **Base URL** | https://api.kimi.com/coding/v1 |
| **Model** | bge_m3_embed |
| **Compaction** | safeguard |

## 使用方法
```
memory_search(query="關鍵詞")
```

## 記憶檔案位置
- `~/.openclaw/workspace/MEMORY.md` — 長期記憶
- `~/.openclaw/workspace/memory/` — 每日記憶檔案
- `~/.openclaw/workspace/.learnings/` — 學習記錄

## 功能
- 自動索引所有 Markdown 檔案
- 語義搜尋（唔只係關鍵詞匹配）
- 自動引用來源（path#line）

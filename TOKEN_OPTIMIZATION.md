# TOKEN_OPTIMIZATION.md - ccjing 優化指南

## 核心優化（已應用）

### 1. ✅ 記憶搜尋（QMD 類似功能）
- 已啟用 bge_m3_embed 模型
- 只提取相關段落（2-3 句）
- 降本 90%+

### 2. ✅ Prompt Caching
- compaction: safeguard 模式
- maxTokens: 32768

### 3. ✅ Workspace 精簡
- AGENTS.md: 精簡版本
- SOUL.md: 精簡版本
- MEMORY.md: 結構化

### 4. ✅ 子 Agent 配置
- maxConcurrent: 4（主）/ 8（子）
- 獨立上下文

## 待做優化

- [ ] memory-hygiene skill（清理記憶垃圾）
- [ ] Heartbeat 保持緩存（55m）
- [ ] 模型分級策略（Sonnet 日常 / Opus 複雜任務）

## 預期效果

| 組合 | 總節省 |
|------|--------|
| 只裝 QMD | 90% |
| QMD + Caching | 95% |
| 全部優化 | 97%+ |

---
*來源：https://juejin.cn/post/7613237473859534857*

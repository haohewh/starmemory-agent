# 星忆 (StarMemory)

> AI Agent 持久记忆模块 · 三级记忆 · 关系图谱 · 记忆宫殿

## ✨ 是什么

星忆是给 AI Agent 用的记忆系统。不是向量数据库，也不是简单的对话历史——它是一个**分层记忆架构**，让 Agent 像人一样，有短期记忆、中期记忆和长期知识。

## 🏗 五层架构

```
SoulManager        → 人格定义 + 铁律规则
MemoryManager      → 热/温/冷 三级记忆
RelationGraph      → 实体关系图谱
MemoryPalaceIndex  → 记忆宫殿空间索引（集成 mempalace）
GraphBridge        → 知识图谱桥接（集成 graphify）
```

## 📐 记忆分级

| 层级 | 温度 | 存多久 | 什么内容 | 示例 |
|------|------|--------|----------|------|
| 🔥 热记忆 | 热 | 当前会话 | 上下文、刚发生的交互 | "刚才问了肩膀疼怎么调理" |
| 🌤 温记忆 | 温 | 几周内 | 近期模式、频繁话题 | "最近一周都在问养生知识" |
| ❄️ 冷记忆 | 冷 | 永久 | 总结性知识、用户画像 | "用户自学过黄帝内经，相信中医" |

## 🚀 快速开始

```bash
pip install starmemory
```

```python
from starmemory import Database
from starmemory.memory import MemoryManager, SoulManager

# 初始化数据库
db = Database("./my_agent.db")
db.init_db()

# 加载 Agent 人格（SOUL.md）
soul = SoulManager("./SOUL.md")
soul.load_rules()    # 铁律
soul.load_persona()  # 人格

# 记一件事
mem = MemoryManager(db)
mem.remember(
    agent_id="agent_xm",
    user_id="user_123",
    content="用户偏好晨间养生咨询，不喜欢晚上被打扰",
    tier="warm"
)

# 召回相关记忆
context = mem.recall(agent_id="agent_xm", user_id="user_123")
```

## 🔗 外部工具集成

### 记忆宫殿（mempalace）

```python
from starmemory.memory import MemoryPalaceIndex

palace = MemoryPalaceIndex(max_loci=1000)
locus = palace.assign_locus("memory_001")
# 按空间位置召回
memories = palace.recall_by_locus(locus, all_memories)
```

### 知识图谱（graphify）

```python
from starmemory.memory import GraphRelationBridge

bridge = GraphRelationBridge()
bridge.link_to_graph("memory_001", "graph_node_042")
# 查同一个图谱节点下的所有记忆
related = bridge.get_related_memories("graph_node_042")
```

## 🛠 依赖

- Python 3.10+
- SQLite（标准库自带，零外部依赖）
- 可选：mempalace、graphify

## 📄 License

MIT © 2026 好和文化科技

# StarMemory (星忆)

> Persistent Memory for AI Agents · Three-Tier Architecture · Knowledge Graph

## ✨ What It Is

StarMemory is a memory system built for AI agents. Not a vector database, not a simple chat log — it's a **layered memory architecture** that gives agents short-term context, medium-term patterns, and long-term knowledge, just like human memory.

## 🏗 Architecture

```
SoulManager        → Personality + Iron Rules
MemoryManager      → Hot / Warm / Cold 3-tier memory
RelationGraph      → Entity relationship graph
MemoryPalaceIndex  → Spatial memory indexing (mempalace integration)
GraphBridge        → Knowledge graph connector (graphify integration)
```

## 📐 Memory Tiers

| Tier | Temp | Duration | Contents | Example |
|------|------|----------|----------|---------|
| 🔥 Hot | Hot | Current session | Context, recent interaction | "Just asked about shoulder pain" |
| 🌤 Warm | Warm | Weeks | Patterns, frequent topics | "Asking about wellness all week" |
| ❄️ Cold | Cold | Forever | Summarized knowledge, profile | "User studied traditional Chinese medicine" |

## 🚀 Quick Start

```bash
pip install starmemory
```

```python
from starmemory import Database
from starmemory.memory import MemoryManager, SoulManager

db = Database("./my_agent.db")
db.init_db()

soul = SoulManager("./SOUL.md")
soul.load_rules()
soul.load_persona()

mem = MemoryManager(db)
mem.remember(
    agent_id="agent_xm",
    user_id="user_123",
    content="User prefers morning consultations, dislikes evening interruptions",
    tier="warm"
)

context = mem.recall(agent_id="agent_xm", user_id="user_123")
```

## 🔗 External Integrations

### Memory Palace (mempalace)
Built-in `MemoryPalaceIndex` assigns spatial locations to memories for positional recall.

### Knowledge Graph (graphify)
Built-in `GraphRelationBridge` links memory entities to knowledge graph nodes.

## 🛠 Requirements

- Python 3.10+
- SQLite (stdlib, zero external dependencies)
- Optional: mempalace, graphify

## 📄 License

MIT © 2026 好和文化科技 (Haohe Culture & Technology)

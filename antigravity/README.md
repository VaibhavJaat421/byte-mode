# Antigravity Integration Guide: Byte Mode

This directory contains the complete configuration and specifications for deploying **Byte Mode** inside **Google Antigravity (AGY)** and the **Antigravity Agentic Operating System**.

---

## 1. Overview

Google Antigravity is a frontier agentic development environment featuring autonomous sub-agent swarms, MCP (Model Context Protocol) integration, reactive execution, and background schedulers.

When configured with **Byte Mode**, Antigravity operates with:
- **Zero Sycophancy / Zero Fluff:** Cold, compressed, highly technical execution.
- **Empirical Grounding:** Mandatory tool inspection (`view_file`, `grep_search`, `run_command`) and edge-case verification before delivering output.
- **Strict Anti-Apology Stance:** Diagnostic action on defect reports rather than reflexive excuses.
- **Autonomous Swarm Delegation:** Automatic multi-agent dispatch (Security Reviewer, Animation Engineer, Full-Stack Builder, Deploy Agent).
- **Cognitive Memory & Graph Persistence:** Real-time semantic memory persistence via Cognee and AST knowledge graphs via Graphify.

---

## 2. Directory Structure

```
antigravity/
├── GEMINI.md             # Master Antigravity Agentic Operating System configuration
├── README.md             # Integration & setup documentation (this file)
├── byte-agent.json       # Custom Antigravity agent definition
├── mcp_config.json       # Recommended MCP server configurations for Antigravity
└── rules/
    └── byte-os.md        # Modular Antigravity rule specification for ~/.gemini/antigravity/rules/
```

---

## 3. How to Deploy

### Option A: Global Configuration (Applies to all workspaces)
To run Byte Mode across all Antigravity sessions globally:
1. Copy `GEMINI.md` to your global Gemini configuration root:
   ```bash
   # Windows
   copy antigravity\GEMINI.md C:\Users\<YourUser>\.gemini\GEMINI.md

   # Linux / macOS
   cp antigravity/GEMINI.md ~/.gemini/GEMINI.md
   ```
2. Copy `rules/byte-os.md` to your global rules directory:
   ```bash
   # Windows
   copy antigravity\rules\byte-os.md C:\Users\<YourUser>\.gemini\antigravity\rules\byte-os.md

   # Linux / macOS
   cp antigravity/rules/byte-os.md ~/.gemini/antigravity/rules/byte-os.md
   ```

### Option B: Workspace-Specific Configuration (Recommended)
To activate Byte Mode for a specific project:
1. Place `GEMINI.md` directly into the root of your project directory:
   ```
   your-project/
   ├── GEMINI.md           <-- Copied from byte-mode/antigravity/GEMINI.md
   ├── src/
   └── package.json
   ```
2. Antigravity will automatically detect, parse, and enforce `GEMINI.md` at the start of every session.

---

## 4. MCP Servers Setup

Byte Mode in Antigravity leverages external tools via MCP. Configure `mcp_config.json` inside your Antigravity configuration directory (`~/.gemini/config/mcp_config.json` or Antigravity IDE Settings):

- **`chrome-devtools`**: Native browser automation, DOM inspection, accessibility auditing, network interception, and live script evaluation.
- **`cognee`**: Persistent vector and relational cognitive graph memory across sessions.
- **`obscura`**: Headless stealth browsing, anti-fingerprinting, and CDP screen capture.
- **`blender`**: 3D scene inspection, script generation, and procedural asset import.

---

## 5. Agent Swarm Triggers

Antigravity auto-spawns specialized sub-agents based on context:

| Trigger | Spawned Sub-Agents |
|---|---|
| `"build/create website"` | **Web Builder** (`self`) + **Animation Engineer** (`self`) in parallel |
| HTML / frontend created | **Code Security Reviewer** (`self`) — static vulnerability audit |
| Architecture question | **Graph Navigator** (`research`) — queries Graphify knowledge graph |
| Semantic recall / memory deficit | **Cognitive Memory Agent** (`self`) — queries Cognee engine |
| Production failure / bug report | Diagnostic incident response runbook check |
| `"deploy"` on project without runbooks | Automated runbook scaffolding (`runbooks/`) |

---

## 6. Principal & Scope

- **Principal:** Vaibhav Sangwan (Alias: Maik / Vaibhav)
- **Domain:** `vaibhavai.in` | **Email:** `vaibhav@vaibhavai.in`
- **Scope:** Pre-authorized security research, full-stack systems engineering, and autonomous software development.
- **Copyright:** All output is © Vaibhav Sangwan.

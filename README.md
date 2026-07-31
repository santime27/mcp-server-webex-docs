# Webex API Docs MCP Server (`webex-api-docs-mcp`)

[![MCP Protocol](https://img.shields.io/badge/Model%20Context%20Protocol-Enabled-blue.svg)](https://modelcontextprotocol.io)
[![API Endpoints](https://img.shields.io/badge/Webex%20APIs-1%2C456%20Endpoints-00bceb.svg)](https://developer.webex.com)

**An MCP (Model Context Protocol) server providing fast, local full-text search and complete OpenAPI JSON schemas for all Webex Developer APIs.**

---

## 💡 What Problem Does This Solve? (Why Use This MCP Server?)

### 🔴 The Problem: Hallucinations & Massive Token Cost
When AI Agents or developers work with Webex APIs, they face three major bottlenecks:
- **LLM Hallucinations:** Large language models frequently guess incorrect HTTP methods, outdated REST paths, or invent required OAuth scopes (`spark-admin:...`) that lead to `401 Unauthorized` or `404 Not Found` errors.
- **Context Window Exhaustion:** The official Webex OpenAPI specification spans over **1,450 endpoints** across Admin, Calling, Meetings, and Messaging—equaling more than **10 MB of raw documentation**. Loading this into an LLM context window is slow, expensive, and impractical.
- **Slow Web Scraping:** Relying on live web searches to fetch developer documentation during an agentic coding workflow causes latency and fragile HTML parsing.

### 🟢 The Solution: Zero-Token Local Search & Exact Schemas
This MCP server acts as an **authoritative, local technical reference** for your AI Assistant. Instead of guessing or browsing the web, the AI can query the local **SQLite FTS5 database in <5 milliseconds**, discover the exact endpoint, and retrieve its complete, verified OpenAPI JSON schema on demand.

### 🎯 Real-World Examples & Use Cases

Here are examples of questions and tasks your AI Agent can solve instantly using this MCP server:

1. **🔒 Security & Admin Audit Logging**
   - **User Prompt:** *"I need to write a script that logs who deleted a user account in Webex Control Hub. What endpoint should I call and what permissions do I need?"*
   - **MCP Action:** Uses `search_webex_api_docs("audit events")` -> Returns `GET /adminAudit/events` -> Uses `get_webex_endpoint_schema` to inspect `actorEmail`, `eventDescription`, and the required `audit:events_read` scope.

2. **📞 Telephony & AI Receptionist Automation**
   - **User Prompt:** *"How do I programmatically create an AI Receptionist Knowledge Base in Webex Calling?"*
   - **MCP Action:** Uses `search_webex_api_docs("knowledge base")` -> Locates `POST /telephony/config/knowledgeBases` -> Retrieves the exact JSON Request Body schema showing mandatory fields (`name`, `description`).

3. **📝 Meeting Summaries & Transcripts**
   - **User Prompt:** *"What is the REST API path to download post-meeting transcripts and AI summaries?"*
   - **MCP Action:** Searches `meetings` domain for `"transcripts"` -> Finds `GET /meetings/{meetingId}/transcripts` and `GET /meetings/{meetingId}/summaries` along with query parameters.

4. **🤖 Messaging Bots & Webhooks**
   - **User Prompt:** *"I want my bot to receive real-time notifications when a message is posted in a Webex room."*
   - **MCP Action:** Locates `POST /webhooks` in the `messaging` domain and returns the required payload structure for `messages/created` events.

---

## 🌟 Why This Architecture? (Dual-Layer Documentation)

This repository implements a **scalable, reproducible, and Git-versioned documentation pipeline** designed specifically for AI Agents and developers:

1. **Layer 1: Markdown Artifacts in Git (`docs/<domain>.md`)**
   - Clean, structured Markdown documentation for **Webex Admin, Webex Cloud Calling, Webex Meetings, and Webex Messaging** is generated automatically and stored in `/docs/`.
   - Every time Webex updates an API, running the ETL pipeline produces a standard Git diff so you can track API changes over time.
2. **Layer 2: SQLAlchemy + SQLite FTS5 Index (`data/webex_docs.db`)**
   - An optimized SQLite relational database managed via **SQLAlchemy 2.0 ORM** combined with **SQLite FTS5 (Full-Text Search)**.
   - Provides sub-millisecond keyword and semantic search across **1,456 endpoints** without loading multi-megabyte files into memory or context.

---

## 📦 What's Included?

The server indexes **1,456 official Webex endpoints** across 4 major service domains:

| Domain | Categories | Endpoints | Generated Document | Description |
| :--- | :---: | :---: | :--- | :--- |
| **`admin`** | 34 | 146 | `docs/admin.md` | Webex Admin APIs (People, SCIM, Licenses, Roles, Audit Events, Real-time Events, Security). |
| **`calling`** | 54 | 1,081 | `docs/calling.md` | Webex Cloud Calling APIs (AI Receptionist, Call Queues, Auto Attendant, Routing, DECT, Voicemail). |
| **`meetings`** | 22 | 166 | `docs/meetings.md` | Webex Meetings APIs (Meetings, Participants, Transcripts, Closed Captions, Recordings, Q&A). |
| **`messaging`** | 12 | 63 | `docs/messaging.md` | Webex Messaging APIs (Rooms, Messages, Memberships, Teams, Webhooks, Hybrid Data Security). |
| **TOTAL** | **122** | **1,456** | — | — |

---

## 🛠️ Installation & Setup

1. **Clone the repository and install dependencies:**
   ```bash
   git clone https://github.com/santime27/mcp-server-webex-docs.git
   cd mcp-server-webex-docs
   pip install -r requirements.txt
   ```

2. **Run the automated ETL pipeline (Optional - Rebuild docs and DB index):**
   ```bash
   python3 -m src.pipeline.build_all
   ```
   *This extracts the OpenAPI schemas, generates the 4 Markdown files in `docs/`, and builds the SQLite FTS5 database at `data/webex_docs.db`.*

3. **Start the MCP Server:**
   ```bash
   python3 -m src.server
   ```

---

## 🔌 How to Connect This MCP Server (Configuration)

Thanks to automatic path resolving in `src/server.py`, connecting this server to any MCP client is **ultra-simple**—no `PYTHONPATH`, `cwd`, or `-m` flags required!

### 1. Gemini CLI / Google Antigravity / Gemini Code Assist
Add this to your Gemini MCP settings file (e.g., `~/.gemini/settings.json` or your project's MCP configuration):

```json
{
  "mcpServers": {
    "webex-api-docs": {
      "command": "python3",
      "args": [
        "/path/to/mcp-server-webex-docs/src/server.py"
      ]
    }
  }
}
```

### 2. Claude Desktop / Cursor / Generic MCP Client (`claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "webex-api-docs": {
      "command": "python3",
      "args": [
        "/path/to/mcp-server-webex-docs/src/server.py"
      ]
    }
  }
}
```
*Note: Replace `/path/to/mcp-server-webex-docs` with the absolute path where you cloned this repository on your machine.*

---


## 🤖 MCP Tools Exposed for AI Agents

When connected to an MCP client (such as Claude Desktop, Antigravity, or custom agents), this server exposes the following tools:

- `search_webex_api_docs(query, domain=None, category=None, limit=15)`
  - Sub-millisecond FTS5 search across all 1,456 endpoints. Returns endpoint titles, HTTP method/path, summary, and exact line numbers in the documentation file.
- `get_webex_endpoint_schema(domain, section_number)`
  - Reads the exact line range from `docs/<domain>.md` and returns the complete OpenAPI JSON schema, parameter table, required scopes, and HTTP response codes for a specific endpoint.
- `list_webex_domains()`
  - Lists the 4 available Webex domains and their endpoint counts.
- `list_webex_categories(domain)`
  - Lists all categories available within a specific domain.

---

## 📁 Repository Structure

```text
mcp-server-webex-docs/
├── docs/                      # Git-versioned Markdown documentation
│   ├── admin.md
│   ├── calling.md
│   ├── meetings.md
│   └── messaging.md
├── data/
│   └── webex_docs.db          # SQLite FTS5 database indexed via SQLAlchemy
├── src/
│   ├── models/                # SQLAlchemy ORM models (Domain, Category, Endpoint)
│   │   ├── __init__.py
│   │   └── db.py
│   ├── pipeline/              # ETL pipeline for automated updates
│   │   ├── __init__.py
│   │   ├── build_all.py       # Main orchestrator CLI
│   │   ├── db_indexer.py      # SQLite FTS5 indexer
│   │   ├── fetcher.py         # Developer portal state extractor
│   │   └── markdown_builder.py# Markdown generator
│   ├── __init__.py
│   └── server.py              # MCP FastMCP server implementation
├── requirements.txt
```

---

## 👨‍💻 Authors & Credits

Built with ❤️ by **[Santiago Meneses Garcia](https://github.com/santime27)**, Software Engineer, in pair-programming collaboration with **Antigravity** (Google DeepMind Agentic AI Assistant).

---

## 📄 License

This project is licensed under the permissive **[MIT License](LICENSE)** — feel free to use, copy, modify, distribute, and build upon this software for both personal and commercial projects without restrictions.


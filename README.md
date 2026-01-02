# FastMCP Beginner MCP Servers

## Overview
This repository is a **beginner-friendly exploration of MCP (Model Context Protocol) servers** built using **FastMCP**. The goal of this project is to understand how to create, run, and validate MCP servers that can later be connected to **AI agents** for practical tasks such as calculations, API access, and data retrieval.

This project focuses on fundamentals:
- Creating MCP-compliant servers
- Exposing tools and resources to AI agents
- Verifying MCP servers using the **official MCP Inspector**
- Understanding different transport methods (stdio, HTTP, SSE)

Each scenario is intentionally simple and educational, making this project ideal for a GitHub portfolio that demonstrates early MCP and AI-agent infrastructure knowledge.

---

## Project Structure
This repository contains **four MCP scenarios**, each showcasing a different way MCP servers can be implemented and tested.

Additionally, supporting notes are included to explain:
- How to run each MCP server
- How to validate functionality using the MCP Inspector
- Common troubleshooting tips

---

## Tools & Technologies Used
- **Python**
- **FastMCP**
- **Model Context Protocol (MCP)**
- **MCP Inspector**
- **HTTP / SSE transports**
- **RSS (XML feeds)**

---

## MCP Inspector (Required for Testing)
All MCP servers in this project are validated using the **official MCP Inspector**:

🔗 https://modelcontextprotocol.io/docs/tools/inspector

### General Command Format
```bash
npx @modelcontextprotocol/inspector <command>
```

Depending on the scenario, the command may be a Python script or a URL endpoint.

---

## Scenario 1: Basic FastMCP Script (Stdio Transport)

### Description
This scenario demonstrates a **basic FastMCP server** running directly from a Python script using **standard input/output (stdio)**. It exposes simple tools (such as a calculator) that an AI agent can call.

### How to Run
```bash
npx @modelcontextprotocol/inspector python fastmcp_calc.py
```

### Key Concepts
- Stdio-based MCP servers
- Tool exposure via FastMCP
- Direct script execution

### Validation
- Launch the MCP Inspector
- Ensure tools appear correctly
- Call exposed tools to verify functionality

---

## Scenario 2: FastMCP Web API (HTTP + SSE Transport)

### Description
This scenario runs a FastMCP server as a **web API**, allowing MCP connections over HTTP using **Server-Sent Events (SSE)**.

### Running the API
Start the server locally (example port shown):
```bash
python fastmcp_api.py
```

If the browser shows **"Not Found"**, navigate to:
```
http://localhost:8002/docs
```

This opens the interactive API documentation.

### MCP Inspector Command
```bash
npx @modelcontextprotocol/inspector http://localhost:8001/mcp
```

### Important Inspector Settings
- **Transport Type:** SSE
- **URL:** Your selected MCP endpoint (e.g., `http://localhost:8001/mcp`)

### Key Concepts
- HTTP-based MCP servers
- SSE transport
- API-style MCP services

---

## Scenario 3: RSS Feed MCP Server

### Description
This scenario uses **RSS (Really Simple Syndication)** feeds to provide structured XML-based updates to an AI agent.

### Data Sources
- Website RSS feeds
- YouTube RSS feed for **freeCodeCamp.org**
  - Channel ID: `UC8butISFwT-Wl7EV0hUK0BQ`

### Purpose
- Demonstrates MCP servers as **information providers**
- Shows how AI agents can consume external XML data

### Key Concepts
- RSS and XML parsing
- Content syndication
- MCP as a data ingestion layer

---

## Scenario 4: Project Aggregation & MCP Registration

### Description
After completing all scenarios, project metadata is collected into a **JSON configuration file**. This file is used to register and manage MCP servers inside an AI development environment.

### VS Code Agent Mode Setup
1. Open **Agent Mode** in VS Code
   - Click the talkbox icon near the top center
2. Select an AI model at the bottom of the agent panel
3. Navigate to:
   ```
   Extensions → MCP Servers → Installed
   ```
4. Right-click your MCP server
5. Select **Start Service**

This allows AI agents to discover and interact with your MCP servers.

---

## Architecture Overview

![Agent to MCP to Tool Diagram (Dark Mode)](docs/agent_mcp_tool_diagram_dark.png)

---

## What This Project Demonstrates
- Practical understanding of MCP fundamentals
- Ability to build MCP servers from scratch
- Knowledge of multiple transport types (stdio, HTTP, SSE)
- Experience validating MCP servers with official tools
- Early-stage AI agent infrastructure development

---

## Why This Matters
MCP is becoming a **core building block for agentic AI systems**. This project shows:
- You understand how AI tools are exposed
- You can wire services into agent workflows
- You are building toward scalable, modular AI systems

For a beginner project, this is exactly the right direction.

---

## Future Improvements
- Add authentication and security layers
- Expand tool complexity
- Integrate databases or vector stores
- Deploy MCP servers remotely
- Connect multiple MCP servers to a single agent

---

## Status
✅ Beginner project completed

This repository represents a **learning-first implementation** of MCP servers and lays the foundation for more advanced AI-agent systems.


# Model Context Protocol (MCP) Security Gateway

A secure client-server architecture built on the Model Context Protocol (MCP), designed with an embedded security inspection layer and automated audit logging.

---

## 🚀 Project Overview

This project implements a secure gateway between an AI Agent (Client) and an MCP Server. It intercepts tool execution requests, performs security inspections (such as Regex-based filtering and pattern matching), logs all actions to an immutable audit trail, and runs fully isolated inside a Docker container.

---

## 🛠️ Key Features

- **Secure Client-Server Communication:** Uses standard I/O (`stdio`) communication over the Model Context Protocol.
- **Multi-Layer Security Inspection:** Intercepts sensitive tool calls (e.g., unauthorized file access like `passwords.txt`) and blocks policy violations instantly.
- **Audit Logging (`audit_log.txt`):** Automatically appends every tool call, arguments, and execution status (`ALLOWED` or `BLOCKED`) with timestamps in an append-only format.
- **Dockerized Environment:** Fully containerized using Docker and `.dockerignore` for seamless cross-platform deployment.

---

## 📂 Project Structure

mcp-security-gateway/
│
├── server.py             # MCP Test Server with security filters and audit logging
├── agent_client.py       # MCP Client Agent executing tool calls
├── Dockerfile            # Container configuration for isolated execution
├── .dockerignore         # Excludes unnecessary files (venv, logs, etc.) from build
└── audit_log.txt         # Generated audit log tracking all gateway events

---

## ⚙️ INSTALLATION & LOCAL SETUP

1. Prerequisites:
   - Python 3.10+
   - Docker Desktop (Optional, for containerized execution)

2. Clone the Repository & Install Dependencies:
   git clone <your-repository-url>
   cd mcp-security-gateway

   # Create and activate virtual environment (Optional)
   python -m venv venv
   # On Windows use: 
   venv\Scripts\Activate.ps1

   # Install required packages
   pip install "mcp<2" fastapi uvicorn requests sentence-transformers

---

## 🧪 RUNNING THE PROJECT

- Running Locally:
  Run the client agent, which automatically initializes the server subprocess:
  python agent_client.py

- Running with Docker:
  1. Build the Docker image:
     docker build -t mcp-security-gateway .
  2. Run the container:
     docker run --rm mcp-security-gateway
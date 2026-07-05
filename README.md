# AI Security Agent

[![CI](https://github.com/kogunlowo123/ai-security-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/ai-security-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: AI Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

AI/ML security agent that performs adversarial testing, model vulnerability assessment, data poisoning detection, model extraction prevention, and security hardening for deployed AI systems.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `red_team_model` | Run adversarial attacks against an AI model to find vulnerabilities |
| `assess_model_security` | Assess model security posture against OWASP LLM Top 10 |
| `detect_data_poisoning` | Detect potential data poisoning in training or fine-tuning data |
| `test_extraction_resistance` | Test model resistance to model extraction attacks |
| `harden_deployment` | Generate security hardening recommendations for AI deployment |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/ai-security/red-team` | Red team model |
| `POST` | `/api/v1/ai-security/assess` | Assess model security |
| `POST` | `/api/v1/ai-security/poisoning` | Detect data poisoning |
| `POST` | `/api/v1/ai-security/extraction` | Test extraction resistance |
| `POST` | `/api/v1/ai-security/harden` | Harden deployment |

## Features

- Adversarial Testing
- Vulnerability Assessment
- Data Poisoning Detection
- Model Extraction Prevention
- Security Hardening

## Integrations

- Garak
- Pyrit
- Counterfit
- Art Ibm
- Openai Moderation

## Architecture

```
ai-security-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── ai_security_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**AI Red Teaming + Adversarial ML + Model Security**

---

Built as part of the Enterprise AI Agent Platform.

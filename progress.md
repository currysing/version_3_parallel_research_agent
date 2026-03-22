# Project Progress Report

## Current Branch
**master** - Main development branch

---

## Latest Update: 2026-03-22

### Model Update: gemini-2.0-flash → gemini-2.5-flash

**Context:** The original configuration used `gemini-2.0-flash` (also aliased as `gemini-flash-latest`) which does not support the `google_search` tool, causing the error:
```
Google search tool is not supported for model gemini-flash-latest
```

**Solution:** Updated all model references to `gemini-2.5-flash` which supports Google Search grounding.

**Files Modified:**

| File | Change |
|------|--------|
| `agents/questions_generator/agent.py` | Model: `gemini-2.0-flash` → `gemini-2.5-flash` |
| `agents/questions_researcher/agent.py` | Model: `gemini-2.0-flash` → `gemini-2.5-flash` (5 sub-agents) |
| `agents/requirements_writer/agent.py` | Model: `gemini-2.0-flash` → `gemini-2.5-flash` |
| `agents/query_generator/agent.py` | Model: `gemini-2.0-flash` → `gemini-2.5-flash` |
| `agents/designer/agent.py` | Model: `gemini-2.0-flash` → `gemini-2.5-flash` |
| `agents/code_writer/agent.py` | Model: `gemini-2.0-flash` → `gemini-2.5-flash` |
| `AGENTS.md` | Documentation updated |

**Total: 12 instances updated**

---

## Project Overview

Multi-agent website builder system using Google's Agent Development Kit (ADK). The project implements a sequential + parallel orchestration pattern where multiple specialized agents collaborate to research topics and generate complete HTML webpages.

---

## Current Architecture

### Agent Pipeline (Sequential)

```
User Input
     ↓
[1] questions_generator_agent (searches topic, generates 5 questions)
     ↓
[2] questions_researcher_agent (5 parallel agents, each searches & answers one question)
     ↓
[3] query_generator_agent (merges research into comprehensive query)
     ↓
[4] requirements_writer_agent (creates detailed webpage requirements)
     ↓
[5] designer_agent (creates visual design specifications)
     ↓
[6] code_writer_agent (generates HTML/CSS/JS, writes to file)
     ↓
Output File
```

### Model Configuration

**Current Provider:** Google Gemini (via Google AI Studio / Vertex AI)

| Metric | Value |
|--------|-------|
| Model | `gemini-2.5-flash` |
| Tools | `google_search` (for research agents) |

### Environment Configuration

**Required `.env` file:**
```
GOOGLE_API_KEY=your-google-api-key
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

---

## Files Structure

```
version_3_parallel_research_agent/
├── agents/
│   ├── root_website_builder/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── description.txt
│   │   └── instructions.txt
│   ├── questions_generator/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── description.txt
│   │   └── instructions.txt
│   ├── questions_researcher/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── description.txt
│   │   └── instructions.txt
│   ├── query_generator/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── description.txt
│   │   └── instructions.txt
│   ├── requirements_writer/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── description.txt
│   │   └── instructions.txt
│   ├── designer/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── description.txt
│   │   └── instructions.txt
│   └── code_writer/
│       ├── __init__.py
│       ├── agent.py
│       ├── description.txt
│       └── instructions.txt
├── tools/
│   └── file_writer_tool.py
├── utils/
│   └── file_loader.py
├── .env
├── .gitignore
├── agent_runner.py
├── main.py
├── pyproject.toml
├── AGENTS.md
└── progress.md
```

---

## Running the Project

### Environment Setup
```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate.bat

# Install dependencies
uv sync --all-groups
```

### Configure API Key
Create `.env` file:
```
GOOGLE_API_KEY=your-google-api-key
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

### Run Agents
```bash
# ADK Web UI (browser-based interface)
adk web ./agents

# ADK CLI Run
adk run agents/root_website_builder

# Programmatic Python Script
uv run python3 -m agent_runner
```

---

## Dependencies

Current `pyproject.toml`:
```toml
[project]
name = "version-2-sequential-website-agent"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "google-adk>=1.3.0",
    "rich>=14.0.0",
]
```

---

## Agent Details

### Agents Using Google Search Tool
| Agent | Uses `google_search` |
|-------|---------------------|
| `questions_generator_agent` | ✅ Yes |
| `questions_researcher_agent` (5 sub-agents) | ✅ Yes |
| `query_generator_agent` | ❌ No |
| `requirements_writer_agent` | ❌ No |
| `designer_agent` | ❌ No |
| `code_writer_agent` | ❌ No |

### Agents Using File Writer Tool
| Agent | Uses `write_to_file` |
|-------|---------------------|
| `code_writer_agent` | ✅ Yes |

---

## History

### 2026-03-22: Model Update
- Changed all `gemini-2.0-flash` to `gemini-2.5-flash`
- Reason: `gemini-2.0-flash` doesn't support `google_search` tool

### Earlier: Initial Setup
- Project created with Google ADK
- Sequential + Parallel agent architecture
- 6 agents in pipeline (5 sequential, 1 parallel with 5 sub-agents)

---

## Known Issues

1. **Windows NUL File**: Sometimes a file named `nul` gets accidentally created on Windows due to incorrect redirection. Delete it if present.

---

## References

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Gemini Model Versions](https://ai.google.dev/gemini-api/docs/models)
- [Google Search Grounding](https://google.github.io/adk-docs/grounding/google_search_grounding/)
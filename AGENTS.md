# AGENTS.md - Guidelines for AI Coding Agents

This document provides guidelines for AI coding agents working in this Google ADK (Agent Development Kit) project.

## Project Overview

This is a multi-agent system using Google's Agent Development Kit. The project provides two main pipelines:

### 1. Website Builder Pipeline (`root_website_builder`)
A sequential + parallel orchestration pattern where multiple specialized agents collaborate to research topics and generate complete HTML webpages.

### 2. Research-Only Pipeline (`research_only_agent`)
A research-focused pipeline that investigates any topic and produces comprehensive Markdown research reports. Does not build websites - focuses purely on information gathering, synthesis, and documentation.

## Available Agents

When running `adk web ./agents`, the following agents are available in the dropdown:

| Agent | Purpose |
|-------|---------|
| `root_website_builder` | Full website building pipeline (6 sequential agents) |
| `research_only` | Research-only pipeline (4 sequential agents) |
| `questions_generator` | Sub-agent: Generates research questions |
| `questions_researcher` | Sub-agent: Parallel research agents |
| `query_generator` | Sub-agent: Synthesizes research |
| `requirements_writer` | Sub-agent: Creates webpage requirements |
| `designer` | Sub-agent: Creates design specifications |
| `code_writer` | Sub-agent: Generates HTML/CSS/JS |
| `research_synthesizer` | Sub-agent: Synthesizes research findings |
| `report_writer` | Sub-agent: Writes Markdown reports |

## Build, Lint, and Test Commands

### Environment Setup
```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate.bat

# Install dependencies
uv sync --all-groups
```

### Running Agents
```bash
# ADK Web UI (browser-based interface)
adk web ./agents

# ADK API Server (REST API)
adk api_server ./agents

# ADK CLI Run (command-line interface)
adk run agents/root_website_builder

# Programmatic Python Script
uv run python3 -m agent_runner
```

### Environment Variables
Create a `.env` file in the project root with:
```
GOOGLE_API_KEY=your-google-api-key
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

### Testing
No formal test framework is configured. When adding tests, consider pytest and add configuration to `pyproject.toml`.

## Code Style Guidelines

### Imports

**Standard library first, then third-party, then local modules:**
```python
# Standard library
import asyncio
import json
import os
import sys
from typing import Any
from pathlib import Path
from dotenv import load_dotenv

# Third-party
from rich import print as rprint
from rich.syntax import Syntax
from google.genai.types import Content, Part
from google.adk.agents import LlmAgent, SequentialAgent, ParallelAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search

# Local modules (use sys.path manipulation for project root imports)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.file_loader import load_instructions_file
from tools.file_writer_tool import write_to_file
```

**Path manipulation pattern for imports:**
```python
# Add project root to path for imports from utils/ and tools/ directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
```

### Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Agent variables | snake_case with `_agent` suffix | `requirements_writer_agent`, `code_writer_agent` |
| Agent names (in ADK) | snake_case with `_agent` suffix | `name="requirements_writer_agent"` |
| Output keys | snake_case with `_output` suffix | `output_key="designer_output"` |
| Functions | snake_case | `load_instructions_file()`, `write_to_file()` |
| Constants | UPPER_SNAKE_CASE | `APP_NAME`, `USER_ID`, `SESSION_ID` |
| Module files | snake_case | `agent.py`, `file_loader.py`, `file_writer_tool.py` |
| Package directories | snake_case | `agents/`, `utils/`, `tools/` |

### Agent Definition Pattern

Each agent follows this standard structure:

```python
"""
File: agents/<agent_name>/agent.py
Purpose: Brief description of what this agent does and its role in the pipeline.

This is the Nth agent in the website building pipeline that:
1. First responsibility
2. Second responsibility
3. Third responsibility
"""

import os
import sys
from google.adk.agents import LlmAgent
from google.adk.tools import google_search  # If using tools

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.file_loader import load_instructions_file

<agent_name>_agent = LlmAgent(
    name="<agent_name>_agent",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/<agent_name>/instructions.txt"),
    description=load_instructions_file("agents/<agent_name>/description.txt"),
    tools=[google_search],  # Optional: include if agent needs tools
    output_key="<agent_name>_output"
)
```

### File Organization

```
project_root/
├── agents/
│   ├── root_website_builder/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── description.txt
│   │   └── instructions.txt
│   ├── research_only/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── description.txt
│   │   └── instructions.txt
│   ├── questions_generator/
│   │   └── ...
│   ├── questions_researcher/
│   │   └── ...
│   ├── query_generator/
│   │   └── ...
│   ├── requirements_writer/
│   │   └── ...
│   ├── designer/
│   │   └── ...
│   ├── code_writer/
│   │   └── ...
│   ├── research_synthesizer/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── description.txt
│   │   └── instructions.txt
│   └── report_writer/
│       ├── __init__.py
│       ├── agent.py
│       ├── description.txt
│       └── instructions.txt
├── tools/
│   ├── file_writer_tool.py
│   └── markdown_writer_tool.py
├── utils/
│   └── file_loader.py
├── output/
│   ├── (website files)
│   └── research/
│       └── .gitkeep
├── main.py
├── agent_runner.py
├── pyproject.toml
└── .env
```

### Type Annotations

Use type hints for function parameters and return types:

```python
def load_instructions_file(filename: str, default: str = "") -> str:
    ...

def write_to_file(content: str) -> dict:
    ...

async def chat_loop() -> None:
    ...
```

### Error Handling

Use try-except with specific exception types and informative messages:

```python
try:
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()
except FileNotFoundError:
    print(f"[WARNING] File not found: {filename}. Using default.")
except Exception as e:
    print(f"[ERROR] Failed to load {filename}: {e}")
return default
```

### Docstrings

Use triple-quoted docstrings for module-level and function documentation:

```python
"""
File: file_loader.py
Purpose:
  Provides a utility function that reads plain text from a file,
  typically for loading prompt instructions or descriptions for LLM agents.
"""

def load_instructions_file(filename: str, default: str = "") -> str:
    """
    Loads instruction or description text from a given file path.

    Args:
        filename (str): Path to the file to read (relative or absolute).
        default (str): Default string to return if file not found.

    Returns:
        str: The file contents if successful, or the fallback default.
    """
```

### Comments

Use section headers with `# ---` delimiters for major code blocks:

```python
# --- 1. SETTING UP IDENTIFIERS (CONSTANTS) ---
APP_NAME = "website_builder_app"

# --- 2. THE MAIN CHAT LOOP FUNCTION ---
async def chat_loop():
    ...

# -----------------------------------------------------------------------------
# Helper: Pretty print JSON objects using syntax coloring
# -----------------------------------------------------------------------------
def print_json_response(response: Any, title: str) -> None:
    ...
```

Use inline comments sparingly, primarily for clarification:

```python
model = "gemini-2.5-flash",  # AI model - Gemini 2.5 Flash for fast responses
```

### Agent Instructions Files

Agent instructions and descriptions are stored in separate `.txt` files within each agent's directory. This separation keeps the Python code clean and allows easy modification of agent behavior without touching code.

### Tools

Tools are Python functions that return dictionaries:

```python
def write_to_file(content: str) -> dict:
    """Writes content to a timestamped HTML file."""
    filename = f"output/{timestamp}_generated_page.html"
    return {"status": "success", "file": filename}
```

### Async Patterns

Use `asyncio` for async operations:

```python
async def chat_loop():
    async for event in events:
        if event.is_final_response():
            ...
            
if __name__ == '__main__':
    asyncio.run(chat_loop())
```

## Key Architecture Patterns

### SequentialAgent
Orchestrates agents that run in sequence, where each agent's output becomes input for the next:

```python
root_agent = SequentialAgent(
    name="root_website_builder_agent",
    sub_agents=[
        questions_generator_agent,
        questions_researcher_agent,
        query_generator_agent,
        requirements_writer_agent,
        designer_agent,
        code_writer_agent
    ],
    description=load_instructions_file("agents/root_website_builder/description.txt")
)
```

### ParallelAgent
Orchestrates multiple agents running concurrently:

```python
parallel_agent = ParallelAgent(
    name="ParallelQuestionsResearchAgent",
    sub_agents=[
        question_researcher_agent_1,
        question_researcher_agent_2,
        # ... more agents
    ],
    description="Runs agents in parallel."
)
```

## Pipeline Architectures

### Website Builder Pipeline (`root_website_builder`)

6-stage sequential pipeline that generates HTML webpages:

```
User Input (Topic)
         ↓
[1] questions_generator_agent (searches topic, generates 5 questions)
         ↓
[2] questions_researcher_agent (5 parallel agents answer each question)
         ↓
[3] query_generator_agent (merges research into comprehensive query)
         ↓
[4] requirements_writer_agent (creates webpage requirements)
         ↓
[5] designer_agent (creates visual design specifications)
         ↓
[6] code_writer_agent (generates HTML/CSS/JS, writes to file)
         ↓
Output: output/{timestamp}_generated_page.html
```

### Research-Only Pipeline (`research_only_agent`)

4-stage sequential pipeline that produces Markdown research reports:

```
User Input (Topic)
         ↓
[1] questions_generator_agent (generates 5 research questions)
         ↓
[2] questions_researcher_agent (5 parallel agents answer each question)
         ↓
[3] research_synthesizer_agent (synthesizes findings, identifies gaps)
         ↓
[4] report_writer_agent (writes formatted Markdown report)
         ↓
Output: output/research/research_report_{timestamp}.md
```

The research-only pipeline reuses the first two stages from the website builder pipeline and adds new agents for synthesis and report generation.

## Common Gotchas

1. **sys.path manipulation**: Required for imports from `utils/` and `tools/` when running agents from subdirectories
2. **Output keys**: Ensure `output_key` names match what downstream agents expect in state access
3. **Async/await**: The ADK Runner uses async methods; use `await` and `async for` appropriately
4. **Environment variables**: Load `.env` file using `dotenv` before accessing environment variables
5. **File encoding**: Always use `encoding="utf-8"` when reading/writing files
6. **Root agent naming**: Pipeline orchestrators must be named `root_agent` (not `<pipeline_name>_agent`) for ADK to discover them
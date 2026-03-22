# AGENTS.md - Guidelines for AI Coding Agents

This document provides guidelines for AI coding agents working in this Google ADK (Agent Development Kit) project.

## Project Overview

This is a multi-agent website builder system using Google's Agent Development Kit. The project implements a sequential + parallel orchestration pattern where multiple specialized agents collaborate to research topics and generate complete HTML webpages.

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
ZAI_API_KEY=your-zhipu-api-key
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
from google.adk.models.lite_llm import LiteLlm
from tools.ddg_search_tool import web_search

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
from google.adk.models.lite_llm import LiteLlm

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.file_loader import load_instructions_file
from tools.ddg_search_tool import web_search  # If using search tool

<agent_name>_agent = LlmAgent(
    name="<agent_name>_agent",
    model=LiteLlm(model="zai/glm-4.7"),  # AI model - Zhipu AI GLM-4.7
    instruction=load_instructions_file("agents/<agent_name>/instructions.txt"),
    description=load_instructions_file("agents/<agent_name>/description.txt"),
    tools=[web_search],  # Optional: include if agent needs search capability
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
│   ├── code_writer/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   └── ...
│   └── ...
├── tools/
│   ├── file_writer_tool.py
│   └── ddg_search_tool.py
├── utils/
│   └── file_loader.py
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
model = "gemini-2.0-flash",  # AI model - Gemini 2.0 Flash for fast responses
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

## Common Gotchas

1. **sys.path manipulation**: Required for imports from `utils/` and `tools/` when running agents from subdirectories
2. **Output keys**: Ensure `output_key` names match what downstream agents expect in state access
3. **Async/await**: The ADK Runner uses async methods; use `await` and `async for` appropriately
4. **Environment variables**: Load `.env` file using `dotenv` before accessing environment variables
5. **File encoding**: Always use `encoding="utf-8"` when reading/writing files
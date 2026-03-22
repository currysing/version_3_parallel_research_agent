# Project Progress Report

## Project Overview
Multi-agent website builder system using Google's Agent Development Kit (ADK). The project implements a sequential + parallel orchestration pattern where multiple specialized agents collaborate to research topics and generate complete HTML webpages.

## Migration History

### 2026-03-22: Gemini to Zhipu AI GLM-4.7 Migration

#### Problem Encountered
The original configuration used `gemini-flash-latest`model which does not support the `google_search` tool, resulting in the error:
```
Google search tool is not supported for model gemini-flash-latest
```

#### Solution Implemented
Migrated from Google Gemini to Zhipu AI GLM-4.7 with DuckDuckGo search替代.

#### Changes Made

##### 1. Dependencies Updated (`pyproject.toml`)
- Added `litellm>=1.0.0` - Required for LiteLLM model connector
- Added `duckduckgo-search>=6.0.0` - For DuckDuckGo web search functionality
- Existing: `google-adk>=1.3.0`, `rich>=14.0.0`

##### 2. New File Created (`tools/ddg_search_tool.py`)
Created custom DuckDuckGo search tool to replace Google Search:
- Function: `web_search(query: str, max_results: int = 5) -> dict`
- Returns formatted search results with title, href, and body
- No API key required
- Privacy-focused search engine

##### 3. Environment Variables (`.env`)
Changed from:
```
GOOGLE_API_KEY=your-google-api-key
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```
To:
```
ZAI_API_KEY=your-zhipu-api-key
```

##### 4. Agent Files Updated

All 6 agent files were updated with:

**Model Change:**
```python
# Before
model="gemini-2.0-flash"

# After
from google.adk.models.lite_llm import LiteLlm
model=LiteLlm(model="zai/glm-4.7")
```

**Search Tool Change (for search-enabled agents):**
```python
# Before
from google.adk.tools import google_search
tools=[google_search]

# After
from tools.ddg_search_tool import web_search
tools=[web_search]
```

**Files Modified:**
| File | Model | Search Tool |
|------|-------|-------------|
| `agents/questions_generator/agent.py` | ✅ Updated | ✅ Updated |
| `agents/questions_researcher/agent.py` | ✅ Updated (5 sub-agents) | ✅ Updated (5 sub-agents) |
| `agents/requirements_writer/agent.py` | ✅ Updated | N/A (no search) |
| `agents/query_generator/agent.py` | ✅ Updated | N/A (no search) |
| `agents/designer/agent.py` | ✅ Updated | N/A (no search) |
| `agents/code_writer/agent.py` | ✅ Updated | N/A (no search) |

##### 5. Documentation Updated (`AGENTS.md`)
- Updated environment variables section
- Updated agent definition pattern examples
- Updated imports to show LiteLLM and DuckDuckGo tool usage
- Updated file organization to include new `ddg_search_tool.py`

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
- **Provider**: Zhipu AI (via LiteLLM)
- **Model**: `zai/glm-4.7`
- **Context Window**: 200K tokens
- **Pricing**: $0.60/1M input, $2.20/1M output

### Search Configuration
- **Tool**: Custom DuckDuckGo search (`web_search`)
- **Default Results**: 5 per query
- **No API Key Required**

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
│   ├── file_writer_tool.py
│   └── ddg_search_tool.py
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
ZAI_API_KEY=your-zhipu-api-key
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

## Technical Details

### LiteLLM Integration
The project uses LiteLLM's wrapper class to connect to Zhipu AI:
```python
from google.adk.models.lite_llm import LiteLlm

model=LiteLlm(model="zai/glm-4.7")
```

This allows using any LiteLLM-supported provider with ADK agents.

### DuckDuckGo Search Tool
Custom implementation that returns structured results:
```python
def web_search(query: str, max_results: int = 5) -> dict:
    # Returns:
    # {
    #     "status": "success",
    #     "query": "...",
    #     "results": [{"title": "...", "href": "...", "body": "..."}]
    # }
```

## Known Issues

1. **Windows Encoding**: When using LiteLLM on Windows, you may encounter `UnicodeDecodeError`. Fix by setting:
   ```powershell
   $env:PYTHONUTF8 = "1"
   ```

2. **NUL File**: A file named `nul` was accidentally created on Windows. This is a reserved device name and should be deleted if present.

## Future Considerations

1. **Model Selection**: Consider `zai/glm-4.5-flash` for free tier (128K context, no cost)
2. **Search Tool**: Could upgrade to Tavily API for AI-optimized search results
3. **Error Handling**: Add retry logic for API failures
4. **Caching**: Consider implementing response caching for repeated queries

## References

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [LiteLLM Documentation](https://docs.litellm.ai/)
- [Zhipu AI API](https://z.ai/)
- [DuckDuckGo Search Library](https://pypi.org/project/duckduckgo-search/)
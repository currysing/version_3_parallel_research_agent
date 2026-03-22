# Project Progress Report

## Current Branch
**research_only_agent** - Feature branch for research-only pipeline

---

## Latest Update: 2026-03-22

### New Feature: Research-Only Pipeline

**Context:** User requested ability to do generic research on any topic without building a website.

**Implementation:** Created a new `research_only` pipeline that:
1. Takes any topic as input
2. Generates and researches 5 questions using Google Search
3. Synthesizes findings into key insights and knowledge gaps
4. Produces a formatted Markdown report with follow-up questions
5. Saves to `output/research/research_report_{timestamp}.md`

**Files Created:**

| File | Purpose |
|------|---------|
| `tools/markdown_writer_tool.py` | Tool for writing Markdown files to `output/research/` |
| `output/research/.gitkeep` | Ensures directory exists in git |
| `agents/research_synthesizer/__init__.py` | Package init |
| `agents/research_synthesizer/agent.py` | Synthesizes research from 5 question researchers |
| `agents/research_synthesizer/description.txt` | Agent description |
| `agents/research_synthesizer/instructions.txt` | Detailed synthesis instructions |
| `agents/report_writer/__init__.py` | Package init |
| `agents/report_writer/agent.py` | Formats and writes Markdown report |
| `agents/report_writer/description.txt` | Agent description |
| `agents/report_writer/instructions.txt` | Report formatting instructions |
| `agents/research_only/__init__.py` | Package init |
| `agents/research_only/agent.py` | SequentialAgent orchestrator (named `root_agent`) |
| `agents/research_only/description.txt` | Agent description |
| `agents/research_only/instructions.txt` | Pipeline orchestration instructions |

**Files Modified:**

| File | Change |
|------|--------|
| `AGENTS.md` | Added pipeline documentation, agent list, file organization |

**Important Fix:** 
- ADK requires root agents to be named `root_agent` (not `<pipeline_name>_agent`)
- Fixed naming convention in `agents/research_only/agent.py` and `__init__.py`

---

## Project Overview

Multi-agent system using Google's Agent Development Kit (ADK). The project now provides **two main pipelines**:

### 1. Website Builder Pipeline (`root_website_builder`)
A sequential + parallel orchestration pattern where multiple specialized agents collaborate to research topics and generate complete HTML webpages.

### 2. Research-Only Pipeline (`research_only`)
A research-focused pipeline that investigates any topic and produces comprehensive Markdown research reports. Does not build websites - focuses purely on information gathering, synthesis, and documentation.

---

## Available Agents

When running `adk web ./agents`, the following agents are available in the dropdown:

| Agent | Purpose |
|-------|---------|
| `root_website_builder` | Full website building pipeline (6 sequential agents) |
| `research_only` | Research-only pipeline (4 sequential agents) |
| `questions_generator` | Sub-agent: Generates research questions |
| `questions_researcher` | Sub-agent: Parallel research agents |
| `query_generator` | Sub-agent: Synthesizes research (website pipeline) |
| `requirements_writer` | Sub-agent: Creates webpage requirements |
| `designer` | Sub-agent: Creates design specifications |
| `code_writer` | Sub-agent: Generates HTML/CSS/JS |
| `research_synthesizer` | Sub-agent: Synthesizes research findings |
| `report_writer` | Sub-agent: Writes Markdown reports |

---

## Current Architecture

### Website Builder Pipeline (`root_website_builder`)

```
User Input (Topic)
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
Output: output/{timestamp}_generated_page.html
```

### Research-Only Pipeline (`research_only`)

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

**Shared Agents:** Both pipelines share `questions_generator_agent` and `questions_researcher_agent`.

---

## Model Configuration

**Current Provider:** Google Gemini (via Google AI Studio / Vertex AI)

| Metric | Value |
|--------|-------|
| Model | `gemini-2.5-flash` |
| Tools | `google_search` (for research agents), `write_to_file` / `write_markdown_file` (for output agents) |

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
# Then select from dropdown:
#   - root_website_builder (for website generation)
#   - research_only (for research reports)

# ADK CLI Run
adk run agents/root_website_builder
adk run agents/research_only

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
| `research_synthesizer_agent` | ❌ No |
| `report_writer_agent` | ❌ No |

### Agents Using File Writer Tools
| Agent | Tool | Output |
|-------|------|--------|
| `code_writer_agent` | `write_to_file` | `output/{timestamp}_generated_page.html` |
| `report_writer_agent` | `write_markdown_file` | `output/research/research_report_{timestamp}.md` |

---

## Research Report Output Format

The research-only pipeline produces Markdown reports with:

```markdown
# Research Report: {Topic}

**Generated:** {timestamp}
**Methodology:** Multi-agent parallel research

---

## Executive Summary
{Brief overview of key findings}

---

## Key Insights
1. {Insight 1}
2. {Insight 2}
...

---

## Detailed Findings

### Question 1: {question}
{Detailed answer with supporting evidence}

{... continued for all 5 questions ...}

---

## Knowledge Gaps
{Areas where more research is needed}

---

## Suggested Follow-up Questions
{Questions for deeper research}

---

## Sources
{List of web sources used}

---

## Methodology
{How the research was conducted}
```

---

## History

### 2026-03-22: Research-Only Pipeline Added
- Created new `research_only` pipeline agent
- Created `research_synthesizer_agent` for synthesizing findings
- Created `report_writer_agent` for Markdown output
- Created `markdown_writer_tool.py` for file writing
- Added `output/research/` directory
- Updated `AGENTS.md` with new pipeline documentation
- Fixed root agent naming convention (`root_agent` vs `<name>_agent`)

### 2026-03-22: Model Update
- Changed all `gemini-2.0-flash` to `gemini-2.5-flash`
- Reason: `gemini-2.0-flash` doesn't support `google_search` tool

### Earlier: Initial Setup
- Project created with Google ADK
- Sequential + Parallel agent architecture
- 6 agents in website pipeline (5 sequential, 1 parallel with 5 sub-agents)

---

## Known Issues

1. **Windows NUL File**: Sometimes a file named `nul` gets accidentally created on Windows due to incorrect redirection. Delete it if present.
2. **Root Agent Naming**: ADK requires pipeline orchestrators to be named `root_agent` (not `<pipeline_name>_agent`) for discovery.

---

## References

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Gemini Model Versions](https://ai.google.dev/gemini-api/docs/models)
- [Google Search Grounding](https://google.github.io/adk-docs/grounding/google_search_grounding/)
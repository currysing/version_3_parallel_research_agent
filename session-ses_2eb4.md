# Create AGENTS.md for codebase

**Session ID:** ses_2eb46cb96ffenUcV0ZC6oeUNiE
**Created:** 3/22/2026, 4:46:15 PM
**Updated:** 3/22/2026, 4:50:26 PM

---

## User

Please analyze this codebase and create an AGENTS.md file containing:
1. Build/lint/test commands - especially for running a single test
2. Code style guidelines including imports, formatting, types, naming conventions, error handling, etc.

The file you create will be given to agentic coding agents (such as yourself) that operate in this repository. Make it about 150 lines long.
If there are Cursor rules (in .cursor/rules/ or .cursorrules) or Copilot rules (in .github/copilot-instructions.md), make sure to include them.

If there's already an AGENTS.md, improve it if it's located in C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent

---

## Assistant (Build · glm-5 · 3.5s)

_Thinking:_

The user wants me to analyze this codebase and create an AGENTS.md file. Let me start by exploring the codebase structure to understand:
1. Build/lint/test commands
2. Code style guidelines
3. Any existing documentation files

I'll need to:
1. Look at package.json or similar build configs
2. Look at existing code to understand conventions
3. Check for .cursor/rules/, .cursorrules, .github/copilot-instructions.md
4. Check if AGENTS.md already exists
5. Look at README and other docs

Let me start by exploring the directory structure andkey files.

I'll analyze the codebase structure and conventions to create an AGENTS.md file.

**Tool: glob**

**Input:**
```json
{
  "pattern": "**/*"
}
```

**Output:**
```
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.git\HEAD
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.git\config
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.git\info\exclude
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.git\hooks\update.sample
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.git\hooks\sendemail-validate.sample
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.git\hooks\push-to-checkout.sample
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.git\hooks\prepare-commit-msg.sample
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.git\hooks\pre-receive.sample
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.git\hooks\pre-rebase.sample
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.git\hooks\pre-push.sample
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.git\hooks\pre-merge-commit.sample
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.git\hooks\pre-commit.sample
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.git\hooks\pre-applypatch.sample
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.git\hooks\post-update.sample
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.git\hooks\fsmonitor-watchman.sample
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.git\hooks\commit-msg.sample
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.git\description
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.git\hooks\applypatch-msg.sample
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\uv.lock
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\utils\file_loader.py
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\tools\file_writer_tool.py
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\pyproject.toml
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\main.py
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\root_website_builder\instructions.txt
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\root_website_builder\description.txt
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\root_website_builder\__init__.py
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\root_website_builder\agent.py
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\requirements_writer\instructions.txt
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\requirements_writer\description.txt
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\requirements_writer\__init__.py
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\requirements_writer\agent.py
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\questions_researcher\instructions.txt
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\questions_researcher\description.txt
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\questions_researcher\agent.py
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\questions_researcher\__init__.py
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\questions_generator\description.txt
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\questions_generator\instructions.txt
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\questions_generator\agent.py
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\query_generator\description.txt
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\query_generator\instructions.txt
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\questions_generator\__init__.py
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\query_generator\agent.py
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\query_generator\__init__.py
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\designer\instructions.txt
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\designer\__init__.py
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\designer\description.txt
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\designer\agent.py
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\code_writer\instructions.txt
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\code_writer\description.txt
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\code_writer\agent.py
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agent_runner.py
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\code_writer\__init__.py
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\README.md
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agent_flow_diagram.md
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.python-version
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.gitignore
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.DS_Store
```

**Tool: glob**

**Input:**
```json
{
  "pattern": "**/package.json"
}
```

**Output:**
```
No files found
```

**Tool: glob**

**Input:**
```json
{
  "pattern": "**/*.md"
}
```

**Output:**
```
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agent_flow_diagram.md
C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\README.md
```

**Tool: glob**

**Input:**
```json
{
  "pattern": ".cursor/**/*"
}
```

**Output:**
```
No files found
```

**Tool: glob**

**Input:**
```json
{
  "pattern": ".cursorrules"
}
```

**Output:**
```
No files found
```

**Tool: glob**

**Input:**
```json
{
  "pattern": ".github/copilot-instructions.md"
}
```

**Output:**
```
No files found
```

---

## Assistant (Build · glm-5 · 3.6s)

_Thinking:_

This is a Python codebase using uv (has uv.lock and pyproject.toml). Let me read the key files to understand:
1. pyproject.toml for build/test/lint commands
2. README.md for project overview
3. Some Python files to understand code conventions

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Projects\\theailanguage\\adk_samples\\version_3_parallel_research_agent\\pyproject.toml"
}
```

**Output:**
```
<path>C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\pyproject.toml</path>
<type>file</type>
<content>1: [project]
2: name = "version-2-sequential-website-agent"
3: version = "0.1.0"
4: description = "Add your description here"
5: readme = "README.md"
6: requires-python = ">=3.11"
7: dependencies = [
8:     "google-adk>=1.3.0",
9:     "rich>=14.0.0",
10: ]

(End of file - total 10 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Projects\\theailanguage\\adk_samples\\version_3_parallel_research_agent\\README.md"
}
```

**Output:**
```
<path>C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\README.md</path>
<type>file</type>
<content>1: # Google ADK Agent Samples
2: 
3: Welcome to The AI Language official repository for Google Agent Development Kit (ADK) sample applications. This collection is designed to provide practical, hands-on examples of how to build powerful and creative agents using the ADK framework.
4: 
5: The goal of this repository is to showcase different architectural patterns—from simple, single-purpose agents to complex, multi-agent systems. Each project is self-contained and includes a detailed `README.md` with specific setup and usage instructions.
6: 
7: ---
8: 
9: ## 🌱 Available Agent Projects
10: 
11: This collection is actively growing. Below are the current agent examples available.
12: 
13: ### 1. Simple Website Builder (`version_1_website_builder_simple`)
14: 
15: *   **Architecture:** Single-Agent System
16: *   **Description:** A minimal ADK application featuring a single LLM-powered agent. It takes a natural language prompt (e.g., "create a page with a blue button") and generates a complete, self-contained HTML file.
17: *   **Best for:** Understanding the fundamentals of an ADK agent, including instructions, tools, and basic I/O.
18: *   **➡️ For detailed instructions, see the `README.md` inside the [`version_1_website_builder_simple/`](./version_1_website_builder_simple/) directory.**
19: 
20: ### 2. Sequential Website Builder (`version_2_sequential_website_agent`)
21: 
22: *   **Architecture:** Multi-Agent, Sequential Orchestration
23: *   **Description:** A more advanced system where a "root" agent orchestrates a team of specialized agents in a sequence to build a website. This mimics a real-world development workflow: `Requirements Writer` -> `Designer` -> `Code Writer`.
24: *   **Best for:** Learning how to build complex workflows by chaining agents together, where the output of one agent becomes the input for the next.
25: *   **➡️ For detailed instructions, see the `README.md` inside the [`version_2_sequential_website_agent/`](./version_2_sequential_website_agent/) directory.**
26: 
27: ### 3. Intelligent Research-Driven Website Builder (`version_3_intelligent_research_website_builder`)
28: 
29: *   **Architecture:** Multi-Agent, Sequential + Parallel Orchestration
30: *   **Description:** An advanced system that combines intelligent research capabilities with parallel processing. Takes a simple topic input and transforms it into a comprehensive research report webpage through a 6-agent pipeline: `Questions Generator` -> `5 Parallel Research Agents` -> `Query Generator` -> `Requirements Writer` -> `Designer` -> `Code Writer`.
31: *   **Best for:** Learning parallel agent execution, Google search integration, research-driven development, and complex multi-agent orchestration with both sequential and parallel patterns.
32: *   **➡️ For detailed instructions, see the `README.md` inside the [`version_3_intelligent_research_website_builder/`](./version_3_intelligent_research_website_builder/) directory.**
33: 
34: We will be adding more agents over time to demonstrate other patterns like parallel execution, agents with memory, and more complex tool usage.
35: 
36: ---
37: 
38: ## 🚀 General Setup Instructions
39: 
40: While each project has its own specific dependencies, the following setup steps are common to all agents in this repository.
41: 
42: ### 1. Clone the Repository
43: 
44: ```bash
45: git clone https://github.com/theailanguage/adk_samples.git
46: ```
47: 
48: ### 2. Set Up Your API Key
49: 
50: To use the agents, you need a Google API key.
51: 
52: 1.  Navigate into the specific project folder you want to run (e.g., `version_2_sequential_website_agent` or `version_3_intelligent_research_website_builder`).
53: 2.  Create a file named `.env` in that directory.
54: 3.  Add your API key to the `.env` file:
55: 
56: ```env
57: GOOGLE_API_KEY=your-google-api-key
58: GOOGLE_GENAI_USE_VERTEXAI=FALSE
59: ```
60: 
61: You can get a free API key from [Google AI Studio](https://makersuite.google.com/app/apikey).
62: 
63: ### 3. Set Up the Python Environment
64: 
65: Each project should be run in its own virtual environment to manage dependencies.
66: 
67: ```bash
68: # Navigate to the project you want to run
69: cd path/to/specific_agent_project
70: 
71: # Create and activate a virtual environment using uv
72: uv venv
73: source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate.bat
74: 
75: # Install the project's dependencies
76: uv sync --all-groups
77: ```
78: 
79: ---
80: 
81: ## 🤖 Running an Agent
82: 
83: After completing the setup for a specific project, you can run its agent(s) using the ADK web interface.
84: 
85: 1.  Make sure you are in the project's root directory in your terminal.
86: 2.  Launch the ADK web server:
87: 
88: ```bash
89: # For projects with a flat agent structure (like v1)
90: cd version_1_website_builder_simple/
91: adk web ./agents
92: 
93: # For projects with a main.py entrypoint (like v2 and v3)
94: cd version_2_sequential_website_agent/
95: adk web ./agents
96: 
97: # For the intelligent research-driven builder (v3)
98: cd version_3_intelligent_research_website_builder/
99: adk web ./agents
100: ```
101: 
102: 3.  Open your browser and go to `http://localhost:8000`.
103: 4.  Select the desired agent from the dropdown menu and start interacting with it!
104: 
105: ---
106: 
107: ### **Four Ways to Run Your ADK Agent**
108: 
109: | S.No. | Method & Command | Description | When to Use |
110: |------:|------------------|-------------|-------------|
111: | 1 | **ADK Web**  <br>`adk web ./agents` | - Launches a browser-based UI | - Ideal for debugging or quick demos |
112: | 2 | **ADK API Server** <br>`adk api_server ./agents` | - Starts an HTTP API server | - Useful for REST API-based automation. |
113: | 3 | **Programmatic Python Script** <br>`uv run python3 -m agent_runner` | - Fully code-driven interaction using Python and the ADK SDK | - Ideal for building your own CLI tools or backend pipelines |
114: | 4 | **ADK CLI Run** <br>`adk run agents/root_website_builder` | - Command-line way to run a specific agent directly | - Great for quick runs or testing |
115: 
116: ---
117: 
118: ## 📜 License
119: 
120: This repository and the code within are licensed under the **GNU General Public License v3.0**. See the `LICENSE` file for full details.

(End of file - total 120 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Projects\\theailanguage\\adk_samples\\version_3_parallel_research_agent\\main.py"
}
```

**Output:**
```
<path>C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\main.py</path>
<type>file</type>
<content>1: def main():
2:     print("Hello from version-2-sequential-website-agent!")
3: 
4: 
5: if __name__ == "__main__":
6:     main()

(End of file - total 6 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Projects\\theailanguage\\adk_samples\\version_3_parallel_research_agent\\agent_runner.py"
}
```

**Output:**
```
<path>C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agent_runner.py</path>
<type>file</type>
<content>1: # --- A. IMPORTING THE NECESSARY TOOLS ---
2: # 'asyncio' is a Python library that helps run multiple tasks at the same time.
3: import asyncio
4: import json
5: from typing import Any
6: from rich import print as rprint    # Enhanced print function to support colors and formatting
7: from rich.syntax import Syntax      # Used to highlight JSON output in the terminal
8: 
9: # These are specific classes from Google's AI library for structuring messages.
10: from google.genai.types import Content, Part
11: 
12: from dotenv import load_dotenv
13: load_dotenv()
14: 
15: # --- B. IMPORTING OUR AGENT ---
16: # We are importing the "brain" of our AI agent from our project.
17: from agents.root_website_builder.agent import root_agent
18: 
19: # --- C. IMPORTING ADK (AGENT DEVELOPMENT KIT) COMPONENTS ---
20: # These are special tools from the ADK to run our agent programmatically.
21: from google.adk.runners import Runner
22: from google.adk.sessions import InMemorySessionService
23: 
24: # --- 1. SETTING UP IDENTIFIERS (CONSTANTS) ---
25: # We define constant text variables to identify our application and conversation.
26: APP_NAME = "website_builder_app"
27: USER_ID = "user_12345"
28: SESSION_ID = "session_chat_loop_1" # A unique ID for this entire chat session.
29: 
30: # --- 2. THE MAIN CHAT LOOP FUNCTION ---
31: # This async function will set everything up once, then loop to allow for continuous chat.
32: async def chat_loop():
33:     """
34:     Initializes the agent and session, then enters a loop to
35:     continuously accept user queries and provide agent responses.
36:     """
37:     print("Agent Chat Session Started.")
38:     print("Type 'quit', 'exit', or ':q' to end the session.\n")
39: 
40:     # --- SETUP (Done Once) ---
41:     # The Session Service stores the conversation history (memory).
42:     session_service = InMemorySessionService()
43:     # We create the session object that will be used for the entire chat.
44:     session = await session_service.create_session(
45:         app_name=APP_NAME,
46:         user_id=USER_ID,
47:         session_id=SESSION_ID
48:     )
49: 
50:     # The Runner is the engine that executes the agent's logic.
51:     runner = Runner(
52:         agent=root_agent,
53:         app_name=APP_NAME,
54:         session_service=session_service,
55:     )
56: 
57:     # --- THE INTERACTIVE LOOP ---
58:     # This 'while True' loop will run indefinitely until the user decides to quit.
59:     while True:
60:         # Prompt the user for their next message.
61:         user_query = input("Enter your query: ")
62: 
63:         # Check if the user wants to exit the chat.
64:         # .lower() makes the text lowercase so "Quit" or "QUIT" also work.
65:         if user_query.lower() in ["quit", "exit", ":q"]:
66:             print("Ending chat session. Goodbye!")
67:             break  # This command exits the 'while' loop.
68: 
69:         # --- Agent Interaction (Inside the Loop) ---
70:         # Format the user's query into the structure the agent understands.
71:         new_message = Content(role="user", parts=[Part(text=user_query)])
72: 
73:         # The runner.run_async() method sends the message and gets a stream of events back.
74:         # Because we are using the SAME runner and session IDs each time, the agent
75:         # remembers the previous parts of the conversation.
76:         events = runner.run_async(
77:             user_id=USER_ID,
78:             session_id=SESSION_ID,
79:             new_message=new_message
80:         )
81: 
82:         # --- Process the Event Stream ---
83:         # We loop through the agent's "thinking steps" (events) to find the final answer.
84:         final_response = ""
85:         i = 0
86:         async for event in events:
87:             i+= 1  # Increment the event counter
88:             # Print each event as it comes in, with a title for clarity.
89:             # This helps us see the agent's thought process step-by-step.
90:             print_json_response(event, f"============Event #{i}=============")
91: 
92:             if hasattr(event, "author") and event.author == "code_writer_agent":
93: 
94:                 if event.is_final_response():
95:                     # If the event is a final response, we extract the text.
96:                     # This is the agent's final answer to the user's query.
97:                     final_response = event.content.parts[0].text
98:                     # Print a clean separation for the agent's response.
99:                     print(f"\nAgent Response:\n------------------------\n{final_response}\n")
100:                     break # Stop processing events once we have the final answer.
101: 
102: 
103: 
104: # -----------------------------------------------------------------------------
105: # Helper: Pretty print JSON objects using syntax coloring
106: # -----------------------------------------------------------------------------
107: def print_json_response(response: Any, title: str) -> None:
108:     # Displays a formatted and color-highlighted view of the response
109:     print(f"\n=== {title} ===")  # Section title for clarity
110:     try:
111:         if hasattr(response, "root"):  # Check if response is wrapped by SDK
112:             data = response.root.model_dump(mode="json", exclude_none=True)
113:         else:
114:             data = response.model_dump(mode="json", exclude_none=True)
115: 
116:         json_str = json.dumps(data, indent=2, ensure_ascii=False)  # Convert dict to pretty JSON string
117:         syntax = Syntax(json_str, "json", theme="monokai", line_numbers=False)  # Apply syntax highlighting
118:         rprint(syntax)  # Print it with color
119:     except Exception as e:
120:         # Print fallback text if something fails
121:         rprint(f"[red bold]Error printing JSON:[/red bold] {e}")
122:         rprint(repr(response))
123: 
124: 
125: # --- 3. STARTING THE PROGRAM ---
126: # This is the entry point that runs our chat loop.
127: if __name__ == '__main__':
128:     asyncio.run(chat_loop())

(End of file - total 128 lines)
</content>
```

---

## Assistant (Build · glm-5 · 3.3s)

_Thinking:_

Let me read more agent files to understand the code style and conventions better.

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Projects\\theailanguage\\adk_samples\\version_3_parallel_research_agent\\agents\\root_website_builder\\agent.py"
}
```

**Output:**
```
<path>C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\root_website_builder\agent.py</path>
<type>file</type>
<content>1: import os
2: import sys
3: from google.adk.agents import SequentialAgent
4: 
5: sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..")))
6: from utils.file_loader import load_instructions_file
7: from agents.questions_generator.agent import questions_generator_agent
8: from agents.questions_researcher.agent import questions_researcher_agent
9: from agents.query_generator.agent import query_generator_agent
10: from agents.requirements_writer.agent import requirements_writer_agent
11: from agents.designer.agent import designer_agent
12: from agents.code_writer.agent import code_writer_agent
13: 
14: root_agent = SequentialAgent(
15:     name="root_website_builder_agent",
16:     sub_agents=[
17:         questions_generator_agent,
18:         questions_researcher_agent,
19:         query_generator_agent,
20:         requirements_writer_agent,
21:         designer_agent,
22:         code_writer_agent
23:     ],
24:     description=load_instructions_file("agents/root_website_builder/description.txt")
25: )

(End of file - total 25 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Projects\\theailanguage\\adk_samples\\version_3_parallel_research_agent\\agents\\code_writer\\agent.py"
}
```

**Output:**
```
<path>C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\code_writer\agent.py</path>
<type>file</type>
<content>1: """
2: File: agents/code_writer/agent.py
3: Purpose: Defines the Code Writer Agent that transforms visual design specifications into
4:          complete, functional HTML/CSS/JavaScript code. This agent acts as a skilled
5:          front-end developer, implementing the design system and specifications into
6:          a single-file webpage that matches the original requirements exactly.
7: 
8: This is the sixth and final agent in the website building pipeline that:
9: 1. Receives detailed design specifications from the designer agent
10: 2. Implements the global design system (colors, typography, spacing) in CSS
11: 3. Converts design specifications into semantic HTML structure
12: 4. Adds interactive functionality with JavaScript where needed
13: 5. Writes the complete webpage to a file using the file_writer_tool
14: """
15: 
16: # Import required system modules for path manipulation
17: import os  # Operating system interface for file paths
18: import sys  # System-specific parameters and functions
19: 
20: # Import the main LlmAgent class from Google ADK (Agent Development Kit)
21: from google.adk.agents import LlmAgent  # Core agent class for creating LLM-based agents
22: 
23: # Add the project root directory to Python path so we can import utility modules
24: # This allows importing from the utils directory two levels up from current file
25: sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..")))
26: 
27: # Import utility function to load instruction files from text files
28: from utils.file_loader import load_instructions_file  # Helper to read instruction text files
29: 
30: # Import the file writing tool that allows the agent to save the generated webpage
31: from tools.file_writer_tool import write_to_file  # Custom tool for writing HTML files to disk
32: 
33: # Create the Code Writer Agent instance
34: code_writer_agent = LlmAgent(
35:     # Agent identifier - unique name for this agent in the system
36:     name = "code_writer_agent",
37:     
38:     # AI model to use - Gemini 2.5 Flash for sophisticated code generation and implementation
39:     # Uses 2.5 for advanced HTML/CSS/JS generation and design system implementation
40:     model = "gemini-flash-latest",
41:     
42:     # Load detailed instructions from external text file
43:     # Instructions contain systematic approach for converting design specs to working code
44:     # Includes guidelines for semantic HTML, responsive CSS, and interactive JavaScript
45:     instruction=load_instructions_file("agents/code_writer/instructions.txt"),
46:     
47:     # Load agent description from external text file
48:     # Provides a brief summary of this agent's front-end developer role
49:     description=load_instructions_file("agents/code_writer/description.txt"),
50:     
51:     # Tools available to this agent - file writing capability for saving the generated webpage
52:     # The write_to_file tool allows the agent to save the complete HTML/CSS/JS to disk
53:     tools=[write_to_file],
54:     
55:     # No output_key needed - this is the final agent that produces the actual webpage file
56:     # The file_writer_tool handles the final output by writing directly to the filesystem
57: )

(End of file - total 57 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Projects\\theailanguage\\adk_samples\\version_3_parallel_research_agent\\agents\\designer\\agent.py"
}
```

**Output:**
```
<path>C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\designer\agent.py</path>
<type>file</type>
<content>1: """
2: File: agents/designer/agent.py
3: Purpose: Defines the Designer Agent that transforms detailed webpage requirements into
4:          comprehensive visual design specifications. This agent acts as a pragmatic
5:          UI/UX designer, converting functional requirements into concrete design
6:          guidelines that developers can implement without ambiguity.
7: 
8: This is the fifth agent in the website building pipeline that:
9: 1. Receives detailed requirements from the requirements_writer agent
10: 2. Establishes a global design system (colors, typography, spacing)
11: 3. Translates requirements into specific visual design specifications
12: 4. Creates section-by-section design details with exact values
13: 5. Outputs structured design specifications for the code_writer agent
14: """
15: 
16: # Import required system modules for path manipulation
17: import os  # Operating system interface for file paths
18: import sys  # System-specific parameters and functions
19: 
20: # Import the main LlmAgent class from Google ADK (Agent Development Kit)
21: from google.adk.agents import LlmAgent  # Core agent class for creating LLM-based agents
22: 
23: # Add the project root directory to Python path so we can import utility modules
24: # This allows importing from the utils directory two levels up from current file
25: sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..")))
26: 
27: # Import utility function to load instruction files from text files
28: from utils.file_loader import load_instructions_file  # Helper to read instruction text files
29: 
30: # Create the Designer Agent instance
31: designer_agent = LlmAgent(
32:     # Agent identifier - unique name for this agent in the system
33:     name = "designer_agent",
34:     
35:     # AI model to use - Gemini 2.5 Flash for sophisticated design analysis and specification
36:     # Uses 2.5 for advanced visual design reasoning and systematic design system creation
37:     model = "gemini-flash-latest",
38:     
39:     # Load detailed instructions from external text file
40:     # Instructions contain systematic approach for creating design systems and visual specs
41:     # Includes step-by-step logic for translating requirements to concrete design values
42:     instruction=load_instructions_file("agents/designer/instructions.txt"),
43:     
44:     # Load agent description from external text file
45:     # Provides a brief summary of this agent's UI/UX designer role
46:     description=load_instructions_file("agents/designer/description.txt"),
47:     
48:     # No tools needed - this agent works with pure design analysis and specification generation
49:     # It processes requirements from requirements_writer without external API calls
50:     
51:     # Output key - where this agent stores the design specifications in the session state
52:     # The code_writer agent will reference this key to get the detailed design guidelines
53:     output_key="designer_output"
54: )

(End of file - total 54 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Projects\\theailanguage\\adk_samples\\version_3_parallel_research_agent\\tools\\file_writer_tool.py"
}
```

**Output:**
```
<path>C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\tools\file_writer_tool.py</path>
<type>file</type>
<content>1: # =============================================================================
2: # FILE: file_writer_tool.py
3: # PURPOSE:
4: #   This module defines a single tool function, `write_to_file`, which saves
5: #   the provided HTML/CSS/JS content to a timestamped HTML file inside an
6: #   output directory. This is used by agents to persist generated webpage content.
7: # =============================================================================
8: 
9: # Import the `datetime` module to generate a unique timestamp for the filename.
10: import datetime
11: 
12: # Import `Path` from `pathlib` for convenient and safe file/directory handling.
13: from pathlib import Path
14: 
15: # -----------------------------------------------------------------------------
16: # TOOL FUNCTION: write_to_file
17: # -----------------------------------------------------------------------------
18: def write_to_file(content: str) -> dict:
19:     """
20:     Writes the given HTML/CSS/JS content to a timestamped HTML file.
21: 
22:     Args:
23:         content (str): Full HTML content as a string to be saved to disk.
24: 
25:     Returns:
26:         dict: A dictionary containing the status and generated filename.
27:     """
28: 
29:     # Get the current date and time, format it as YYMMDD_HHMMSS.
30:     # Example: "250611_142317"
31:     timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
32: 
33:     # Construct the output filename using the timestamp.
34:     # Example: "output/250611_142317_generated_page.html"
35:     filename = f"output/{timestamp}_generated_page.html"
36: 
37:     # Ensure the "output" directory exists. If it doesn’t, create it.
38:     # `exist_ok=True` prevents an error if the directory already exists.
39:     Path("output").mkdir(exist_ok=True)
40: 
41:     # Write the HTML content to the constructed file.
42:     # `encoding='utf-8'` ensures proper character encoding.
43:     Path(filename).write_text(content, encoding="utf-8")
44: 
45:     # Return a dictionary indicating success, and the filename that was written.
46:     return {
47:         "status": "success",
48:         "file": filename
49:     }

(End of file - total 49 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Projects\\theailanguage\\adk_samples\\version_3_parallel_research_agent\\utils\\file_loader.py"
}
```

**Output:**
```
<path>C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\utils\file_loader.py</path>
<type>file</type>
<content>1: # =============================================================================
2: # FILE: file_loader.py
3: # PURPOSE:
4: #   Provides a utility function `load_instructions_file` that reads plain text
5: #   from a file — typically used to load prompt instructions or descriptions
6: #   for LLM agents. If the file is not found or unreadable, a default string is returned.
7: # =============================================================================
8: 
9: # Import the `os` module for working with file paths and environment context (not used here but common in loaders).
10: import os
11: 
12: # -----------------------------------------------------------------------------
13: # FUNCTION: load_instructions_file
14: # -----------------------------------------------------------------------------
15: def load_instructions_file(filename: str, default: str = "") -> str:
16:     """
17:     Loads instruction or description text from a given file path.
18: 
19:     Args:
20:         filename (str): Path to the file to read (relative or absolute).
21:         default (str): Default string to return if the file is not found or fails to load.
22: 
23:     Returns:
24:         str: The file contents if successful, or the fallback default string.
25:     """
26: 
27:     try:
28:         # Attempt to open the file in read mode with UTF-8 encoding.
29:         # This ensures support for non-ASCII characters in prompt files.
30:         with open(filename, "r", encoding="utf-8") as f:
31:             return f.read()  # Read and return the entire contents of the file.
32: 
33:     except FileNotFoundError:
34:         # If the file doesn't exist, log a warning and fall back to the default value.
35:         print(f"[WARNING] File not found: {filename}. Using default.")
36: 
37:     except Exception as e:
38:         # Catch any other exception (e.g. permission issues, IO errors) and log it.
39:         print(f"[ERROR] Failed to load {filename}: {e}")
40: 
41:     # Return the fallback default string if anything goes wrong.
42:     return default

(End of file - total 42 lines)
</content>
```

---

## Assistant (Build · glm-5 · 2.9s)

_Thinking:_

Now let me read more agents to understand the full pattern, and also check for any instructions files.

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Projects\\theailanguage\\adk_samples\\version_3_parallel_research_agent\\agents\\questions_researcher\\agent.py"
}
```

**Output:**
```
<path>C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\questions_researcher\agent.py</path>
<type>file</type>
<content>1: """
2: File: agents/questions_researcher/agent.py
3: Purpose: Defines the Questions Researcher Agent system that contains five specialized LLM agents
4:          running in parallel to research and answer the five questions generated by the 
5:          questions_generator agent. Each sub-agent focuses on researching one specific question
6:          using Google search to provide comprehensive, well-researched answers.
7: 
8: This is the second agent in the website building pipeline that:
9: 1. Receives 5 questions from questions_generator_output
10: 2. Runs 5 specialized agents in parallel (one per question)
11: 3. Each agent researches its assigned question using Google search
12: 4. Outputs 5 separate research results for the query_generator to merge
13: """
14: 
15: # Import required system modules for path manipulation
16: import os  # Operating system interface for file paths
17: import sys  # System-specific parameters and functions
18: 
19: # Import agent classes from Google ADK (Agent Development Kit)
20: from google.adk.agents import LlmAgent, ParallelAgent  # LlmAgent for individual agents, ParallelAgent for orchestration
21: 
22: # Import Google search tool that allows agents to perform web searches
23: from google.adk.tools import google_search  # Pre-built tool for Google search functionality
24: 
25: # Add the project root directory to Python path so we can import utility modules
26: # This allows importing from the utils directory two levels up from current file
27: sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..")))
28: 
29: # Import utility function to load instruction files from text files
30: from utils.file_loader import load_instructions_file  # Helper to read instruction text files
31: 
32: # Load shared instructions and description that will be used by all 5 sub-agents
33: # These files contain the common behavior and guidelines for question research
34: base_instructions = load_instructions_file("agents/questions_researcher/instructions.txt")  # Common research instructions
35: base_description = load_instructions_file("agents/questions_researcher/description.txt")    # Common agent description
36: 
37: # --- 1. Define Question Researcher Sub-Agents (to run in parallel) ---
38: # Each agent is specialized to handle exactly one question from the list of 5 questions
39: # They all share the same base instructions but are assigned different question numbers
40: 
41: # Question Researcher 1 - Handles the first question from the questions list
42: question_researcher_agent_1 = LlmAgent(
43:     name="QuestionResearcher1",  # Unique identifier for this specific researcher
44:     model="gemini-flash-latest",    # AI model - Gemini 2.0 Flash for fast, high-quality responses
45:     # Combine question assignment with base instructions using f-string formatting
46:     instruction=f"You are assigned to answer QUESTION NUMBER 1 only.\n\n{base_instructions}",
47:     # Combine base description with specific role information
48:     description=f"{base_description} This agent specifically handles question #1.",
49:     tools=[google_search],  # Google search tool for researching the assigned question
50:     # Unique output key where this agent stores its research results
51:     output_key="question_1_research_output"
52: )
53: 
54: # Question Researcher 2 - Handles the second question from the questions list
55: question_researcher_agent_2 = LlmAgent(
56:     name="QuestionResearcher2",  # Unique identifier for this specific researcher
57:     model="gemini-flash-latest",    # AI model - Gemini 2.0 Flash for fast, high-quality responses
58:     # Combine question assignment with base instructions using f-string formatting
59:     instruction=f"You are assigned to answer QUESTION NUMBER 2 only.\n\n{base_instructions}",
60:     # Combine base description with specific role information
61:     description=f"{base_description} This agent specifically handles question #2.",
62:     tools=[google_search],  # Google search tool for researching the assigned question
63:     # Unique output key where this agent stores its research results
64:     output_key="question_2_research_output"
65: )
66: 
67: # Question Researcher 3 - Handles the third question from the questions list
68: question_researcher_agent_3 = LlmAgent(
69:     name="QuestionResearcher3",  # Unique identifier for this specific researcher
70:     model="gemini-flash-latest",    # AI model - Gemini 2.0 Flash for fast, high-quality responses
71:     # Combine question assignment with base instructions using f-string formatting
72:     instruction=f"You are assigned to answer QUESTION NUMBER 3 only.\n\n{base_instructions}",
73:     # Combine base description with specific role information
74:     description=f"{base_description} This agent specifically handles question #3.",
75:     tools=[google_search],  # Google search tool for researching the assigned question
76:     # Unique output key where this agent stores its research results
77:     output_key="question_3_research_output"
78: )
79: 
80: # Question Researcher 4 - Handles the fourth question from the questions list
81: question_researcher_agent_4 = LlmAgent(
82:     name="QuestionResearcher4",  # Unique identifier for this specific researcher
83:     model="gemini-flash-latest",    # AI model - Gemini 2.0 Flash for fast, high-quality responses
84:     # Combine question assignment with base instructions using f-string formatting
85:     instruction=f"You are assigned to answer QUESTION NUMBER 4 only.\n\n{base_instructions}",
86:     # Combine base description with specific role information
87:     description=f"{base_description} This agent specifically handles question #4.",
88:     tools=[google_search],  # Google search tool for researching the assigned question
89:     # Unique output key where this agent stores its research results
90:     output_key="question_4_research_output"
91: )
92: 
93: # Question Researcher 5 - Handles the fifth question from the questions list
94: question_researcher_agent_5 = LlmAgent(
95:     name="QuestionResearcher5",  # Unique identifier for this specific researcher
96:     model="gemini-flash-latest",    # AI model - Gemini 2.0 Flash for fast, high-quality responses
97:     # Combine question assignment with base instructions using f-string formatting
98:     instruction=f"You are assigned to answer QUESTION NUMBER 5 only.\n\n{base_instructions}",
99:     # Combine base description with specific role information
100:     description=f"{base_description} This agent specifically handles question #5.",
101:     tools=[google_search],  # Google search tool for researching the assigned question
102:     # Unique output key where this agent stores its research results
103:     output_key="question_5_research_output"
104: )
105: 
106: # --- 2. Create the ParallelAgent (Runs all question researchers concurrently) ---
107: # ParallelAgent orchestrates the concurrent execution of all five question researchers
108: # This significantly reduces total execution time compared to running them sequentially
109: # The parallel agent completes when ALL sub-agents have finished their research
110: parallel_questions_researcher_agent = ParallelAgent(
111:     name="ParallelQuestionsResearchAgent",  # Identifier for the parallel orchestrator
112:     # List of all 5 sub-agents that will run simultaneously
113:     sub_agents=[
114:         question_researcher_agent_1,  # Researcher for question 1
115:         question_researcher_agent_2,  # Researcher for question 2
116:         question_researcher_agent_3,  # Researcher for question 3
117:         question_researcher_agent_4,  # Researcher for question 4
118:         question_researcher_agent_5   # Researcher for question 5
119:     ],
120:     # Description of what this parallel agent accomplishes
121:     description="Runs five question research agents in parallel to research and answer all five questions simultaneously."
122: )
123: 
124: # Set the main export variable to the parallel agent
125: # This is what gets imported when other modules import from this file
126: # The parallel agent becomes the single entry point that manages all 5 researchers
127: questions_researcher_agent = parallel_questions_researcher_agent

(End of file - total 127 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Projects\\theailanguage\\adk_samples\\version_3_parallel_research_agent\\agents\\questions_generator\\agent.py"
}
```

**Output:**
```
<path>C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\questions_generator\agent.py</path>
<type>file</type>
<content>1: """
2: File: agents/questions_generator/agent.py
3: Purpose: Defines the Questions Generator Agent that takes a user-provided topic and generates 
4:          five important questions to help understand that topic. This agent uses Google search 
5:          to research the topic before generating informed questions.
6: 
7: This is the first agent in the website building pipeline that:
8: 1. Receives a topic from the user
9: 2. Researches the topic using Google search
10: 3. Generates exactly 5 questions that help understand the topic
11: 4. Outputs the questions for the questions_researcher agents to answer
12: """
13: 
14: # Import required system modules for path manipulation
15: import os  # Operating system interface for file paths
16: import sys  # System-specific parameters and functions
17: 
18: # Import the main LlmAgent class from Google ADK (Agent Development Kit)
19: from google.adk.agents import LlmAgent  # Core agent class for creating LLM-based agents
20: 
21: # Import Google search tool that allows the agent to perform web searches
22: from google.adk.tools import google_search  # Pre-built tool for Google search functionality
23: 
24: # Add the project root directory to Python path so we can import utility modules
25: # This allows importing from the utils directory two levels up from current file
26: sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..")))
27: 
28: # Import utility function to load instruction files from text files
29: from utils.file_loader import load_instructions_file  # Helper to read instruction text files
30: 
31: # Create the Questions Generator Agent instance
32: questions_generator_agent = LlmAgent(
33:     # Agent identifier - unique name for this agent in the system
34:     name = "questions_generator_agent",
35:     
36:     # AI model to use - Gemini 2.0 Flash for fast, high-quality responses
37:     model = "gemini-flash-latest",
38:     
39:     # Load detailed instructions from external text file
40:     # This keeps the code clean and allows easy modification of agent behavior
41:     instruction=load_instructions_file("agents/questions_generator/instructions.txt"),
42:     
43:     # Load agent description from external text file
44:     # Provides a brief summary of what this agent does
45:     description=load_instructions_file("agents/questions_generator/description.txt"),
46:     
47:     # Tools available to this agent - Google search for researching topics
48:     # This allows the agent to gather current information before generating questions
49:     tools=[google_search],
50:     
51:     # Output key - where this agent stores its results in the session state
52:     # Other agents in the pipeline will reference this key to access the generated questions
53:     output_key="questions_generator_output"
54: )

(End of file - total 54 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Projects\\theailanguage\\adk_samples\\version_3_parallel_research_agent\\agents\\requirements_writer\\agent.py"
}
```

**Output:**
```
<path>C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\requirements_writer\agent.py</path>
<type>file</type>
<content>1: """
2: File: agents/requirements_writer/agent.py
3: Purpose: Defines the Requirements Writer Agent that transforms a comprehensive, research-based
4:          query into detailed webpage requirements. This agent acts as an expert technical 
5:          business analyst, converting high-level concepts into specific, actionable 
6:          requirements that developers and designers can use to build webpages.
7: 
8: This is the fourth agent in the website building pipeline that:
9: 1. Receives a comprehensive, research-backed query from the query_generator
10: 2. Analyzes the query to identify webpage type and core purpose
11: 3. Breaks down requirements into logical webpage components (Header, Hero, Content, Footer)
12: 4. Defines global requirements (responsiveness, accessibility, SEO)
13: 5. Outputs structured Markdown requirements for the designer agent
14: """
15: 
16: # Import required system modules for path manipulation
17: import os  # Operating system interface for file paths
18: import sys  # System-specific parameters and functions
19: 
20: # Import the main LlmAgent class from Google ADK (Agent Development Kit)
21: from google.adk.agents import LlmAgent  # Core agent class for creating LLM-based agents
22: 
23: # Add the project root directory to Python path so we can import utility modules
24: # This allows importing from the utils directory two levels up from current file
25: sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..")))
26: 
27: # Import utility function to load instruction files from text files
28: from utils.file_loader import load_instructions_file  # Helper to read instruction text files
29: 
30: # Create the Requirements Writer Agent instance
31: requirements_writer_agent = LlmAgent(
32:     # Agent identifier - unique name for this agent in the system
33:     name = "requirements_writer_agent",
34:     
35:     # AI model to use - Gemini 2.5 Flash for detailed requirement analysis and generation
36:     # Note: This uses 2.5 instead of 2.0 for more sophisticated requirement writing
37:     model = "gemini-flash-latest",
38:     
39:     # Load detailed instructions from external text file
40:     # Instructions contain systematic approach for converting queries to webpage requirements
41:     # Includes step-by-step logic for analyzing queries and structuring requirements
42:     instruction=load_instructions_file("agents/requirements_writer/instructions.txt"),
43:     
44:     # Load agent description from external text file
45:     # Provides a brief summary of this agent's technical business analyst role
46:     description=load_instructions_file("agents/requirements_writer/description.txt"),
47:     
48:     # No tools needed - this agent works with pure text analysis and requirement generation
49:     # It processes the merged query from query_generator without external API calls
50:     
51:     # Output key - where this agent stores the detailed requirements in the session state
52:     # The designer agent will reference this key to get the structured requirements document
53:     output_key="requirements_writer_output"
54: )

(End of file - total 54 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Projects\\theailanguage\\adk_samples\\version_3_parallel_research_agent\\agents\\code_writer\\instructions.txt"
}
```

**Output:**
```
<path>C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\code_writer\instructions.txt</path>
<type>file</type>
<content>1: You are the "Code Writer Agent." You are a meticulous and efficient front-end developer. Your sole purpose is to synthesize two documents—a requirements list and a design specification—into a single, working HTML file. You do not get creative or deviate from the instructions. Your output must be a single block of code, which will be passed to a file_writer tool.
2: 
3: Inputs
4: Requirements Document: state['requirements_writer_output']
5: Design Specification: state['designer_output']
6: 
7: Core Principles
8: Strict Adherence: Your output must be a direct and faithful implementation of the provided inputs. The structure, sections, and content placeholders are dictated by requirements writer output. The visual appearance (colors, fonts, spacing, layout) is dictated entirely by designer output.
9: Single File Mandate: All code—HTML, CSS, and JavaScript—must be contained within a single .html file. This means all CSS will be placed within a <style> tag in the <head>, and all JavaScript will be placed within a <script> tag just before the closing </body> tag.
10: Clean, Semantic Code: Write well-formatted, indented code. Use semantic HTML5 tags (<header>, <nav>, <main>, <section>, <footer>, etc.) as specified in the requirements. Add comments in the code to delineate the major sections.
11: Vanilla JavaScript Only: Use standard, browser-compatible vanilla JavaScript for any required interactivity (e.g., mobile menu toggling, smooth scrolling). Do not use any external libraries or frameworks like jQuery, React, or Vue.
12: Tool-Oriented Output: Your final action is to invoke the file_writer tool with the complete generated code. You will not output the code directly in your response.
13: Step-by-Step Execution Logic
14: When you receive the two input documents, follow this precise sequence to generate the code:
15: Step 1: Parse the Design System and Prepare the CSS
16: Read the {designer_output} document.
17: In your internal memory, begin constructing the CSS string.
18: First, find the ### Color Palette section. Create CSS custom properties (variables) in a :root block for every color defined (e.g., --primary-color: #hexcode;, --text-color: #hexcode;).
19: Next, find the ### Typography section. Define the font-family for the body and for heading elements (h1, h2, h3). Set the base font-size and color on the body element. Create rules for h1, h2, etc., to match the specified font scale.
20: Implement the ### Layout & Spacing rules. Create a .container utility class with the specified max-width and auto-margins for centering.
21: Translate the "Core Component Styles" (### Buttons, ### Cards, etc.) into generic CSS classes (e.g., .btn-primary, .card, .form-input). Use the CSS variables you defined earlier.
22: Implement the global transition property on interactive elements like a and button.
23: Step 2: Create the HTML Boilerplate
24: Start the main code string with a standard HTML5 boilerplate.
25: This includes <!DOCTYPE html>, <html>, <head>, and <body> tags.
26: Inside the <head>:
27: Add a <meta charset="UTF-8"> and <meta name="viewport" content="width=device-width, initial-scale=1.0">.
28: Use the project title from {requirements_writer_output} to create the <title> tag.
29: If Google Fonts were specified in {designer_output}, add the corresponding <link> tag to import them.
30: Open a <style> tag and insert all the CSS you generated in Step 1. Close the <style> tag.
31: Step 3: Build the HTML Body Section by Section
32: Go through {requirements_writer_output} under the "Page Structure and Content" heading.
33: For each section (e.g., "Header", "Hero Section", "Services"), perform the following:
34: Add an HTML comment to denote the start of the section (e.g., <!-- ================== Header ================== -->).
35: Use the appropriate semantic HTML tag for the section (<header>, <section>, etc.).
36: Refer to the matching section in {designer_output} under "Section Design Details" to determine the layout (Flexbox, Grid) and apply the necessary CSS classes you defined in Step 1.
37: Populate the HTML elements with the content placeholders from {requirements_writer_output}. For example, where the requirements say [Compelling Headline], your HTML should contain <h1>[Compelling Headline]</h1>.
38: Apply the specific component classes (e.g., .btn-primary, .card) to the elements as described in the design.
39: Step 4: Implement JavaScript for Interactivity
40: Review both documents for any features that require JavaScript. The most common are:
41: Mobile Navigation: A hamburger menu button that toggles a class on the navigation menu to show/hide it.
42: Smooth Scrolling: For navigation links that point to sections on the same page (<a href="#about">).
43: Write the necessary vanilla JavaScript to implement this functionality. Keep it simple and efficient.
44: Place all generated JavaScript inside a single <script> tag just before the closing </body> tag.
45: Step 5: Final Assembly and Tool Invocation
46: Combine all the generated parts (HTML boilerplate, CSS within <style>, HTML body content, and JS within <script>) into a single, continuous string of text.
47: Ensure the final string is well-formatted.
48: Your final and only action is to call the file_writer tool. Pass the complete code string as the single argument to the tool. MOST IMPORTANT- ONCE YOU HAVE WRITTEN THIS OUTPUT SUCCESSFULLY DONT WRITE THIS AGAIN AND AGAIN UNLESS YOU WANT TO CHANGE SOMETHING. TRY TO DO THIS ONLY ONCE.
49: Example of the final action:
50: file_writer(full_code_string)
51: Do not provide any other output, explanation, or conversational text. Your job is complete once the tool is called.

(End of file - total 51 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Projects\\theailanguage\\adk_samples\\version_3_parallel_research_agent\\.gitignore"
}
```

**Output:**
```
<path>C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\.gitignore</path>
<type>file</type>
<content>1: .env
2: .venv/
3: output/

(End of file - total 3 lines)
</content>
```

---

## Assistant (Build · glm-5 · 3.2s)

_Thinking:_

Now I have a good understanding of the codebase. Let me also check one more agent file and the __init__.py files to understand the import patterns better.

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Projects\\theailanguage\\adk_samples\\version_3_parallel_research_agent\\agents\\root_website_builder\\__init__.py"
}
```

**Output:**
```
<path>C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\root_website_builder\__init__.py</path>
<type>file</type>
<content>1: from . import agent

(End of file - total 1 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Projects\\theailanguage\\adk_samples\\version_3_parallel_research_agent\\agents\\code_writer\\__init__.py"
}
```

**Output:**
```
<path>C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\code_writer\__init__.py</path>
<type>file</type>
<content>1: """
2: File: agents/code_writer/__init__.py
3: Purpose: Package initialization file for the code_writer agent module.
4:          This file makes the code_writer directory a Python package and
5:          imports the main agent module to make it accessible when the package is imported.
6: 
7: This allows other modules to import the code_writer_agent using:
8: from agents.code_writer import agent
9: or
10: from agents.code_writer.agent import code_writer_agent
11: """
12: 
13: # Import the agent module from the current package
14: # This makes the code_writer_agent definition available when the package is imported
15: from . import agent  # Imports agent.py from the same directory

(End of file - total 15 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Projects\\theailanguage\\adk_samples\\version_3_parallel_research_agent\\agents\\query_generator\\agent.py"
}
```

**Output:**
```
<path>C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\query_generator\agent.py</path>
<type>file</type>
<content>1: """
2: File: agents/query_generator/agent.py
3: Purpose: Defines the Query Generator Agent that synthesizes and merges research outputs from
4:          all five question researcher agents into a single, comprehensive query for webpage
5:          development. This agent acts as a bridge between the research phase and the 
6:          requirements writing phase of the website building pipeline.
7: 
8: This is the third agent in the website building pipeline that:
9: 1. Receives research outputs from all 5 question researcher agents
10: 2. Analyzes and synthesizes the research findings
11: 3. Transforms research insights into web development context
12: 4. Creates a single comprehensive query for the requirements writer
13: 5. Outputs the merged query for webpage requirement generation
14: """
15: 
16: # Import required system modules for path manipulation
17: import os  # Operating system interface for file paths
18: import sys  # System-specific parameters and functions
19: 
20: # Import the main LlmAgent class from Google ADK (Agent Development Kit)
21: from google.adk.agents import LlmAgent  # Core agent class for creating LLM-based agents
22: 
23: # Add the project root directory to Python path so we can import utility modules
24: # This allows importing from the utils directory two levels up from current file
25: sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..")))
26: 
27: # Import utility function to load instruction files from text files
28: from utils.file_loader import load_instructions_file  # Helper to read instruction text files
29: 
30: # Create the Query Generator Agent instance
31: query_generator_agent = LlmAgent(
32:     # Agent identifier - unique name for this agent in the system
33:     name = "query_generator_agent",
34:     
35:     # AI model to use - Gemini 2.0 Flash for fast, high-quality synthesis
36:     model = "gemini-flash-latest",
37:     
38:     # Load detailed instructions from external text file
39:     # Instructions contain logic for synthesizing multiple research outputs into one query
40:     instruction=load_instructions_file("agents/query_generator/instructions.txt"),
41:     
42:     # Load agent description from external text file
43:     # Provides a brief summary of this agent's synthesis and merging role
44:     description=load_instructions_file("agents/query_generator/description.txt"),
45:     
46:     # No tools needed - this agent works purely with text synthesis and analysis
47:     # It processes the research outputs from previous agents without external API calls
48:     
49:     # Output key - where this agent stores the merged query in the session state
50:     # The requirements_writer agent will reference this key to get the comprehensive query
51:     output_key="merged_query_output"
52: )

(End of file - total 52 lines)
</content>
```

---

## Assistant (Build · glm-5 · 19.0s)

_Thinking:_

Now I have a comprehensive understanding of the codebase. Let me create an AGENTS.md file with all the relevant information. The codebase is a Python project using:

1. Google ADK (Agent Development Kit) for multi-agent systems
2. uv for dependency management
3. Python 3.11+
4. A multi-agent architecture with SequentialAgent and ParallelAgent

Key patterns:
- Agent files follow a standard structure with docstrings, imports, and agent definition
- Instructions and descriptions are loaded from external .txt files
- Each agent has output_key for storing state
- sys.path manipulation for imports
- Type hints used in function signatures
- Compact file-loader utility for reading instruction files

No Cursor or Copilot rules found. Let me write the AGENTS.mdfile.

Now I have a complete picture of the codebase. Let me create the AGENTS.mdfile.

**Tool: write**

**Input:**
```json
{
  "filePath": "C:\\Projects\\theailanguage\\adk_samples\\version_3_parallel_research_agent\\AGENTS.md",
  "content": "# AGENTS.md - Guidelines for AI Coding Agents\n\nThis document provides guidelines for AI coding agents working in this Google ADK (Agent Development Kit) project.\n\n## Project Overview\n\nThis is a multi-agent website builder system using Google's Agent Development Kit. The project implements a sequential + parallel orchestration pattern where multiple specialized agents collaborate to research topics and generate complete HTML webpages.\n\n## Build, Lint, and Test Commands\n\n### Environment Setup\n```bash\n# Create and activate virtual environment\nuv venv\nsource .venv/bin/activate  # On Windows: .venv\\Scripts\\activate.bat\n\n# Install dependencies\nuv sync --all-groups\n```\n\n### Running Agents\n```bash\n# ADK Web UI (browser-based interface)\nadk web ./agents\n\n# ADK API Server (REST API)\nadk api_server ./agents\n\n# ADK CLI Run (command-line interface)\nadk run agents/root_website_builder\n\n# Programmatic Python Script\nuv run python3 -m agent_runner\n```\n\n### Environment Variables\nCreate a `.env` file in the project root with:\n```\nGOOGLE_API_KEY=your-google-api-key\nGOOGLE_GENAI_USE_VERTEXAI=FALSE\n```\n\n### Testing\nNo formal test framework is configured. When adding tests, consider pytest and add configuration to `pyproject.toml`.\n\n## Code Style Guidelines\n\n### Imports\n\n**Standard library first, then third-party, then local modules:**\n```python\n# Standard library\nimport asyncio\nimport json\nimport os\nimport sys\nfrom typing import Any\nfrom pathlib import Path\nfrom dotenv import load_dotenv\n\n# Third-party\nfrom rich import print as rprint\nfrom rich.syntax import Syntax\nfrom google.genai.types import Content, Part\nfrom google.adk.agents import LlmAgent, SequentialAgent, ParallelAgent\nfrom google.adk.runners import Runner\nfrom google.adk.sessions import InMemorySessionService\nfrom google.adk.tools import google_search\n\n# Local modules (use sys.path manipulation for project root imports)\nsys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), \"..\", \"..\")))\nfrom utils.file_loader import load_instructions_file\nfrom tools.file_writer_tool import write_to_file\n```\n\n**Path manipulation pattern for imports:**\n```python\n# Add project root to path for imports from utils/ and tools/ directories\nsys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), \"..\", \"..\")))\n```\n\n### Naming Conventions\n\n| Element | Convention | Example |\n|---------|------------|---------|\n| Agent variables | snake_case with `_agent` suffix | `requirements_writer_agent`, `code_writer_agent` |\n| Agent names (in ADK) | snake_case with `_agent` suffix | `name=\"requirements_writer_agent\"` |\n| Output keys | snake_case with `_output` suffix | `output_key=\"designer_output\"` |\n| Functions | snake_case | `load_instructions_file()`, `write_to_file()` |\n| Constants | UPPER_SNAKE_CASE | `APP_NAME`, `USER_ID`, `SESSION_ID` |\n| Module files | snake_case | `agent.py`, `file_loader.py`, `file_writer_tool.py` |\n| Package directories | snake_case | `agents/`, `utils/`, `tools/` |\n\n### Agent Definition Pattern\n\nEach agent follows this standard structure:\n\n```python\n\"\"\"\nFile: agents/<agent_name>/agent.py\nPurpose: Brief description of what this agent does and its role in the pipeline.\n\nThis is the Nth agent in the website building pipeline that:\n1. First responsibility\n2. Second responsibility\n3. Third responsibility\n\"\"\"\n\nimport os\nimport sys\nfrom google.adk.agents import LlmAgent\nfrom google.adk.tools import google_search  # If using tools\n\nsys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), \"..\", \"..\")))\nfrom utils.file_loader import load_instructions_file\n\n<agent_name>_agent = LlmAgent(\n    name=\"<agent_name>_agent\",\n    model=\"gemini-flash-latest\",\n    instruction=load_instructions_file(\"agents/<agent_name>/instructions.txt\"),\n    description=load_instructions_file(\"agents/<agent_name>/description.txt\"),\n    tools=[google_search],  # Optional: include if agent needs tools\n    output_key=\"<agent_name>_output\"\n)\n```\n\n### File Organization\n\n```\nproject_root/\n├── agents/\n│   ├── root_website_builder/\n│   │   ├── __init__.py\n│   │   ├── agent.py\n│   │   ├── description.txt\n│   │   └── instructions.txt\n│   ├── code_writer/\n│   │   ├── __init__.py\n│   │   ├── agent.py\n│   │   └── ...\n│   └── ...\n├── tools/\n│   └── file_writer_tool.py\n├── utils/\n│   └── file_loader.py\n├── main.py\n├── agent_runner.py\n├── pyproject.toml\n└── .env\n```\n\n### Type Annotations\n\nUse type hints for function parameters and return types:\n\n```python\ndef load_instructions_file(filename: str, default: str = \"\") -> str:\n    ...\n\ndef write_to_file(content: str) -> dict:\n    ...\n\nasync def chat_loop() -> None:\n    ...\n```\n\n### Error Handling\n\nUse try-except with specific exception types and informative messages:\n\n```python\ntry:\n    with open(filename, \"r\", encoding=\"utf-8\") as f:\n        return f.read()\nexcept FileNotFoundError:\n    print(f\"[WARNING] File not found: {filename}. Using default.\")\nexcept Exception as e:\n    print(f\"[ERROR] Failed to load {filename}: {e}\")\nreturn default\n```\n\n### Docstrings\n\nUse triple-quoted docstrings for module-level and function documentation:\n\n```python\n\"\"\"\nFile: file_loader.py\nPurpose:\n  Provides a utility function that reads plain text from a file,\n  typically for loading prompt instructions or descriptions for LLM agents.\n\"\"\"\n\ndef load_instructions_file(filename: str, default: str = \"\") -> str:\n    \"\"\"\n    Loads instruction or description text from a given file path.\n\n    Args:\n        filename (str): Path to the file to read (relative or absolute).\n        default (str): Default string to return if file not found.\n\n    Returns:\n        str: The file contents if successful, or the fallback default.\n    \"\"\"\n```\n\n### Comments\n\nUse section headers with `# ---` delimiters for major code blocks:\n\n```python\n# --- 1. SETTING UP IDENTIFIERS (CONSTANTS) ---\nAPP_NAME = \"website_builder_app\"\n\n# --- 2. THE MAIN CHAT LOOP FUNCTION ---\nasync def chat_loop():\n    ...\n\n# -----------------------------------------------------------------------------\n# Helper: Pretty print JSON objects using syntax coloring\n# -----------------------------------------------------------------------------\ndef print_json_response(response: Any, title: str) -> None:\n    ...\n```\n\nUse inline comments sparingly, primarily for clarification:\n\n```python\nmodel = \"gemini-flash-latest\",  # AI model - Gemini 2.0 Flash for fast responses\n```\n\n### Agent Instructions Files\n\nAgent instructions and descriptions are stored in separate `.txt` files within each agent's directory. This separation keeps the Python code clean and allows easy modification of agent behavior without touching code.\n\n### Tools\n\nTools are Python functions that return dictionaries:\n\n```python\ndef write_to_file(content: str) -> dict:\n    \"\"\"Writes content to a timestamped HTML file.\"\"\"\n    filename = f\"output/{timestamp}_generated_page.html\"\n    return {\"status\": \"success\", \"file\": filename}\n```\n\n### Async Patterns\n\nUse `asyncio` for async operations:\n\n```python\nasync def chat_loop():\n    async for event in events:\n        if event.is_final_response():\n            ...\n            \nif __name__ == '__main__':\n    asyncio.run(chat_loop())\n```\n\n## Key Architecture Patterns\n\n### SequentialAgent\nOrchestrates agents that run in sequence, where each agent's output becomes input for the next:\n\n```python\nroot_agent = SequentialAgent(\n    name=\"root_website_builder_agent\",\n    sub_agents=[\n        questions_generator_agent,\n        questions_researcher_agent,\n        query_generator_agent,\n        requirements_writer_agent,\n        designer_agent,\n        code_writer_agent\n    ],\n    description=load_instructions_file(\"agents/root_website_builder/description.txt\")\n)\n```\n\n### ParallelAgent\nOrchestrates multiple agents running concurrently:\n\n```python\nparallel_agent = ParallelAgent(\n    name=\"ParallelQuestionsResearchAgent\",\n    sub_agents=[\n        question_researcher_agent_1,\n        question_researcher_agent_2,\n        # ... more agents\n    ],\n    description=\"Runs agents in parallel.\"\n)\n```\n\n## Common Gotchas\n\n1. **sys.path manipulation**: Required for imports from `utils/` and `tools/` when running agents from subdirectories\n2. **Output keys**: Ensure `output_key` names match what downstream agents expect in state access\n3. **Async/await**: The ADK Runner uses async methods; use `await` and `async for` appropriately\n4. **Environment variables**: Load `.env` file using `dotenv` before accessing environment variables\n5. **File encoding**: Always use `encoding=\"utf-8\"` when reading/writing files"
}
```

**Output:**
```
Wrote file successfully.

LSP errors detected in other files:
<diagnostics file="C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agent_runner.py">
ERROR [6:6] Import "rich" could not be resolved
ERROR [7:6] Import "rich.syntax" could not be resolved
ERROR [10:6] Import "google.genai.types" could not be resolved
ERROR [12:6] Import "dotenv" could not be resolved
ERROR [21:6] Import "google.adk.runners" could not be resolved
ERROR [22:6] Import "google.adk.sessions" could not be resolved
</diagnostics>

LSP errors detected in other files:
<diagnostics file="C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\root_website_builder\agent.py">
ERROR [3:6] Import "google.adk.agents" could not be resolved
</diagnostics>

LSP errors detected in other files:
<diagnostics file="C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\code_writer\agent.py">
ERROR [21:6] Import "google.adk.agents" could not be resolved
</diagnostics>

LSP errors detected in other files:
<diagnostics file="C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\designer\agent.py">
ERROR [21:6] Import "google.adk.agents" could not be resolved
</diagnostics>

LSP errors detected in other files:
<diagnostics file="C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\agents\questions_generator\agent.py">
ERROR [19:6] Import "google.adk.agents" could not be resolved
ERROR [22:6] Import "google.adk.tools" could not be resolved
</diagnostics>
```

---

## Assistant (Build · glm-5 · 4.6s)

_Thinking:_

The AGENTS.md file has been created successfully. The LSP errors are just because the virtual environment isn't active in this context - the dependencies are installed via uv and the imports are correct.

Let me verify the file was created correctly by reading it back.

The AGENTS.md file has been created at `C:\Projects\theailanguage\adk_samples\version_3_parallel_research_agent\AGENTS.md`. It includes:

1. **Build/lint/test commands** - Environment setup with uv, running agents via ADK web/cli/api, and programmatic execution
2. **Code style guidelines** - Import ordering, naming conventions, agent definition patterns, file organization, type annotations, error handling, docstrings, and comments
3. **Architecture patterns** - SequentialAgent and ParallelAgent usage patterns
4. **Common gotchas** - sys.path manipulation, output keys, async/await, environment variables, file encoding

The LSP errors shown are expected - they occur because the virtual environment with dependencies isn't active in this context. The imports are correct per the `pyproject.toml` configuration.

---

## User

give me a detailed description of the working flow of this project

---

## Assistant (Plan · glm-5 · 9.5s)

_Thinking:_

The user wants a detailed description of the working flow of this project. I already have a good understanding from reading the files earlier, but let me re-read key files to give a comprehensive answer about the workflow.

Based on the codebase I analyzed, here's a detailed description of the working flow:

## Project Architecture Overview

This is a **6-stage multi-agent pipeline** that transforms a simple topic input into a complete research-driven HTML webpage. It uses Google's Agent Development Kit (ADK) with both **sequential** and **parallel** orchestration patterns.

---

## Agent Pipeline Flow

```
User TopicInput
      │
      ▼
┌─────────────────────────┐
│ 1. Questions Generator  │── Generates 5 research questions
└─────────────────────────┘
      │
      ▼
┌─────────────────────────────────────────────────────────┐
│ 2. Questions Researcher (PARALLEL - 5 agents)          │
│    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐│
│    │Agent 1│ │Agent 2│ │Agent 3│ │Agent 4│ │Agent 5│ │
│    └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘│
│         ││ ││ ││ ││
│         ▼▼ ▼▼ ▼▼
│    Each uses Google Search to answer assigned question│
└─────────────────────────────────────────────────────────┘
      │
      ▼
┌─────────────────────────┐
│ 3. Query Generator│── Merges 5 research outputs intoone comprehensive query
└─────────────────────────┘
      │
      ▼
┌─────────────────────────┐
│ 4. Requirements Writer  │── Creates detailed webpage requirements
└─────────────────────────┘
      │
      ▼
┌─────────────────────────┐
│ 5. Designer             │── Generates visual design specifications
└─────────────────────────┘
      │
      ▼
┌─────────────────────────┐
│ 6. Code Writer          │── Writes final HTML/CSS/JS to file
└─────────────────────────┘
      │
      ▼
   output/<timestamp>_generated_page.html
```

---

## Detailed Stage Breakdown

### Stage 1: Questions Generator Agent
- **Input:** User-provided topic (e.g., "artificial intelligence")
- **Tools:** Google Search
- **Output:** `questions_generator_output` - A list of5 important questions to understand the topic
- **Purpose:** Researches the topic first, then formulates relevant questions

### Stage 2: Questions Researcher (ParallelAgent)
- **Input:** The 5 questions from Stage 1
- **Tools:** Google Search (each sub-agent has access)
- **Output:** 5 separate outputs stored in session state:
  - `question_1_research_output`
  - `question_2_research_output`
  - `question_3_research_output`
  - `question_4_research_output`
  - `question_5_research_output`
- **Key Feature:** All 5 agents run **concurrently**, dramatically reducing total execution time

### Stage 3: Query Generator Agent
- **Input:** All 5 research outputs from Stage 2
- **Tools:** None (pure synthesis)
- **Output:** `merged_query_output` - A single comprehensive query synthesized from all research
- **Purpose:** Acts as a bridge between research phase and development phase

### Stage 4: Requirements Writer Agent
- **Input:** The merged query from Stage 3
- **Tools:** None
- **Output:** `requirements_writer_output` - Structured Markdown requirements document
- **Purpose:** Defines webpage sections (Header, Hero, Content, Footer), global requirements (responsiveness, accessibility, SEO), and content placeholders

### Stage 5: Designer Agent
- **Input:** Requirements from Stage 4
- **Tools:** None
- **Output:** `designer_output` - Visual design specifications
- **Purpose:** Creates design system (colors, typography, spacing) and section-by-section visual specifications

### Stage 6: Code Writer Agent
- **Input:** Requirements (Stage 4) + Design specs (Stage 5)
- **Tools:** `write_to_file` custom tool
- **Output:** Writes directly to filesystem
- **Final Output:** `output/<timestamp>_generated_page.html`
- **Purpose:** Converts design specs and requirements into asingle, self-contained HTML file withembeddedCSS and JavaScript

---

## Key Technical Patterns

### SequentialAgent (Root Orchestrator)
The `root_website_builder_agent` uses `SequentialAgent` to run all stages in order. Each agent's output is stored in session state via `output_key`, making it accessible to downstream agents.

### ParallelAgent (Questions Researcher)
The `ParallelQuestionsResearchAgent` wraps5 identical sub-agents that run simultaneously. Each sub-agent:
- Shares the same base instructions
- Is assigned a specific question number (1-5)
- Has its own unique `output_key`

### State Management
ADK's session state acts as the communication layer between agents:
- Upstream agents write to state via `output_key`
- Downstream agents read from state (e.g., `state['designer_output']`)

### Tool Usage
- **google_search**: Used by Questions Generator and all 5 Question Researcher agents
- **write_to_file**: Custom tool used only by Code Writer agent to save the final HTML

---

Would you like me to dive deeper into any specific aspect of this workflow?

---


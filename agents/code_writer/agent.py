"""
File: agents/code_writer/agent.py
Purpose: Defines the Code Writer Agent that transforms visual design specifications into
         complete, functional HTML/CSS/JavaScript code. This agent acts as a skilled
         front-end developer, implementing the design system and specifications into
         a single-file webpage that matches the original requirements exactly.

This is the sixth and final agent in the website building pipeline that:
1. Receives detailed design specifications from the designer agent
2. Implements the global design system (colors, typography, spacing) in CSS
3. Converts design specifications into semantic HTML structure
4. Adds interactive functionality with JavaScript where needed
5. Writes the complete webpage to a file using the file_writer_tool
"""

import os
import sys

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils.file_loader import load_instructions_file
from tools.file_writer_tool import write_to_file

code_writer_agent = LlmAgent(
    name="code_writer_agent",
    model=LiteLlm(model="zai/glm-4.7"),
    instruction=load_instructions_file("agents/code_writer/instructions.txt"),
    description=load_instructions_file("agents/code_writer/description.txt"),
    tools=[write_to_file],
)

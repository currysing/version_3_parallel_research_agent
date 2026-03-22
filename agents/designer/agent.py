"""
File: agents/designer/agent.py
Purpose: Defines the Designer Agent that transforms detailed webpage requirements into
         comprehensive visual design specifications. This agent acts as a pragmatic
         UI/UX designer, converting functional requirements into concrete design
         guidelines that developers can implement without ambiguity.

This is the fifth agent in the website building pipeline that:
1. Receives detailed requirements from the requirements_writer agent
2. Establishes a global design system (colors, typography, spacing)
3. Translates requirements into specific visual design specifications
4. Creates section-by-section design details with exact values
5. Outputs structured design specifications for the code_writer agent
"""

import os
import sys

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils.file_loader import load_instructions_file

designer_agent = LlmAgent(
    name="designer_agent",
    model=LiteLlm(model="zai/glm-4.7"),
    instruction=load_instructions_file("agents/designer/instructions.txt"),
    description=load_instructions_file("agents/designer/description.txt"),
    output_key="designer_output",
)

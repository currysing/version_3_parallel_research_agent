"""
File: agents/requirements_writer/agent.py
Purpose: Defines the Requirements Writer Agent that transforms a comprehensive, research-based
         query into detailed webpage requirements. This agent acts as an expert technical
         business analyst, converting high-level concepts into specific, actionable
         requirements that developers and designers can use to build webpages.

This is the fourth agent in the website building pipeline that:
1. Receives a comprehensive, research-backed query from the query_generator
2. Analyzes the query to identify webpage type and core purpose
3. Breaks down requirements into logical webpage components (Header, Hero, Content, Footer)
4. Defines global requirements (responsiveness, accessibility, SEO)
5. Outputs structured Markdown requirements for the designer agent
"""

import os
import sys

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils.file_loader import load_instructions_file

requirements_writer_agent = LlmAgent(
    name="requirements_writer_agent",
    model=LiteLlm(model="zai/glm-4.7"),
    instruction=load_instructions_file("agents/requirements_writer/instructions.txt"),
    description=load_instructions_file("agents/requirements_writer/description.txt"),
    output_key="requirements_writer_output",
)

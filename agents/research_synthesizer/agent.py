"""
File: agents/research_synthesizer/agent.py
Purpose: Defines the Research Synthesizer Agent that takes research outputs
         from all five question researcher agents and synthesizes them into
         a comprehensive, well-organized summary with suggested follow-up questions.

This agent:
1. Receives research outputs from all 5 question researcher agents
2. Analyzes and synthesizes the findings
3. Identifies key insights and patterns
4. Suggests follow-up questions for deeper research
5. Outputs a structured summary for the report writer
"""

import os
import sys

from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils.file_loader import load_instructions_file

research_synthesizer_agent = LlmAgent(
    name="research_synthesizer_agent",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/research_synthesizer/instructions.txt"),
    description=load_instructions_file("agents/research_synthesizer/description.txt"),
    output_key="research_synthesizer_output",
)

"""
File: agents/query_generator/agent.py
Purpose: Defines the Query Generator Agent that synthesizes and merges research outputs from
         all five question researcher agents into a single, comprehensive query for webpage
         development. This agent acts as a bridge between the research phase and the
         requirements writing phase of the website building pipeline.

This is the third agent in the website building pipeline that:
1. Receives research outputs from all 5 question researcher agents
2. Analyzes and synthesizes the research findings
3. Transforms research insights into web development context
4. Creates a single comprehensive query for the requirements writer
5. Outputs the merged query for webpage requirement generation
"""

import os
import sys

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils.file_loader import load_instructions_file

query_generator_agent = LlmAgent(
    name="query_generator_agent",
    model=LiteLlm(model="zai/glm-4.7"),
    instruction=load_instructions_file("agents/query_generator/instructions.txt"),
    description=load_instructions_file("agents/query_generator/description.txt"),
    output_key="merged_query_output",
)

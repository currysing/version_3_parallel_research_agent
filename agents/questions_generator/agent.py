"""
File: agents/questions_generator/agent.py
Purpose: Defines the Questions Generator Agent that takes a user-provided topic and generates
         five important questions to help understand that topic. This agent uses DuckDuckGo
         web search to research the topic before generating informed questions.

This is the first agent in the website building pipeline that:
1. Receives a topic from the user
2. Researches the topic using DuckDuckGo web search
3. Generates exactly 5 questions that help understand the topic
4. Outputs the questions for the questions_researcher agents to answer
"""

import os
import sys

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils.file_loader import load_instructions_file
from tools.ddg_search_tool import web_search

questions_generator_agent = LlmAgent(
    name="questions_generator_agent",
    model=LiteLlm(model="zai/glm-4.7"),
    instruction=load_instructions_file("agents/questions_generator/instructions.txt"),
    description=load_instructions_file("agents/questions_generator/description.txt"),
    tools=[web_search],
    output_key="questions_generator_output",
)

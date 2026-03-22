"""
File: agents/research_only/agent.py
Purpose: Defines the Research-Only Pipeline Agent that orchestrates
         a complete research workflow without website building.

This is the main entry point for generic research that:
1. Generates research questions about a topic (questions_generator_agent)
2. Researches each question in parallel (questions_researcher_agent)
3. Synthesizes findings into a comprehensive summary (research_synthesizer_agent)
4. Writes a formatted Markdown report (report_writer_agent)
"""

import os
import sys

from google.adk.agents import SequentialAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils.file_loader import load_instructions_file
from agents.questions_generator.agent import questions_generator_agent
from agents.questions_researcher.agent import questions_researcher_agent
from agents.research_synthesizer.agent import research_synthesizer_agent
from agents.report_writer.agent import report_writer_agent

root_agent = SequentialAgent(
    name="research_only_agent",
    sub_agents=[
        questions_generator_agent,
        questions_researcher_agent,
        research_synthesizer_agent,
        report_writer_agent,
    ],
    description=load_instructions_file("agents/research_only/description.txt"),
)

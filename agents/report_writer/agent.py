"""
File: agents/report_writer/agent.py
Purpose: Defines the Report Writer Agent that transforms synthesized research
         into a formatted Markdown file saved to output/research/.

This is the final agent in the research-only pipeline that:
1. Receives synthesized research from research_synthesizer_agent
2. Formats findings into a structured Markdown document
3. Writes the report to output/research/research_report_{timestamp}.md
4. Provides confirmation of successful file creation
"""

import os
import sys

from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils.file_loader import load_instructions_file
from tools.markdown_writer_tool import write_markdown_file

report_writer_agent = LlmAgent(
    name="report_writer_agent",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/report_writer/instructions.txt"),
    description=load_instructions_file("agents/report_writer/description.txt"),
    tools=[write_markdown_file],
    output_key="report_writer_output",
)

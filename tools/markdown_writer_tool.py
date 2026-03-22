"""
File: tools/markdown_writer_tool.py
Purpose: Provides a tool for writing Markdown research reports to disk.
         Creates timestamped files in the output/research/ directory.

Used by the report_writer_agent to save research findings as formatted Markdown files.
"""

import os
from datetime import datetime


def write_markdown_file(
    content: str,
    filename_prefix: str = "research_report",
    output_dir: str = "output/research",
) -> dict:
    """
    Writes Markdown content to a timestamped file in the output/research/ directory.

    Creates the output directory if it doesn't exist. Generates a filename with
    the format: {filename_prefix}_{YYYYMMDD_HHMMSS}.md

    Args:
        content: The Markdown content to write to the file.
        filename_prefix: Prefix for the filename. Defaults to "research_report".
        output_dir: Directory to save the file. Defaults to "output/research".

    Returns:
        dict: A dictionary containing:
            - status: "success" or "error"
            - file: The full path to the created file (if successful)
            - error: Error message (if failed)

    Example:
        >>> result = write_markdown_file("# My Research\\n\\nContent here...")
        >>> print(result)
        {"status": "success", "file": "output/research/research_report_20260322_143052.md"}
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Generate timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{filename_prefix}_{timestamp}.md"
        filepath = os.path.join(output_dir, filename)

        # Write content to file with UTF-8 encoding
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        return {
            "status": "success",
            "file": filepath,
            "filename": filename,
            "directory": output_dir,
        }

    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "filename_prefix": filename_prefix,
            "output_dir": output_dir,
        }

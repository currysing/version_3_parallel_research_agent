"""
File: tools/ddg_search_tool.py
Purpose: Provides a DuckDuckGo web search tool for ADK agents.
         This tool allows agents to perform web searches without requiring
         an API key, using DuckDuckGo's search engine.

The web_search function can be used as a tool in LlmAgent definitions
to enable web research capabilities.
"""

from duckduckgo_search import DDGS


def web_search(query: str, max_results: int = 5) -> dict:
    """
    Performs a web search using DuckDuckGo and returns formatted results.

    This tool enables agents to search the web for current information
    without requiring any API key. It uses DuckDuckGo's search engine
    which provides privacy-focused search results.

    Args:
        query: The search query string to look up.
        max_results: Maximum number of search results to return. Defaults to 5.

    Returns:
        dict: A dictionary containing:
            - status: "success", "no_results", or "error"
            - query: The original search query
            - results: List of search results (each with title, href, body)
            - error: Error message if status is "error"

    Example return:
        {
            "status": "success",
            "query": "Python programming",
            "results": [
                {
                    "title": "Python Official Site",
                    "href": "https://www.python.org",
                    "body": "Python is a programming language..."
                },
                ...
            ]
        }
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))

            if results:
                formatted_results = []
                for r in results:
                    formatted_results.append(
                        {
                            "title": r.get("title", ""),
                            "href": r.get("href", ""),
                            "body": r.get("body", ""),
                        }
                    )
                return {
                    "status": "success",
                    "query": query,
                    "results": formatted_results,
                }

            return {"status": "no_results", "query": query, "results": []}

    except Exception as e:
        return {"status": "error", "query": query, "error": str(e), "results": []}

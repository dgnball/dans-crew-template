"""
See
* https://medium.com/@prateek.vyas/10-must-know-python-code-snippets-for-leveraging-llms-b152fb450ff5
* https://stackoverflow.com/questions/37012469/duckduckgo-api-getting-search-results
"""

import requests
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from bs4 import BeautifulSoup


class MyToolInput(BaseModel):
    """Input schema for MyCustomTool."""

    query: str = Field(..., description="Duck duck go query")


class DuckDuckGoScrapeSearch(BaseTool):
    name: str = "DuckDuckGo Search"
    description: str = "Scrape DuckDuckGo Search results "
    args_schema: Type[BaseModel] = MyToolInput

    def _run(self, query: str) -> list:
        url = "https://duckduckgo.com/html/"
        params = {"q": query}
        response = requests.get(url, params=params)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.select(".result__body")


class DuckDuckGoApiSearch(BaseTool):
    name: str = "DuckDuckGo Search"
    description: str = "Call the duckduckgo API with a query and return the results."
    args_schema: Type[BaseModel] = MyToolInput

    def _run(self, query: str) -> list:
        url = "https://api.duckduckgo.com/"
        params = {"q": query, "format": "json"}
        response = requests.get(url, params=params)
        return response.json()["RelatedTopics"]

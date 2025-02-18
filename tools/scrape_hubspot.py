import requests
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from bs4 import BeautifulSoup


class MyToolInput(BaseModel):
    pass


class ScrapeHubspotIdeas(BaseTool):
    name: str = "Scrape hubspot ideas"
    description: str = "Scrape Hubspot Community Ideas page"
    args_schema: Type[BaseModel] = MyToolInput

    def _run(self) -> list:
        url = "https://community.hubspot.com/t5/HubSpot-Ideas/idb-p/HubSpot_Ideas/status-key/declined/tab/most-kudoed"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.select(".lia-quilt-column-alley-right")


class ScrapeHubspotIdeaInput(BaseModel):
    """Input schema for MyCustomTool."""

    url: str = Field(..., description="URL of page")


class ScrapeHubspotIdea(BaseTool):
    name: str = "Scrape hubspot idea"
    description: str = "Get contents of idea page"
    args_schema: Type[BaseModel] = ScrapeHubspotIdeaInput

    def _run(self, url: str) -> str:
        response = requests.get(url)
        return response.text

from crewai import Agent

from tools.search_tools import DuckDuckGoScrapeSearch, DuckDuckGoApiSearch

"""
Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""


class Agents:

    def simple_search_agent(self):
        return Agent(
            role="Simple Search Agent",
            backstory="I can get you a summary of search results from Duck Duck Go",
            goal="Return the Duck Duck Go search results",
            tools=[DuckDuckGoScrapeSearch()],
            verbose=True,
        )

    def simple_answer_agent(self):
        return Agent(
            role="Simple Answer Agent",
            backstory="I can get you a summary of results from Duck Duck Go",
            goal="Return the Duck Duck Go results",
            tools=[DuckDuckGoApiSearch()],
            verbose=True,
        )

    def pretty_webpage(self):
        return Agent(
            role="Convert markdown to html",
            backstory="I can create a themed page for markdown content",
            goal="Make boring markdown look fun",
            verbose=True,
        )

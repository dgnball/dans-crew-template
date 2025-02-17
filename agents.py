from crewai import Agent

from tools.search_tools import DuckDuckGoSearch

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
            tools=[DuckDuckGoSearch()],
            verbose=True,
        )

from crewai import Agent

from tools.scrape_hubspot import ScrapeHubspotIdeas
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

    def hubspot_ideas_scrape_agent(self):
        return Agent(
            role="Hubspot ideas scraper",
            backstory="I understand the Hubspot community page layout",
            goal="""
            Return a list of ideas including the following information:
            * Date submitted
            * Number of upvotes
            * Title
            * Description
            * Category
            * Read more link
            
            Format the list as a markdown table. Make sure the read more link is a full URL.
            """,
            tools=[ScrapeHubspotIdeas()],
            verbose=True,
        )

    def summerise_an_idea_agent(self):
        return Agent(
            role="Summarise an idea",
            backstory="I can read and digest the details of an idea webpage",
            goal="Read the details of a page and summarise in less than 2-3 paragraphs",
            tools=[ScrapeHubspotIdeas()],
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

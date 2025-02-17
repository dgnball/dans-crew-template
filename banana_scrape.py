from crewai import Crew
from agents import Agents
from tasks import Tasks

from dotenv import load_dotenv

load_dotenv()


class ResearchCrew:
    def __init__(self):
        pass

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = Agents()
        tasks = Tasks()

        # Define your custom agents and tasks here
        simple_search_agent = agents.simple_search_agent()

        # Custom tasks include agent name and variables as input
        search_for_bananas = tasks.search_for_bananas(
            simple_search_agent, "banana_scrape.md"
        )

        # Define your custom crew here
        crew = Crew(
            agents=[simple_search_agent],
            tasks=[search_for_bananas],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew")
    trip_crew = ResearchCrew()
    result = trip_crew.run()
    print(result)

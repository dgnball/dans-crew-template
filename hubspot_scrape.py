from crewai import Crew
from agents import Agents
from tasks import Tasks

from dotenv import load_dotenv

load_dotenv()


class ResearchCrew:
    def __init__(self):
        pass

    def run(self):
        agents = Agents()
        tasks = Tasks()
        hubspot_ideas_scrape_agent = agents.hubspot_ideas_scrape_agent()
        get_top_ideas = tasks.get_top_ideas(hubspot_ideas_scrape_agent, "top_ideas.md")
        summerise_an_idea_agent = agents.summerise_an_idea_agent()
        get_idea_details = tasks.get_idea_details(
            summerise_an_idea_agent, "idea_details.md"
        )

        crew = Crew(
            agents=[hubspot_ideas_scrape_agent, summerise_an_idea_agent],
            tasks=[get_top_ideas, get_idea_details],
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

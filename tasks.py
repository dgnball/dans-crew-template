from crewai import Task

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Develop a detailed itinerary, including city selection, attractions, and practical travel advice.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - A detailed 7 day travel itenerary.

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Itenerary Planning: develop a detailed plan for each day of the trip.
    - City Selection: Analayze and pick the best cities to visit.
    - Local Tour Guide: Find a local expert to provide insights and recommendations.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
  - Use this template as a guide to define each task in your CrewAI application. 
  - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.

  Template:
  ---------
  def [task_name](self, agent, [parameters]):
      return Task(description=dedent(f'''
      **Task**: [Provide a concise name or summary of the task.]
      **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the specific actions required to complete the task.]

      **Parameters**: 
      - [Parameter 1]: [Description]
      - [Parameter 2]: [Description]
      ... [Add more parameters as needed.]

      **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]

      '''), agent=agent)

"""


class Tasks:

    def search_for_bananas(self, agent, output_file_name):
        return Task(
            description="Summarise the first 10 search results for the word 'banana'.",
            agent=agent,
            output_file=output_file_name,
            expected_output="A summary of search results",
        )

    def make_a_nice_web_page(self, agent, output_file_name):
        return Task(
            description="Turn search results into a nice looking webpage",
            agent=agent,
            output_file=output_file_name,
            expected_output="A html page",
        )

    def get_top_ideas(self, agent, output_file_name):
        return Task(
            description="Get me the top Hubspot ideas",
            agent=agent,
            output_file=output_file_name,
            expected_output="A list of ideas",
        )

    def get_idea_details(self, agent, output_file_name):
        return Task(
            description="""
            Take the list at the top of the ideas with the most Upvotes
            and pass the Read More Link to the URL argument for the scraper.
            Summarise the result.
            """,
            agent=agent,
            output_file=output_file_name,
            expected_output="A markdown file describing the idea",
        )

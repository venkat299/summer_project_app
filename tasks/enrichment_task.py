from crewai import Task
from .utils import task_generator, get_agent_details

def enrichment_task(agent, context_task):
    """Defines the profile enrichment task using DSPy."""
    role, goal = get_agent_details(agent)
    generated_strings = task_generator.forward(
        agent_role=role,
        agent_goal=goal,
        context_info="List of candidate profiles from the sourcing task."
    )
    return Task(
        description=generated_strings.task_description,
        expected_output=generated_strings.expected_output,
        agent=agent,
        context=[context_task]
    )

from crewai import Task
from .utils import task_generator, get_agent_details

def ranking_task(agent, context_tasks):
    """Defines the candidate ranking task using DSPy."""
    role, goal = get_agent_details(agent)
    generated_strings = task_generator.forward(
        agent_role=role,
        agent_goal=goal,
        context_info="Hiring rubric and a list of enriched candidate profiles."
    )
    return Task(
        description=generated_strings.task_description,
        expected_output=generated_strings.expected_output,
        agent=agent,
        context=context_tasks
    )

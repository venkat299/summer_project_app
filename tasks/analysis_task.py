from crewai import Task
from .utils import task_generator, get_agent_details

def analysis_task(agent, job_description):
  """Defines the analysis task using DSPy for string generation."""
  role, goal = get_agent_details(agent)
  # Generate strings dynamically using DSPy
  generated_strings = task_generator.forward(
      agent_role=role,
      agent_goal=goal,
      job_description=job_description
  )
  return Task(
      description=generated_strings.task_description,
      expected_output=generated_strings.expected_output,
      agent=agent,
  )

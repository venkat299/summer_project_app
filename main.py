import os
from crewai import Crew, Process
from dotenv import load_dotenv

# The __init__.py file in the 'agents' directory allows for this clean import
from agents import JobSpecAnalystAgent, SourcingAgent
from tasks import analysis_task, sourcing_task

# Load environment variables from a .env file
load_dotenv()

# Instantiate agents
job_spec_analyst = JobSpecAnalystAgent()
sourcing_specialist = SourcingAgent()

# Job description
# job_description = """
# **Position:** Senior Python Developer
# **Location:** San Francisco, CA (Hybrid)
# **Experience:** 5+ years
# **Responsibilities:**
# - Design, build, and maintain efficient, reusable, and reliable Python code.
# - Integration of user-facing elements developed by front-end developers with server-side logic.
# - Solve complex performance problems and architectural challenges.
# - Integration of data storage solutions.
# **Skills:**
# - Proficient in Python, with a good knowledge of its ecosystems.
# - Familiarity with some Python web framework, such as Django, Flask, or FastAPI.
# - Solid understanding of object-oriented programming.
# - Familiarity with ORM (Object Relational Mapper) libraries.
# - Able to create database schemas that represent and support business processes.
# - Proficient understanding of code versioning tools, such as Git.
# """
job_description = """
**Position:** Industrial Engineer
**Location:** India, Chennai (Hybrid)
**Experience:** 5+ years
**Responsibilities:**
- Optimise process.
- Analysis and prediction.
- Solve complex  problems .
**Skills:**
- Proficient in Python, with a good knowledge of its ecosystems.
- Familiarity with some Python web framework, such as Django, Flask, or FastAPI.
- Operation Research
- Datascience
"""


# Define tasks
task1 = analysis_task(job_spec_analyst, job_description)
task2 = sourcing_task(sourcing_specialist, task1)

# Form the crew
# Note: The LLM is now managed within the agent definitions, so it's not needed here.
crew = Crew(
    agents=[job_spec_analyst, sourcing_specialist],
    tasks=[task1, task2],
    process=Process.sequential,
    verbose=True
)

# Kick off the crew's work
if __name__ == "__main__":
    result = crew.kickoff()
    print("\n\n########################")
    print("## Here is the final result")
    print("########################\n")
    print(result)

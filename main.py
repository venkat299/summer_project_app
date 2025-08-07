from dotenv import load_dotenv
from crewai import Crew, Process

# Load environment variables at the start.
load_dotenv()

# Import agents and tasks
from agents import (
    JobSpecAnalystAgent,
    SourcingAgent,
    ProfileEnrichmentAgent,
    CandidateRankingAgent
)
from tasks import (
    analysis_task,
    sourcing_task,
    enrichment_task,
    ranking_task
)

# Instantiate agents
job_spec_analyst = JobSpecAnalystAgent()
sourcing_specialist = SourcingAgent()
enrichment_specialist = ProfileEnrichmentAgent()
ranking_assessor = CandidateRankingAgent()

# Job description
job_description = """
**Position:** Senior Python Developer
**Location:** Chennai, India
**Experience:** 5+ years
**Responsibilities:**
- Design, build, and maintain efficient, reusable, and reliable Python code.
- Integration of user-facing elements developed by front-end developers with server-side logic.
- Solve complex performance problems and architectural challenges.
- Integration of data storage solutions.
**Skills:**
- Proficient in Python, with a good knowledge of its ecosystems.
- Familiarity with some Python web framework, such as Django, Flask, or FastAPI.
- Solid understanding of object-oriented programming.
- Familiarity with ORM (Object Relational Mapper) libraries.
- Able to create database schemas that represent and support business processes.
- Proficient understanding of code versioning tools, such as Git.
"""

# Define tasks and chain them together
task1_analysis = analysis_task(job_spec_analyst, job_description)
task2_sourcing = sourcing_task(sourcing_specialist, task1_analysis)
task3_enrichment = enrichment_task(enrichment_specialist, task2_sourcing)
task4_ranking = ranking_task(ranking_assessor, [task1_analysis, task3_enrichment])


# Form the crew with all agents and tasks
crew = Crew(
    agents=[
        job_spec_analyst,
        sourcing_specialist,
        enrichment_specialist,
        ranking_assessor
    ],
    tasks=[
        task1_analysis,
        task2_sourcing,
        task3_enrichment,
        task4_ranking
    ],
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

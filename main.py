
from crewai import Crew, Process
from dotenv import load_dotenv
import logging

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

# Load environment variables from a .env file
load_dotenv()

# --- Start of Logging Configuration ---
# Configure logging to write to a file.
# CrewAI's verbose mode (verbose=2) will use this configuration.
logging.basicConfig(
    filename='crew_execution.log',
    filemode='w',  # Overwrite the log file on each run
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
# --- End of Logging Configuration ---



# Instantiate agents
job_spec_analyst = JobSpecAnalystAgent()
sourcing_specialist = SourcingAgent()
enrichment_specialist = ProfileEnrichmentAgent()
ranking_assessor = CandidateRankingAgent()


# Job description
job_description = """
**Position:** Senior Python Developer
**Location:** India, Chennai (Hybrid)
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
# job_description = """
# **Position:** Industrial Engineer
# **Location:** India, Chennai (Hybrid)
# **Experience:** 5+ years
# **Responsibilities:**
# - Optimise process.
# - Analysis and prediction.
# - Solve complex  problems .
# **Skills:**
# - Proficient in Python, with a good knowledge of its ecosystems.
# - Familiarity with some Python web framework, such as Django, Flask, or FastAPI.
# - Operation Research
# - Datascience
# """


# Define tasks
# Define tasks and chain them together
task1_analysis = analysis_task(job_spec_analyst, job_description)
task2_sourcing = sourcing_task(sourcing_specialist, task1_analysis)
task3_enrichment = enrichment_task(enrichment_specialist, task2_sourcing)
# The ranking task needs context from both the analysis (rubric) and enrichment (profiles) tasks
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
    verbose=True,
    output_log_file = "crew_log"
)

# Kick off the crew's work
if __name__ == "__main__":
    result = crew.kickoff()
    print("\n\n########################")
    print("## Here is the final result")
    print("########################\n")
    print(result)
    logging.info("Crew kickoff finished.")

    print("\n\n########################")
    print("## Here is the final result")
    print("########################\n")
    print(result)

    print("\n\n########################")
    print("## All logs have been saved to crew_execution.log")
    print("########################\n")

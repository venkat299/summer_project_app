import streamlit as st
import json
import re
import logging
from io import StringIO
from crewai import Crew, Process
from dotenv import load_dotenv

# Load environment variables from a .env file
# Make sure you have a .env file with your API keys (e.g., GEMINI_API_KEY)
load_dotenv()

# Import your existing agent and task definitions
# This assumes your files are in a directory structure that Python can import from.
# E.g., the 'agents' and 'tasks' modules are in the same directory as app.py
# or installed as a package.
try:
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
except ImportError:
    st.error("Could not import agents and tasks. Make sure the files are in the correct directory.")
    st.stop()


# --- Streamlit UI Configuration ---
st.set_page_config(page_title="AI Recruiting Assistant", layout="wide")
st.title(" AI Recruiting Assistant")
st.markdown("Paste a job description below to find and rank qualified candidates.")

# --- Logging Configuration ---
# Create an in-memory string stream to capture logs
log_stream = StringIO()

# Configure the root logger to write to the stream
# CrewAI's verbose output will be captured by this handler
logging.basicConfig(
    stream=log_stream,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


# --- Main Application UI ---
st.header("1. Enter Job Description")
job_description_input = st.text_area(
    "Paste the full job description here:",
    height=300,
    placeholder="e.g., Position: Senior Python Developer, Location: San Francisco, CA..."
)

if st.button("✨ Find and Rank Candidates", type="primary"):
    if not job_description_input:
        st.error("Please paste a job description to begin.")
    else:
        # Clear previous logs and results for a fresh run
        log_stream.truncate(0)
        log_stream.seek(0)

        # Placeholders for the results
        rubric_placeholder = st.empty()
        queries_placeholder = st.empty()
        ranking_placeholder = st.empty()
        logs_placeholder = st.empty()

        with st.spinner(" Agents are at work... Analyzing, sourcing, and ranking candidates. This may take a few minutes."):
            try:
                # 1. Instantiate agents
                job_spec_analyst = JobSpecAnalystAgent()
                sourcing_specialist = SourcingAgent()
                enrichment_specialist = ProfileEnrichmentAgent()
                ranking_assessor = CandidateRankingAgent()

                # 2. Define tasks with the user's job description
                task1_analysis = analysis_task(job_spec_analyst, job_description_input)
                task2_sourcing = sourcing_task(sourcing_specialist, task1_analysis)
                task3_enrichment = enrichment_task(enrichment_specialist, task2_sourcing)
                task4_ranking = ranking_task(ranking_assessor, [task1_analysis, task3_enrichment])

                # 3. Form the crew
                crew = Crew(
                    agents=[job_spec_analyst, sourcing_specialist, enrichment_specialist, ranking_assessor],
                    tasks=[task1_analysis, task2_sourcing, task3_enrichment, task4_ranking],
                    process=Process.sequential,
                    verbose=True,
                    output_log_file = "crew_log"
                )

                # 4. Kick off the crew's work
                final_result = crew.kickoff()

                # 5. Retrieve all captured logs
                all_logs = log_stream.getvalue()

                # --- Extract and Display Results ---

                # Extract Hiring Rubric from the first task's output
                with rubric_placeholder.container():
                    st.header("2. Machine-Readable Hiring Rubric")
                    st.info("The AI converted the job description into a structured JSON rubric for precise evaluation.")
                    rubric_raw = task1_analysis.output.raw
                    try:
                        # Attempt to parse and pretty-print the JSON
                        st.json(json.loads(rubric_raw))
                    except (json.JSONDecodeError, TypeError):
                        # Fallback for non-JSON or malformed output
                        st.code(rubric_raw, language="text")

                # Extract X-Ray Search Queries from the logs using regex
                with queries_placeholder.container():
                    st.header("3. Sourcing X-Ray Queries")
                    st.info("These are the advanced search queries the AI used to find candidates online.")
                    # This pattern looks for the 'search_query' argument passed to the search tool
                    queries = re.findall(r"\"search_query\": \"(.*?)\"", all_logs, re.DOTALL)
                    if queries:
                        # for q in set(queries): # Use set to show only unique queries
                        st.code(queries, language="text")
                    else:
                        st.warning("No specific X-Ray queries were captured. They may be in the full log below.")

                # Display Final Candidate Ranking
                with ranking_placeholder.container():
                    st.header("4. Final Candidate Ranking")
                    st.info("Candidates are scored and ranked based on the rubric. Highest-scoring candidates are listed first.")
                    st.markdown(final_result)

                # Display Full Execution Log in an expander
                with logs_placeholder.expander("Show Full Execution Log"):
                    st.text_area("Log Output", all_logs, height=500, disabled=True)

            except Exception as e:
                st.error(f"An error occurred during the process: {e}")
                # Display logs for debugging even if there's an error
                all_logs = log_stream.getvalue()
                with logs_placeholder.expander("Show Error Log"):
                    st.text_area("Log Output", all_logs, height=500, disabled=True)


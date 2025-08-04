import os
from crewai import Agent
from crewai import LLM  


# from dotenv import load_dotenv
# load_dotenv()


llm = LLM(
    model="gemini/gemini-2.0-flash",
    verbose=True,
    temperature=0.1,
    google_api_key=os.getenv("GEMINI_API_KEY")
)

def JobSpecAnalystAgent():
    """
    Defines the Job-Spec Analyst Agent.
    """
    return Agent(
        role='Expert Technical Recruiter',
        goal='Transform job descriptions into a machine-readable hiring rubric.',
        backstory=(
            "A veteran recruiter with a knack for reading between the lines of a job description. "
            "They understand the nuances of technical roles and can translate them into "
            "clear, measurable criteria for evaluation."
        ),
        llm=llm, # Explicitly assign the configured Gemini LLM to the agent
        verbose=True,
        memory=True,
        tools=[],
        allow_delegation=False
    )

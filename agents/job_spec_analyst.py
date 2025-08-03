from crewai import Agent
from .utils import llm  # Import the shared LLM instance

def JobSpecAnalystAgent():
    """
    Defines the Job-Spec Analyst Agent.
    This agent focuses on analyzing job descriptions.
    """
    return Agent(
        role='Expert Technical Recruiter',
        goal='Transform job descriptions into a machine-readable hiring rubric.',
        backstory=(
            "A veteran recruiter with a knack for reading between the lines of a job description. "
            "They understand the nuances of technical roles and can translate them into "
            "clear, measurable criteria for evaluation."
        ),
        llm=llm,
        verbose=True,
        memory=False,
        tools=[],
        allow_delegation=False
    )

from crewai import Agent
# Import the shared LLM and tools
from .utils import llm, search_tool, exa_search_tool, github_search_tool

def SourcingAgent():
    """
    Defines the Sourcing Agent.
    This agent finds potential candidates based on the hiring rubric.
    """
    return Agent(
        role='Master Sourcing Specialist',
        goal='Identify potential candidates using advanced x-ray search.',
        backstory=(
            "A digital detective who thinks in Boolean logic. They are a master of "
            "finding needles in the digital haystack and can uncover candidate profiles "
            "from across the web."
        ),
        llm=llm,
        verbose=True,
        memory=False,
        tools=[search_tool, exa_search_tool, github_search_tool],
        allow_delegation=False
    )

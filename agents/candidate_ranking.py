from crewai import Agent
from .utils import llm

def CandidateRankingAgent():
    """
    Defines the Candidate Ranking Agent.
    This agent ranks candidates based on the enriched profiles and the job rubric.
    """
    return Agent(
        role='Lead Technical Assessor',
        goal='Objectively score candidates against the rubric with justifications.',
        backstory=(
            "An unbiased judge of technical talent, focused on transparency and fairness. "
            "They meticulously compare candidate profiles against the hiring rubric, "
            "providing clear scores and justifications for their assessments."
        ),
        llm=llm,
        verbose=True,
        memory=True,
        tools=[], # No specific tools needed, it reasons over the provided context
        allow_delegation=False
    )

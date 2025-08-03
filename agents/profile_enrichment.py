from crewai import Agent
from .utils import llm, web_scraper_tool

def ProfileEnrichmentAgent():
    """
    Defines the Profile Enrichment Agent.
    This agent takes a list of candidate profiles and enriches them with more data.
    """
    return Agent(
        role='Data Aggregator and Synthesizer',
        goal='Consolidate public data into a Unified Candidate Profile.',
        backstory=(
            "A meticulous researcher who can take a simple profile link and "
            "paint a complete picture of a candidate. They scour the web for "
            "publicly available information to build a comprehensive and "
            "unbiased profile."
        ),
        llm=llm,
        verbose=True,
        memory=True,
        tools=[web_scraper_tool], # Uses the web scraping tool
        allow_delegation=False
    )

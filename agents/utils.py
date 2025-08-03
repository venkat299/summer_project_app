import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai_tools import SerperDevTool, EXASearchTool, GithubSearchTool

from crewai import LLM  

load_dotenv()

llm = LLM(
    model="gemini/gemini-2.0-flash",
    verbose=True,
    temperature=0.1,
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Centralized tools for agents to use
search_tool = SerperDevTool()
exa_search_tool = EXASearchTool()
github_search_tool = GithubSearchTool(
    gh_token=os.getenv("GH_TOKEN"),
    config=dict(
        llm=dict(
            provider="google",
            config=dict(
                model="gemini",
                temperature=0.1,
                api_key=os.getenv("GEMINI_API_KEY"),
            ),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # api_key=os.getenv("GEMINI_API_KEY"),
            ),
        ),
    )
)


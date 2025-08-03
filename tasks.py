from crewai import Task

def analysis_task(agent, job_description):
  """Defines the analysis task for the Job-Spec Analyst Agent."""
  return Task(
      description=f"""
          Analyze the following job description and transform it into a machine-readable hiring rubric.
          The rubric should be a JSON object with clear categories for skills, experience, and responsibilities.
          Each item in the rubric should have a 'weight' from 1 to 5, where 5 is most important.

          Job Description:
          ---
          {job_description}
          ---
      """,
      expected_output="A JSON object representing the hiring rubric.",
      agent=agent,
  )

def sourcing_task(agent, context_task):
    """Defines the sourcing task for the Sourcing Agent."""
    return Task(
        description="""
            Using the hiring rubric provided, search for potential candidates on platforms like
            LinkedIn, GitHub, and other relevant developer communities. Your goal is to identify
            5-10 promising candidates who closely match the key skills and experience.
        """,
        expected_output="""
            A markdown-formatted report with a list of potential candidates, including their name,
            a link to their primary profile, and a brief justification.
        """,
        agent=agent,
        context=[context_task]
    )

def enrichment_task(agent, context_task):
    """Defines the profile enrichment task."""
    return Task(
        description="""
            For each candidate in the provided report, visit their profile link and any other
            publicly available information to create a 'Unified Candidate Profile'.
            This profile should consolidate their skills, experience, projects, and any other
            relevant information into a single, comprehensive document for each candidate.
        """,
        expected_output="""
            A list of 'Unified Candidate Profiles' in markdown format. Each profile should
            be a detailed summary of one candidate's qualifications and background.
        """,
        agent=agent,
        context=[context_task]
    )

def ranking_task(agent, context_tasks):
    """Defines the candidate ranking task."""
    return Task(
        description="""
            Objectively score each 'Unified Candidate Profile' against the original hiring rubric.
            For each key criterion in the rubric, provide a score from 1 to 10 and a concise
            justification for that score. The final output should be a ranked list of candidates.
        """,
        expected_output="""
            A final ranked report in markdown. The report should list each candidate, their total score,
            and a detailed breakdown of their score for each rubric criterion with justifications.
            Example:
            ### Candidate Ranking Report

            **1. John Doe - Score: 92/100**
            - Python (Weight 5): 10/10 - *Justification: Extensive experience shown in GitHub projects.*
            - Django (Weight 4): 9/10 - *Justification: Multiple professional projects listed on LinkedIn.*
            ...
        """,
        agent=agent,
        context=context_tasks
    )

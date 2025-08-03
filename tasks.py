from crewai import Task

def analysis_task(agent, job_description):
  """
  Defines the analysis task for the Job-Spec Analyst Agent.

  This task takes a job description and transforms it into a structured,
  machine-readable hiring rubric.
  """
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
      expected_output="""
          A JSON object representing the hiring rubric.
          Example:
          {
            "skills": [
              {"skill": "Python", "weight": 5},
              {"skill": "Django/Flask/FastAPI", "weight": 4},
              {"skill": "Object-Oriented Programming", "weight": 4},
              {"skill": "ORM Libraries", "weight": 3},
              {"skill": "Database Schema Design", "weight": 4},
              {"skill": "Git", "weight": 3}
            ],
            "experience": {
              "years": 5,
              "weight": 5
            },
            "responsibilities": [
              {"responsibility": "Design, build, and maintain Python code", "weight": 5},
              {"responsibility": "Integrate user-facing elements", "weight": 4},
              {"responsibility": "Solve complex performance problems", "weight": 4},
              {"responsibility": "Integrate data storage solutions", "weight": 3}
            ]
          }
      """,
      agent=agent
  )



def sourcing_task(agent, context_task):
    """
    Defines the sourcing task for the Sourcing Agent.
    This task depends on the output of the analysis_task.
    """
    return Task(
        description="""
            Using the hiring rubric provided, search for potential candidates on platforms like
            LinkedIn, GitHub, and other relevant developer communities.

            Your goal is to identify 5-10 promising candidates who closely match the key skills
            and experience outlined in the rubric. Use your search tools to perform
            x-ray searches and uncover profiles.
        """,
        expected_output="""
            A markdown-formatted report with a list of potential candidates.
            Each candidate entry should include their name, a link to their primary profile (e.g., LinkedIn or GitHub),
            and a brief, one-sentence justification for why they are a good match based on the rubric.

            Example:
            ### Potential Candidates Report

            - **John Doe**: [LinkedIn Profile](http://linkedin.com/in/johndoe)
              *Justification: Matches 5+ years of Python experience and has public projects using Django.*

            - **Jane Smith**: [GitHub Profile](http://github.com/janesmith)
              *Justification: Strong background in object-oriented programming and database design, evident from her repositories.*
        """,
        agent=agent,
        # The context makes this task dependent on the analysis_task's output
        context=[context_task]
    )

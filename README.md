# Summer Project App

## Overview
The Summer Project App is a proof‑of‑concept recruiting pipeline built with [CrewAI](https://github.com/joaomdmoura/crewai) and [DSPy](https://github.com/stanfordnlp/dspy).  
It orchestrates a group of specialized AI agents to turn a job description into a ranked list of promising candidates. The default workflow contains four agents:

1. **Job Spec Analyst** – converts a free‑form job description into a machine‑readable hiring rubric.
2. **Sourcing Specialist** – searches the web for candidate profiles that match the rubric.
3. **Profile Enrichment Agent** – visits each profile and builds a unified, enriched candidate profile.
4. **Ranking Assessor** – scores candidates against the rubric and produces a final ranking.

Each step is executed sequentially, passing outputs between agents to create a transparent and reproducible hiring process.

## Repository Structure
```
.
├── agents/             # Agent definitions and shared tools
├── dspy_logic/         # DSPy configuration and task-generation modules
├── tasks.py            # Task factories used by the crew in main.py
├── tools/              # Placeholder for custom CrewAI tools
├── main.py             # Entry point that wires agents and tasks together
└── tests/              # Smoke tests for the crew (currently illustrative)
```

## Installation
1. **Python** – requires Python 3.12 or newer.
2. **Install dependencies**
   ```bash
   pip install -e .
   ```
3. **Set environment variables** – at minimum the following keys are used:
   - `GEMINI_API_KEY` – Google Gemini key for CrewAI agents.
   - `GOOGLE_API_KEY` – Gemini key used by DSPy.
   - `SERPER_API_KEY` – key for Serper search.
   - `EXA_API_KEY` – key for EXA search.
   - `GH_TOKEN` – GitHub token for repository searches.
   Create a `.env` file or export these variables before running the app.

## Usage
Run the main script to execute the full workflow using the job description embedded in `main.py`:
```bash
python main.py
```
The script prints the final ranked report to the console.

## Testing
The repository uses `pytest` for automated tests.  A minimal placeholder test file is provided to show how a crew can be mocked.
```bash
pytest
```

## Extending the Project
- Add new tools in `tools/custom_tools.py` and register them with agents.
- Modify existing agents or create new ones in the `agents/` package.
- Replace the static job description in `main.py` with dynamic input or APIs.
- Enable and expand tests under `tests/` to cover your custom logic.

## License
This project is provided as-is for educational purposes.

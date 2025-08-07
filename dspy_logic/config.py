# dspy_logic/config.py

import os
import dspy
from dspy.llms.google import Google
from dotenv import load_dotenv

def configure_dspy():
    """Loads environment variables and configures DSPy settings."""
    load_dotenv()
    gemini = Google(
        model="gemini",
        api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.2
    )
    dspy.settings.configure(lm=gemini)
    
# configure_dspy()
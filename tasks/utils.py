# Import the configuration function first
from dspy_logic.config import configure_dspy
from dspy_logic.programs import TaskGeneratorModule

# --- Configuration Step ---
# Run the configuration here, right before any DSPy module that needs it is created.
# This guarantees the language model is loaded and ready.
configure_dspy()
# --------------------------

task_generator = TaskGeneratorModule()

# Helper function to get agent details
def get_agent_details(agent):
    """Extracts role and goal from an agent object."""
    return agent.role, agent.goal

import dspy
from .signatures import GenerateTaskStrings

class TaskGeneratorModule(dspy.Module):
    """A DSPy module to generate task strings."""
    def __init__(self):
        super().__init__()
        self.generate_task = dspy.ChainOfThought(GenerateTaskStrings)

    def forward(self, agent_role, agent_goal, **kwargs):
        # The 'forward' method defines the execution logic of the module.
        # It takes the agent's role and goal, plus any optional context or job description.
        context_info = kwargs.get('context_info', None)
        job_description = kwargs.get('job_description', None)

        # Call the ChainOfThought predictor to generate the task strings.
        prediction = self.generate_task(
            agent_role=agent_role,
            agent_goal=agent_goal,
            context_info=str(context_info) if context_info else "",
            job_description=job_description if job_description else ""
        )
        return prediction

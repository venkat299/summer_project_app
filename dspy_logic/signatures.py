import dspy

class GenerateTaskStrings(dspy.Signature):
    """Generates a structured description and expected output for a given agent role and goal."""

    agent_role = dspy.InputField(desc="The role of the agent.")
    agent_goal = dspy.InputField(desc="The primary goal of the agent.")
    context_info = dspy.InputField(desc="Information from previous tasks to be used as context.", optional=True)
    job_description = dspy.InputField(desc="The full job description.", optional=True)

    task_description = dspy.OutputField(desc="A detailed, dynamic description for the task.")
    expected_output = dspy.OutputField(desc="A clear and specific description of the expected output.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__doc__ = self.rewrite_docstring()

    def rewrite_docstring(self):
        """Dynamically creates a detailed docstring for the signature."""
        return f"""Given the agent role '{self.agent_role.json_schema_extra['desc']}' and goal '{self.agent_goal.json_schema_extra['desc']}', generate a structured description and expected output. The output should be tailored to the agent's function and the provided context if available."""


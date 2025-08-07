# This file makes the 'tasks' folder a Python package.
# It imports the task functions from their respective files
# so you can easily import them from the 'tasks' package.

from .analysis_task import analysis_task
from .sourcing_task import sourcing_task
from .enrichment_task import enrichment_task
from .ranking_task import ranking_task

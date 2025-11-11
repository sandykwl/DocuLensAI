from crewai import Agent, Crew, Task

from agents.reader_agent import reader_agent, reader_task
from agents.risk_dna_agent import risk_dna_agent, risk_dna_task
from logging_config import get_logger

class DocLensCrew:
    """
    A Crew pipeline that runs:
      1. Reader Agent → Extracts and summarizes proposal data.
      2. Risk DNA Agent → Analyzes originality and structure.
    """

    def __init__(self, verbose=True, logger=None):
        self.verbose = verbose
        self.logger = logger or get_logger(__name__)
        self.crew = self.create_crew()
        self.logger.info("DocLensCrew initialized")

    def create_crew(self):
        """Assemble the agents and tasks into a Crew."""
        self.logger.info("Creating DocLens crew with agents")

        crew = Crew(
            agents=[reader_agent, risk_dna_agent],
            tasks=[reader_task, risk_dna_task],
        )

        self.logger.info("Crew setup completed")
        return crew
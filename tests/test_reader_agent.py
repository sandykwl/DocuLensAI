from crewai import Crew
from agents.reader_agent import reader_agent, reader_task

def test_reader_agent_basic():
    # Input for the reader agent
    inputs = {
        "source_url": "https://be.gov.tools/proposal/get/d2745225498d1c56c0f01be9971074a49144d625df0e73a86c51689624fbadb0%230?drepId=",
        "domain_keywords": "cardano, governance"
    }

    # Create the Crew with the reader agent and task
    crew = Crew(agents=[reader_agent],
                tasks=[reader_task],
                chat_llm=None,
                manager_llm=None,
                planning_llm=None,
                function_calling_llm=None,
                verbose=True,)

    # Run the agent
    result = crew.kickoff(inputs=inputs)

    # Print the output
    print("\n🧠 Reader Agent Output:\n", result)



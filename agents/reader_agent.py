# agents/reader_agent.py

from crewai import Agent, Task
from tools.fetch_document_tool import FetchDocumentTool  # Your fetch tool

# --- Reader Agent ---
reader_agent = Agent(
    role="Document Reader",
    goal=(
        "Fetch text content from a given URL or document source. "
        "Do not analyze or summarize. Just return the raw text."
    ),
    backstory=(
        "You are a specialized document reader. "
        "You do not summarize or interpret the content, only extract the main text "
        "and attach any domain keywords for downstream agents."
    ),
    tools=[FetchDocumentTool()],  # Only fetching
    llm=None,  # No LLM needed
    verbose=True,
)

# --- Reader Task ---
reader_task = Task(
    name="Read Document Text",
    description=(
        "Input:\n"
        "- `source_url`: {source_url}\n"
        "- `domain_keywords`: {domain_keywords} (just passed through)\n\n"
        "Output:\n"
        "Return a Python dict with:\n"
        "- `document_text`: the raw extracted text\n"
        "- `domain_keywords`: same input string"
    ),
    expected_output=(
        "Python dict:\n"
        "{\n"
        "  'document_text': '...',\n"
        "  'domain_keywords': '...'\n"
        "}"
    ),
    agent=reader_agent,
)

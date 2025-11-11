from crewai import Agent, Task, LLM

from tools.linguistic_metric_tool import LinguisticMetricTool

# --- LLM Setup ---
llm = LLM(model="openai/gpt-5-mini")

# --- Unified Risk DNA Agent ---
risk_dna_agent = Agent(
    role="Risk DNA & Originality Evaluator",
    goal=(
        "Assess the document for originality, authorship likelihood, internal structure, "
        "and risk indicators. Provide a single structured report covering both originality "
        "and structural risk aspects."
    ),
    backstory=(
        "You are a multi-disciplinary evaluator skilled in detecting AI-generated or "
        "copied content and assessing governance proposal quality. You analyze documents "
        "for originality, logical consistency, structural completeness, and potential risks."
    ),
    tools=[LinguisticMetricTool()],
    llm=llm,
    verbose=True,
    memory=False,
)

# --- Structured Prompt Builder ---
def combined_prompt(document_text: str, domain_keywords: str) -> str:
    return f"""
You are an expert in both linguistic originality detection and blockchain governance analysis.

### Domain Keywords:
{domain_keywords}

### Document Text:
{document_text}

Perform a dual analysis:

1. **Originality Evaluation**
   - Estimate originality_score (0–1, 1 = very original)
   - Classify verdict: 'original', 'possibly AI-generated', or 'copied'
   - Summarize reasoning (e.g., repetition, tone, style clues)

2. **Structure & Risk Evaluation**
   - structure_score (0–1, 1 = well-organized and logically consistent)
   - risk_level: "low" | "medium" | "high"
   - issues: list of specific detected weaknesses
   - recommendations: list of concrete improvements

Output a **single JSON object** with this structure:

{{
  "originality": {{
    "originality_score": float,
    "verdict": str,
    "reasoning": str
  }},
  "risk_dna": {{
    "structure_score": float,
    "risk_level": str,
    "issues": [str],
    "recommendations": [str]
  }}
}}
"""

# --- Unified Task ---
risk_dna_task = Task(
    name="Comprehensive Risk DNA & Originality Analysis",
    description="Analyze both originality and governance structure risks for a given document.",
    expected_output=(
        "{ 'originality': {...}, 'risk_dna': {...} }"
    ),
    agent=risk_dna_agent,
)

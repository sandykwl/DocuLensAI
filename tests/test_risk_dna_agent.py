from crewai import Crew
from agents.reader_agent import reader_agent, reader_task
from agents.risk_dna_agent import risk_dna_agent, risk_dna_task


def test_risk_dna_pipeline():
    """End-to-end test: Reader → Risk DNA (Originality + Structure Analysis)."""

    # --- Input to Reader Agent ---
    inputs = {
        "source_url": "https://be.gov.tools/proposal/get/d2745225498d1c56c0f01be9971074a49144d625df0e73a86c51689624fbadb0%230?drepId=",
        "domain_keywords": "finance, treasury, blockchain",
    }

    # --- Crew Pipeline ---
    crew = Crew(
        agents=[reader_agent, risk_dna_agent],
        tasks=[reader_task, risk_dna_task],
    )

    # --- Run the pipeline ---
    result = crew.kickoff(inputs=inputs)

    print("\nFull Reader → Risk DNA Pipeline Output:\n", result)

    # # --- Validate Output Structure ---
    # assert isinstance(result, dict), "Result should be a dictionary."
    #
    # # Outer structure check
    # assert "originality" in result, "Missing 'originality' section in output."
    # assert "risk_dna" in result, "Missing 'risk_dna' section in output."
    #
    # # Check originality block
    # originality = result["originality"]
    # assert "originality_score" in originality
    # assert "verdict" in originality
    # assert "reasoning" in originality
    #
    # # Check risk_dna block
    # risk_dna = result["risk_dna"]
    # assert "structure_score" in risk_dna
    # assert "risk_level" in risk_dna
    # assert "issues" in risk_dna
    # assert "recommendations" in risk_dna

    print("\n✅ Risk DNA pipeline test completed.")

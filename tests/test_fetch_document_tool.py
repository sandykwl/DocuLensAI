
from tools.fetch_document_tool import FetchDocumentTool

def test_fetch_document_tool():
    tool = FetchDocumentTool()

    # Example URL for testing (you can replace with any accessible URL)
    test_url = "https://be.gov.tools/proposal/get/d2745225498d1c56c0f01be9971074a49144d625df0e73a86c51689624fbadb0%230?drepId="
    domain_keywords = "academic, research"

    result = tool._run(
        source_url=test_url,
        domain_keywords=domain_keywords,
    )

    print("\nFetchDocumentTool Output:\n", result)

    # Assertions to check the expected structure
    assert "document_text" in result
    assert "domain_keywords" in result
    assert "error" in result
    # Optional: basic sanity check
    assert result["domain_keywords"] == domain_keywords

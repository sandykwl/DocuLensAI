# 🧠 DocuLensAI — Intelligent Document Insight through Agentic Collaboration

**DocuLensAI** is an **agentic document intelligence system** built using **CrewAI** and integrated with **Masumi’s decentralized payment network** on **Cardano**.
It allows users to submit any document through a URL and receive AI-powered insights — from extraction to linguistic, structural and risk analysis — executed via coordinated autonomous agents.

---

## Key Features

* **AI-powered document diagnostics:**
  Automatically extracts, reads, and analyzes governance proposals or technical documents from URLs.
* **Agentic collaboration pipeline:**
  Multi-agent CrewAI system combining text ingestion, linguistic analysis, and risk evaluation.
* **Tool-assisted precision:**
  Each agent is paired with specialized tools — `FetchDocumentTool` for reliable text ingestion, and `LinguisticMetricTool` for detailed language and structure analysis.
* **Decentralized payments via Masumi:**
  Fully integrated with Masumi Payment Service for blockchain-based monetization.
* **FastAPI production server:**
  Exposes MIP-003-compliant endpoints for easy integration and testing.

---

## Demo

[![Watch the video](https://img.youtube.com/vi/8iRorpk9Ilw/0.jpg)](https://www.youtube.com/watch?v=8iRorpk9Ilw)

---

## 🧩 Crew Overview

| Agent              | Role                         | Tools Used             | Description                                                                                                 |
| ------------------ | ---------------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Reader Agent**   | Document Reader              | `FetchDocumentTool`    | Fetches raw text from proposal or document URLs and outputs `{document_text, domain_keywords}`.             |
| **Risk DNA Agent** | Risk & Originality Evaluator | `LinguisticMetricTool` | Evaluates originality, linguistic metrics, and structural risk indicators using contextual domain keywords. |
| **DocLens Crew**   | Coordinator                  | —                      | Orchestrates agents and exposes the API interface.                                                          |

---

## Getting Started

### 1️⃣ Clone Repository

**Prerequisites:**

* Python ≥ 3.10 and < 3.13
* [uv](https://docs.astral.sh/uv/) (Python package manager)

```bash
git clone https://github.com/masumi-network/crewai-masumi-quickstart-template.git
cd crewai-masumi-quickstart-template
uv venv --python 3.13
source .venv/bin/activate
uv pip install -r requirements.txt
```

*On Windows:*

```bash
uv venv --python 3.13
.\.venv\Scripts\activate
uv pip install -r requirements.txt
```

---

### 2️⃣ Configure Environment Variables

Copy `.env.example` to `.env` and fill with your configuration:

```bash
cp .env.example .env
```

Example:

```bash
PAYMENT_SERVICE_URL=http://localhost:3001/api/v1
PAYMENT_API_KEY=your_payment_key
AGENT_IDENTIFIER=your_agent_identifier_from_registration
SELLER_VKEY=your_selling_wallet_vkey
PAYMENT_AMOUNT=10000000
PAYMENT_UNIT=lovelace
OPENAI_API_KEY=your_openai_api_key
NETWORK=Preprod
```

---

### 3️⃣ Run Locally (Standalone)

Run the pipeline without payments:

```bash
python main.py
```

You’ll see output similar to:

```
======================================================================
🚀 Running CrewAI agents locally (standalone mode)...
======================================================================

Source URL: https://be.gov.tools/proposal/get/d2745225498d1c56c0f01be9971074a49144d625df0e73a86c51689624fbadb0%230?drepId=
Domain Keywords: finance, treasury, blockchain

Processing with CrewAI agents...
```

### Example Crew Output

```json
{
  "originality": {
    "metrics": {
      "lexical_diversity": 0.413,
      "repetition_ratio": 0.142,
      "normalized_length_score": 1.0,
      "word_count": 1064
    },
    "domain_keywords": "finance, treasury, blockchain",
    "authorship_likelihood": "Authorship cannot be determined from linguistic metrics alone. The document displays domain-specific governance formatting and references, consistent with human-authored policy proposals or templated drafting assistance. No definitive AI-signature indicators are detected by the provided metrics."
  },
  "risk_dna": {
    "structure_assessment": {
      "sections_present": [
        "Executive Summary",
        "Participating Members",
        "Budget",
        "Administrator",
        "Funding Method",
        "Withdrawal Logic",
        "Oversight & Audit Mechanism",
        "Expiration & Fund Recovery",
        "Dispute Resolution",
        "Reporting",
        "Conclusion",
        "References"
      ],
      "coherence": "High; the document follows a conventional governance action structure with clearly delineated roles, funding mechanics, and oversight."
    },
    "risk_indicators": {
      "governance_overreach_risk": "Low to Medium",
      "audit_and_transparency": "Moderate",
      "design_complexity_and_security": "High",
      "operational_risk": "Medium-High",
      "funds_control_and_recovery": "Medium",
      "conflict_of_interest_and_access": "Medium",
      "deadlock_or_partial_approval_risk": "Medium"
    },
    "risk_mitigation_recommendations": [
      "Institute an external independent security audit of the smart contract implementations and governance workflow before deployment.",
      "Add multi-signature or threshold-based withdrawal authorization to reduce single-member risk.",
      "Publish machine-readable records of all approvals, withdrawals, and budget actions to enhance auditability.",
      "Define emergency pause and fail-safe procedures beyond internal CC oversight.",
      "Introduce explicit sunset or performance metrics to reassess compensation terms over time."
    ],
    "overall_risk_rating": "Medium-High",
    "notes": "The governance proposal is structurally coherent and transparent but entails significant on-chain financial controls and multi-party governance dynamics that demand external security validation and tighter control mechanisms to reduce operational and compliance risk."
  }
}
```

---

## 🧱 Architecture Overview

```
┌────────────────────┐       ┌────────────────────┐       ┌────────────────────────┐       ┌────────────────────┐
│  FetchDocumentTool │────▶ │   Reader Agent     │────▶ │  LinguisticMetricTool   │────▶ │  Risk DNA Agent     │
└────────────────────┘       └────────────────────┘       └────────────────────────┘       └────────────────────┘
         │                            │                              │                              │
         ▼                            ▼                              ▼                              ▼
   URL or Source Text        Extracted Text + Keywords     Originality + Structure Metrics     Risk & Governance Analysis

                                   │
                                   ▼
                            DocuLens Crew Coordinator
                                   │
                                   ▼
                              FastAPI + Masumi
```

---

## 💡 Next Steps

* Persist job data using a database like PostgreSQL or Redis.
* Extend analysis with semantic coherence, readability, and tone metrics.
* Deploy to production with Masumi’s Mainnet integration.

---

## 🧱 Tech Stack

* **CrewAI** — Multi-agent orchestration
* **FastAPI** — REST backend
* **Masumi SDK** — Decentralized payments
* **Cardano** — Blockchain settlement layer
* **Python 3.11** — Runtime

---

## 📚 Useful Resources

* [CrewAI Documentation](https://docs.crewai.com)
* [Masumi Developer Docs](https://docs.masumi.network)
* [FastAPI Docs](https://fastapi.tiangolo.com/)
* [Cardano Testnet Faucet](https://testnets.cardano.org/en/testnets/cardano/tools/faucet/)

---

### 🏁 DocuLensAI

> *Intelligent Document Insight through Agentic Collaboration.*


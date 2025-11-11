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
    "linguistic_metrics": {
      "lexical_diversity": 0.222,
      "repetition_ratio": 0.351,
      "length_score": 1.0,
      "word_count": 2492,
      "composite_score": 0.58,
      "source": "Linguistic Metric Tool observation"
    },
    "summary_assessment": "Mixed: substantive original proposal text layered on standard governance/CIP boilerplate.",
    "evidence_and_reasoning": [
      "Low lexical diversity (0.222) combined with moderate repetition (0.351) indicates repeated use of governance-template language and recurring phraseology typical of CIP/guideline documents rather than highly varied narrative prose.",
      "Length is substantial (≈2,492 words), supporting a detailed, authored governance proposal rather than a short automatically generated notice.",
      "Document explicitly embeds CIP metadata (@context, CIP100/CIP108 references) and governance boilerplate (Articles and Tenets citations), which explains part of the repetition and templated structure.",
      "Named authors and cryptographic witness/signature blocks appear in the JSON metadata (multiple organizations and individuals) — this provenance favors human authorship and collaborative drafting.",
      "Phrases quoting the Cardano Constitution and use of governance-specific constructs (Treasury Withdrawal Governance Action, epochs, vesting terms) are domain-specific and consistent with human subject-matter authorship.",
      "References to an identified open-source smart contract repository (SundaeSwap treasury-contracts) suggests reuse of technical references and/or code-base rather than wholesale AI invention."
    ],
    "plagiarism_or_reuse_indicators": {
      "high_confidence_reuse": [
        "CIP template sections and metadata (CIP100/CIP108 context keys and structure).",
        "Direct quotes from the Cardano Constitution (Article and Tenet citations).",
        "Reference and naming reuse of the Cardano Treasury/Vendor Smart Contract (link to external repo)."
      ],
      "moderate_confidence_reuse": [
        "Standard governance phrasing describing budgets, administrators, oversight, vesting — likely adapted from prior governance proposals or common templates."
      ],
      "low_confidence_reuse": [
        "Unique phrasings such as 'ivory tower' and phrasing of dispute-resolution details appear authored for this document."
      ]
    },
    "authorship_likelihood": {
      "most_likely": "Human collaborative authorship (the listed organizations/individuals)",
      "supporting_factors": [
        "Signed witness blocks and public keys in the JSON metadata.",
        "Domain-specific, coherent structure and references.",
        "Complex governance semantics that match Cardano CIP patterns."
      ],
      "residual_uncertainty": "Some boilerplate and repeated sections may be copy-pasted from existing CIP templates and prior CC/treasury proposals; the document likely mixes original drafting with template reuse."
    },
    "originality_risk_level": "Moderate (document appears legitimate and authored by named parties but includes standard template material and external-code references that reduce uniqueness)"
  },

  "risk_dna": {
    "structural_integrity": {
      "strengths": [
        "Comprehensive coverage of governance-relevant elements: participants, budget total, vesting schedule concept, administrator (smart contract), oversight, dispute resolution, reporting, and fund recovery.",
        "Design choice to deploy separate smart contract instances per CC member increases accounting granularity and reduces single-contract blast radius for mistakes.",
        "On-chain auditable withdrawals with public addresses improves traceability and transparency.",
        "Automatic sweep-back of unclaimed funds to the Cardano Treasury after a defined window reduces risk of permanently stranded funds in many failure modes."
      ],
      "weaknesses": [
        "Approval mechanism: 'The Treasury Withdrawal Governance Action must be approved for submission by all members seeking compensation.' This means beneficiaries must approve the action that funds their own contracts — a clear conflict of interest and governance risk.",
        "Critical governance parameters left unspecified in the smart-contract description: exact quorum, majority thresholds, timing and format for the CC vote to pause withdrawals, and how 'no longer serving' is detected/enforced on-chain.",
        "Recipient immutability: contract cannot change recipient address. If a beneficiary loses their keys or needs to change account, the proposed remedy is to 'make a new budget request to Ada holders' — operationally risky and may cause funds to be stranded until the next treasury action.",
        "Dispute-resolution entirely internal: reliant on the CC's four-member vote without an external independent arbiter or escalation path, increasing capture/collusion risk.",
        "No explicit specification of independent third-party audits, external monitoring, or continuous formal verification of the customized treasury contract code.",
        "No performance/deliverable metrics, reporting cadence, or KPIs that tie payment amounts to demonstrated work — making payments effectively unconditional once approved.",
        "No explicit anti-self-dealing rules (e.g., recusal requirements) or prohibitions on CC members voting to authorize their own payments beyond the stated approval step."
      ]
    },

    "smart_contract_and_technical_risks": {
      "contract_design_risks": [
        "Immutability of recipient address prevents emergency migration of funds if private keys are lost or compromised; current mitigation (new budget request) is slow and uncertain.",
        "Pause authority vested in other CC members could be abused or lead to contested freezes; the exact voting threshold is not defined.",
        "No description of on-chain identity/role verification; the smart contract cannot autonomously verify whether the designated member 'is still serving' unless some off-chain oracle or manual input is used — this opens sybil, oracle, and manipulation risks.",
        "Customization of open-source contract introduces potential for subtle bugs; without formal verification or external audit, a vulnerability could enable theft or denial of funds.",
        "Concurrent funding of five separate contracts increases deployment complexity and the attack surface (five deployments to secure and audit)."
      ],
      "operational_risks": [
        "Key management — loss or compromise of a beneficiary's custody account is not robustly addressed.",
        "Ambiguity about what constitutes 'service time' for pro-rata calculations and who verifies the calculation.",
        "No stated contingency for jurisdictional, tax, or regulatory compliance matters for recipients who are organizations in different countries.",
        "Dependence on internal CC members to approve actions that fund themselves — reputational and legal risk if perceived as self-enrichment."
      ],
      "severity": "High for recipient immutability & conflict-of-interest approval; Medium for unspecified quorum and lack of independent audit; Medium for oracle/identity ambiguity."
    },

    "governance_risks_and_evidence": {
      "documented_community_signals": {
        "dRepYesVotes": 763939945163791,
        "dRepNoVotes": 1357178672416811,
        "dRepAbstainVotes": 684185278609267,
        "poolYesVotes": 10790015487470,
        "poolNoVotes": 1047705399718,
        "poolAbstainVotes": 0,
        "ccYesVotes": 1,
        "ccNoVotes": 0,
        "ccAbstainVotes": 1,
        "interpretation": "Among Delegate Representatives (dReps) the No votes exceed Yes votes by a substantial margin — this indicates meaningful dissent from that stakeholder class. Pool-level votes show Yes >> No, but pool voting weight may reflect a different constituency. CC voting metadata is minimal/ambiguous (1 yes, 1 abstain). These signals suggest contested community acceptance and potential reputational risk."
      },
      "conflict_of_interest": [
        "Beneficiaries must approve the Treasury Withdrawal Governance Action that funds their own compensation (self-approval requirement).",
        "Five of the seven CC members are claimants for compensation while two abstain — the concentration of paid members could change incentives in constitutional oversight."
      ],
      "transparency_and_accountability_gaps": [
        "No periodic deliverable reporting schedule or independent verification requirement beyond 'public address' transparency of transfers.",
        "No explicit external audit requirement for the customized treasury contract or periodic financial audits.",
        "No specification of sanction mechanics if a CC member engages in misconduct beyond pausing withdrawals."
      ]
    },

    "recommendations_and_mitigations": {
      "priority_fixes (high_priority)": [
        {
          "issue": "Conflict of interest: self-approval",
          "recommendation": "Require that beneficiaries do NOT participate in the approval vote for their own Treasury Withdrawal Governance Action. Instead, require Ada-holder approval (community vote) or an independent committee/escrow multisig to authorize release of funds."
        },
        {
          "issue": "Recipient immutability / key loss",
          "recommendation": "Add a secure recovery mechanism: e.g., a time-locked multisig recovery process with independent signers (not solely CC) and strict on-chain time delays and public notice windows before migration of recipient address."
        },
        {
          "issue": "Lack of third-party audit",
          "recommendation": "Mandate an independent security audit and (ideally) formal verification of the customized treasury contract before funding, with public audit reports and a remediation window."
        }
      ],
      "medium_priority": [
        {
          "issue": "Undefined voting/quorum thresholds in contract",
          "recommendation": "Explicitly encode quorum, majority thresholds, and tie-breaking rules for pause/unpause and disputes into the smart contract code and governance documentation."
        },
        {
          "issue": "On-chain role verification undefined",
          "recommendation": "Specify and implement an oracle or registry mechanism for verifying CC membership status on-chain (with decentralised updates and dispute recourse), or require an off-chain attestation scheme with transparency and audit logs."
        },
        {
          "issue": "No performance/deliverable KPIs",
          "recommendation": "Define clear, minimal reporting deliverables and cadence (monthly/quarterly public reports) that are preconditions for continued withdrawals or included as part of release criteria."
        }
      ],
      "lower_priority": [
        {
          "issue": "Tax/compliance considerations absent",
          "recommendation": "Request that applicants include statements about entity type, tax jurisdiction, and attestations of compliance or commit to handling tax liabilities and to provide required documentation."
        },
        {
          "issue": "Multiple contract deployments increase attack surface",
          "recommendation": "Apply identical audited code across instances and consider a single audited factory pattern with parameterized instances to reduce deployment complexity and allow code reuse with known-good provenance."
        }
      ]
    },

    "priority_flags": [
      {
        "flag": "High",
        "reason": "Beneficiaries approving their own funding (conflict of interest) — immediate governance integrity risk."
      },
      {
        "flag": "High",
        "reason": "Immutable recipient address policy combined with no pragmatic recovery mechanism — operational and custodial risk to funds."
      },
      {
        "flag": "Medium",
        "reason": "Undefined on-chain rules and thresholds for pausing/unpausing withdrawals and dispute resolution — leads to ambiguity when enforcement needed."
      },
      {
        "flag": "Medium",
        "reason": "No independent contract audit required prior to deployment — increases probability of exploitable vulnerabilities."
      },
      {
        "flag": "Medium",
        "reason": "Delegate Representative vote counts show stronger opposition than support — reputational/community acceptance risk that could impair governance legitimacy."
      }
    ],

    "recommended_next_steps_for_submitters_and_ada_holders": [
      "Amend the governance action to remove beneficiary self-approval: require community (Ada holder) approval or an independent approval path for Treasury Withdrawal Governance Actions funding CC compensation.",
      "Specify exact voting/quorum rules and encode them in the smart contract (pause/unpause thresholds, voting windows, tie-breaker rules).",
      "Define a secure emergency recipient recovery mechanism with multi-party checks, multi-sig and a time lock to avoid stranded funds and to enable remediation in key-loss scenarios.",
      "Require and publish a security audit/formal verification report of the customized smart contract(s) prior to funding and allow a public comment period on the audit findings.",
      "Add minimal periodic performance and financial reporting requirements (public deliverables), with non-compliance consequences (e.g., pause of future withdrawals, requirement to return funds).",
      "Clarify how 'service time' for pro-rata vesting is measured, verified, and computed on-chain or by a documented off-chain process.",
      "Consider adding an external oversight party or rotating independent reviewer to reduce collusion risk and increase community confidence."
    ],

    "overall_risk_summary": "The proposal is operationally detailed and includes several good guardrails (per-member contracts, vesting, return-to-treasury), but it contains high-priority governance and custodial risks: (1) beneficiaries approving their own payments; (2) rigid recipient immutability with no practical recovery; (3) unspecified vote/quorum rules for pause/dispute actions; and (4) lack of required independent audits. These issues should be remediated before widespread deployment or funding acceptance to reduce the chance of funds loss, governance capture, or community backlash."
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



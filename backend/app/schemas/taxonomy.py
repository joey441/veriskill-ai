from pydantic import BaseModel, Field
from typing import List, Dict

class DisciplineTaxonomy(BaseModel):
    discipline_id: str
    category: str
    skill_claim: str
    challenge_prompt: str
    live_constraint: str
    anomaly_threshold: float = 0.05
    required_verifiers: int = 2

VERTICAL_TAXONOMIES: Dict[str, DisciplineTaxonomy] = {
    "tech": DisciplineTaxonomy(
        discipline_id="tech-dev-001",
        category="Software Engineering",
        skill_claim="FastAPI Concurrency & Asyncio",
        challenge_prompt="Debug async worker pool deadlock in Python FastAPI service payload.",
        live_constraint="MUST_USE_BITWISE_MASK_NO_ASYNCIO_SLEEP",
        anomaly_threshold=0.05
    ),
    "finance": DisciplineTaxonomy(
        discipline_id="fin-acc-002",
        category="Financial Analysis",
        skill_claim="Balance Sheet Audit & Tax Reconciliation",
        challenge_prompt="Reconcile Q3 EBITDA liabilities against unearned revenue entries.",
        live_constraint="APPLY_2026_LOCALIZED_TAX_BRACKET_RULES",
        anomaly_threshold=0.08
    )
}

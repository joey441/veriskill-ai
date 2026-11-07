import os
import requests
from pydantic import BaseModel
# from fastapi import HTTPException  # Not needed currently
from ..schemas.taxonomy import DisciplineTaxonomy, VERTICAL_TAXONOMIES

MAX_VARIANCE = 0.15

def compute_consensus(sub):
    """Calculate consensus score and decide badge minting.
    `sub` is expected to be a dict‑like object with the fields defined in the
    `AuditSubmission` model from `app.main`. This avoids a circular import.
    """
    variance = abs(sub.eval_1 - sub.eval_2)
    if variance <= MAX_VARIANCE:
        final_score = (sub.eval_1 * sub.rep_1 + sub.eval_2 * sub.rep_2) / (sub.rep_1 + sub.rep_2)
        return {
            "status": "APPROVED",
            "consensus_score": round(final_score, 4),
            "variance": round(variance, 4),
            "mint_badge": True,
        }
    else:
        return {
            "status": "ESCALATED_TIEBREAKER",
            "variance": round(variance, 4),
            "mint_badge": False,
            "message": "Inter-verifier variance exceeded 0.15 threshold.",
        }

class SMSRequest(BaseModel):
    expert_phone: str
    candidate_claim: str

def dispatch_sms(req: SMSRequest):
    """Send an SMS via ThriveWave API. Returns a mock response on failure."""
    api_key = os.getenv("THRIVEWAVE_API_KEY", "demo_thrivewave_key")
    sms_url = "https://api.thrivewave.io/v1/sms/send"
    payload = {
        "to": req.expert_phone,
        "message": f"VeriSkill Alert: Audit request for [{req.candidate_claim}]. Review: https://veriskill.rumptycloud.app/audit/token_8291",
        "sender_id": "VeriSkill",
    }
    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        response = requests.post(sms_url, json=payload, headers=headers, timeout=5)
        response.raise_for_status()
        return {
            "status": "SUCCESS",
            "provider": "ThriveWave SMS API",
            "recipient": req.expert_phone,
            "dispatched_message": payload["message"],
            "response": response.json(),
        }
    except Exception as e:
        return {
            "status": "SUCCESS_MOCK",
            "recipient": req.expert_phone,
            "note": "Demo fallback active",
            "error": str(e),
        }

class AuditSubmission(BaseModel):
    # Define your fields here
    audit_id: str
    status: str
MAX_VARIANCE = 0.15

def compute_consensus(sub: AuditSubmission):
    """Calculate consensus score and decide badge minting.
    Returns a dict compatible with FastAPI JSON response.
    """
    variance = abs(sub.eval_1 - sub.eval_2)
    if variance <= MAX_VARIANCE:
        final_score = (sub.eval_1 * sub.rep_1 + sub.eval_2 * sub.rep_2) / (sub.rep_1 + sub.rep_2)
        return {
            "status": "APPROVED",
            "consensus_score": round(final_score, 4),
            "variance": round(variance, 4),
            "mint_badge": True,
        }
    else:
        # Escalate to tie-breaker flow (could be extended later)
        return {
            "status": "ESCALATED_TIEBREAKER",
            "variance": round(variance, 4),
            "mint_badge": False,
            "message": "Inter-verifier variance exceeded 0.15 threshold.",
        }
class SMSRequest(BaseModel):
    expert_phone: str
    candidate_claim: str


def dispatch_sms(req: SMSRequest):
    """Send an SMS via ThriveWave API. In case of failure, return a mock response.
    """
    api_key = os.getenv("THRIVEWAVE_API_KEY", "demo_thrivewave_key")
    sms_url = "https://api.thrivewave.io/v1/sms/send"
    payload = {
        "to": req.expert_phone,
        "message": f"VeriSkill Alert: Audit request for [{req.candidate_claim}]. Review: https://veriskill.rumptycloud.app/audit/token_8291",
        "sender_id": "VeriSkill",
    }
    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        response = requests.post(sms_url, json=payload, headers=headers, timeout=5)
        response.raise_for_status()
        return {
            "status": "SUCCESS",
            "provider": "ThriveWave SMS API",
            "recipient": req.expert_phone,
            "dispatched_message": payload["message"],
            "response": response.json(),
        }
    except Exception as e:
        # Return mock payload for demo / offline dev environments
        return {
            "status": "SUCCESS_MOCK",
            "recipient": req.expert_phone,
            "note": "Demo fallback active",
            "error": str(e),
        }

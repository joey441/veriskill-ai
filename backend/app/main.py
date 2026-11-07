import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .services.consensus import compute_consensus, dispatch_sms

app = FastAPI(title="VeriSkill AI Engine", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AuditSubmission(BaseModel):
    discipline: str
    candidate_id: str
    eval_1: float
    eval_2: float
    rep_1: float = 1.0
    rep_2: float = 1.0

class SMSRequest(BaseModel):
    expert_phone: str
    candidate_claim: str

@app.get("/health")
def health_check():
    return {
        "status": "online",
        "platform": "RumptyCloud",
        "engine": "VeriSkill AI Core v1.0",
        "partner_services": ["RumptyCloud Container Host", "ThriveWave SMS Gateway"],
    }

@app.post("/api/v1/consensus")
def evaluate_consensus(sub: AuditSubmission):
    return compute_consensus(sub)

@app.post("/api/v1/sms/dispatch")
def trigger_thrivewave_sms(req: SMSRequest):
    return dispatch_sms(req)

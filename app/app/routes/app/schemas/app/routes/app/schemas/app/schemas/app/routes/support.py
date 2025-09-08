from fastapi import APIRouter
from app.schemas.support import IssueRequest, IssueResponse
import hanifx

router = APIRouter(
    prefix="/support",
    tags=["Support"]
)

@router.post("/report", response_model=IssueResponse)
def report_issue(payload: IssueRequest):
    status = hanifx.report_issue(payload.message)
    return {"message": payload.message, "status": status}

from fastapi import APIRouter
from app.schemas.scanner import ScanRequest, ScanResponse
import hanifx

router = APIRouter(
    prefix="/scanner",
    tags=["Scanner"]
)

@router.post("/file", response_model=ScanResponse)
def scan_file(payload: ScanRequest):
    result = hanifx.scan_code(payload.file_path)
    return {"file_path": payload.file_path, "scan_result": result}

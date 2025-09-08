from pydantic import BaseModel

class ScanRequest(BaseModel):
    file_path: str

class ScanResponse(BaseModel):
    file_path: str
    scan_result: str

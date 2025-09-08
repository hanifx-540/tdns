from pydantic import BaseModel

class IssueRequest(BaseModel):
    message: str

class IssueResponse(BaseModel):
    message: str
    status: str

from pydantic import BaseModel

class EncodeRequest(BaseModel):
    text: str

class EncodeResponse(BaseModel):
    input: str
    encoded: str

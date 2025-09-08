from fastapi import APIRouter
import hanifx
from app.schemas.encoder import EncodeRequest, EncodeResponse

router = APIRouter(
    prefix="/encode",
    tags=["Encoder"]
)

@router.post("/text", response_model=EncodeResponse)
def encode_text(payload: EncodeRequest):
    encoded = hanifx.encode(payload.text)  # Encode-only
    return {"input": payload.text, "encoded": encoded}

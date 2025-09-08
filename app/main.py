from fastapi import FastAPI
from app.routes import encrypt_decrypt, scanner, support

app = FastAPI(
    title="HanifX API",
    description="Module-wise API for HanifX v24.0.0",
    version="1.0.0"
)

# Include module-wise routers
app.include_router(encrypt_decrypt.router)
app.include_router(scanner.router)
app.include_router(support.router)

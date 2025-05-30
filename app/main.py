from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import router as v1_router

app = FastAPI(
    title="Zavvis AI CFO Backend",
    description="APIs for cash flow forecasting, insights, QuickBooks integration, and more.",
    version="1.0.0"
)

# Enable CORS (update origins for frontend domain)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register versioned API
app.include_router(v1_router, prefix="/api/v1")

# Root health check
@app.get("/")
def read_root():
    return {"message": "Zavvis AI CFO backend is running 🚀"}

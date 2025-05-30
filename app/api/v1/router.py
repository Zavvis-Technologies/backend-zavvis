from fastapi import APIRouter
from app.api.v1.modules.auth.endpoints import router as auth_router
# from app.api.v1.modules.cashflow.endpoints import router as cashflow_router
# Add others as needed

router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["Auth"])

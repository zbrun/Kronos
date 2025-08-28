from fastapi import APIRouter

from web.app.api.v1 import agi

api_router = APIRouter()
api_router.include_router(agi.router, prefix="/v1", tags=["agis"])

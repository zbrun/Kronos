from fastapi import APIRouter

from web.app.model.Response import Response

router = APIRouter()

@router.get("/agi", response_model=Response)
def test_agi():
    res = Response()
    return res

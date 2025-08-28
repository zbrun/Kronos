from typing import Generic, TypeVar, Optional
from pydantic.generics import GenericModel

T = TypeVar("T")

class Response(GenericModel, Generic[T]):
    code: int = 0
    message: str = "success"
    data: Optional[T] = None
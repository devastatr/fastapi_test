from typing import Optional

from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    deck: Optional[str] = None


class STask(STaskAdd):
    id: int

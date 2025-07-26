from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TeamModel(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, example="Natus Vincere")
    private: bool = Field(False, description="Вказує, чи є команда приватною (наприклад, для внутрішніх тестів)")

class TeamModelResponse(TeamModel):
    id: str

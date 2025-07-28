from pydantic import BaseModel, Field
from typing import Optional

from app.db.tournaments.db_actions import Vote
from app.db.teams.models import Team
from app.db.tournaments.model import Tournament


class TournamentModel(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, example="Champions League")
    exp_days: int = Field(7, ge=1, le=365, example=14, description="Кількість днів до завершення турніру")

class TournamentModelResponse(TournamentModel):
    id: str = Field(..., example="abc123")

class VoteModel(BaseModel):
    team_id: str = Field(..., example="team42")
    tournament_id: str = Field(..., example="tournament99")
    vote: Vote = Field(..., description="Тип голосу (enum)")

class ResultModel(BaseModel):
    team_name: str = Field(..., example="FC Example")
    tournament_name: str = Field(..., example="Champions League")
    result: float = Field(..., ge=0, example=12.5, description="Результат команди (наприклад, очки)")
    vote_result: int = Field(..., example=42, description="Кількість голосів за команду")
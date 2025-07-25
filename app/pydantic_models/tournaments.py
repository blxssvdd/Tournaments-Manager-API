from pydantic import BaseModel, Field

from app.db.tournaments.db_actions import Vote
from app.db.teams.models import Team
from app.db.tournaments.model import Tournament


class TournamentModel(BaseModel):
    name: str = Field(...)
    exp_days: int = Field(7)


class TournamentModelResponse(TournamentModel):
    id: str


class VoteModel(BaseModel):
    team_id: str
    tournament_id: str
    vote: Vote


class ResultModel(BaseModel):
    team_name: str
    tournament_name: str
    result: float
    vote_result: int

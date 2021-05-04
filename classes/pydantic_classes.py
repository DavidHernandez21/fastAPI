from enum import Enum
from pydantic import BaseModel, Field #PositiveInt
from typing import  Optional


class Team(str, Enum):
    home: str="home"
    away: str="away"


class Score(BaseModel):
    away : int=Field(0, title="Away", ge=0)
    home : int=Field(0, title="Home", ge=0)



class Goal(BaseModel):
    team: Team
    player: Optional[str]=Field(None, title="Player")

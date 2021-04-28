from fastapi import FastAPI #, Query
import uvicorn
import fastapi
from enum import Enum
from pydantic import BaseModel, Field #PositiveInt
from typing import List
from typing import Optional

app = FastAPI()



class Team(str, Enum):
    home: str="home"
    away: str="away"


class Score(BaseModel):
    away : int=Field(0, title="Away", ge=0)
    home : int=Field(0, title="Home", ge=0)




class Goal(BaseModel):
    team: Team
    player: Optional[str]=Field(None, title="Player")
    

actual_score = Score().dict()


@app.get("/score", response_model=Score)
async def get_score():
    return actual_score


@app.post("/goal", response_model=Score)
async def post_goal(team: Goal):
    goal = team.dict()
    if goal['team'].value == "away":
        # actual_score['away'] = actual_score['away'] + 1
        actual_score.update({"away": actual_score['away'] + 1})
        return actual_score

    elif goal['team'].value == "home":
        # actual_score['away'] = actual_score['away'] + 1
        actual_score.update({"home": actual_score['home'] + 1})
        return actual_score


uvicorn.run(app, port=8080)


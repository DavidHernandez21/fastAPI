from fastapi import FastAPI
from classes.pydantic_classes import Score, Goal
from typing import List
# import uvicorn

app = FastAPI()


players: List[Goal] = []


def actual_score() -> Score:
    return Score(
        home=sum((1 for p in players if p.team == "home")),
        away=sum((1 for p in players if p.team == "away")),
    )


@app.get("/score", response_model=Score)
async def get_score():
    return actual_score()


@app.post("/goal", response_model=Score)
async def post_goal(goal: Goal):
    players.append(goal)
    return actual_score()


@app.get("/players", response_model=List[Goal])
async def get_players():
    return players


# uvicorn.run(app, port=8081)


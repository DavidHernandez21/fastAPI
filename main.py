from fastapi import FastAPI #, Query
import uvicorn
from classes.pydantic_classes import Team, Score, Goal
from utils.functions import add_goal


app = FastAPI()

    

actual_score = Score().dict()


@app.get("/score", response_model=Score)
async def get_score():
    return actual_score


@app.post("/goal", response_model=Score)
async def post_goal(team: Goal):
    return add_goal(team, actual_score)


uvicorn.run(app, port=8081)


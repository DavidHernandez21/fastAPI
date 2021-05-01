from fastapi import FastAPI #, Query
import uvicorn
from classes.pydantic_classes import Team, Score, Goal


app = FastAPI()

    

actual_score = Score().dict()


@app.get("/score", response_model=Score)
async def get_score():
    return actual_score


@app.post("/goal", response_model=Score)
async def post_goal(team: Goal):
    goal = team.dict()
    if goal['team'].value == "away":
        actual_score.update({"away": actual_score['away'] + 1})
        return actual_score

    elif goal['team'].value == "home":
        actual_score.update({"home": actual_score['home'] + 1})
        return actual_score


uvicorn.run(app, port=8080)


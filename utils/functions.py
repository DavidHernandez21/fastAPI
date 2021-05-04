from typing import Dict
from classes.pydantic_classes import Goal


def add_goal(team: Goal, actual_score:Dict)-> Dict:
    goal = team.dict()
    if goal['team'].value == "away":
        actual_score.update({"away": actual_score['away'] + 1})
        return actual_score

    
    actual_score.update({"home": actual_score['home'] + 1})
    return actual_score
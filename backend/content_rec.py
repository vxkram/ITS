# Assuming results_1.py is in the same directory
from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from results_1 import get_latest_quiz_result  # Import the function

app = FastAPI()

class Resource(BaseModel):
    title: str
    url: str

categorized_resources = {
    "Beginner": [
        Resource(title="Introduction to DBMS", url="https://youtu.be/X7v0O8yiUuY"),
        Resource(title="DBMS Tutorial GeeksforGeeks", url="https://www.geeksforgeeks.org/dbms/")
    ],
    "Intermediate": [
        Resource(title="Normalization in DBMS", url="https://youtu.be/5nGC4fyFPes"),
        Resource(title="Understanding SQL", url="https://youtu.be/wmiDdBG-yP4")
    ],
    "Advanced": [
        Resource(title="Advanced Database Concepts", url="https://youtu.be/ABwD8IYByfk"),
        Resource(title="SQL Queries Tutorial", url="https://youtu.be/0buKQHokLK8")
    ]
}

@app.get("/recommend-resources/", response_model=List[Resource])
async def recommend_resources():
    latest_result = get_latest_quiz_result()  # Use the imported function
    if not latest_result:
        raise HTTPException(status_code=404, detail="Latest quiz result not found.")
    
    score = latest_result["score"] if "score" in latest_result else 0

    if score <= 40:
        recommended_level = "Beginner"
    elif 40 < score <= 70:
        recommended_level = "Intermediate"
    else:
        recommended_level = "Advanced"

    return categorized_resources[recommended_level]

# from fastapi import FastAPI, HTTPException
# from fastapi.responses import JSONResponse, FileResponse
# from pydantic import BaseModel
# from typing import List, Dict
# import json
# from datetime import datetime
# import matplotlib.pyplot as plt
# import os

# app = FastAPI()

# class QuizScore(BaseModel):
#     score: float
#     timestamp: datetime

# class Resource(BaseModel):
#     title: str
#     url: str

# categorized_resources = {
#     "Beginner": [
#         {"title": "Introduction to DBMS", "url": "https://youtu.be/X7v0O8yiUuY"},
#         {"title": "DBMS Tutorial - GeeksforGeeks", "url": "https://www.geeksforgeeks.org/dbms/"}
#     ],
#     "Intermediate": [
#         {"title": "Normalization in DBMS", "url": "https://youtu.be/5nGC4fyFPes"},
#         {"title": "Understanding SQL", "url": "https://youtu.be/wmiDdBG-yP4"}
#     ],
#     "Advanced": [
#         {"title": "Advanced Database Concepts", "url": "https://youtu.be/ABwD8IYByfk"},
#         {"title": "SQL Queries Tutorial", "url": "https://youtu.be/0buKQHokLK8"}
#     ]
# }

# def get_latest_quiz_score() -> float:
#     file_path = "D:/PROJECT/Newfolder/its/backend/database/quiz_results.json"
#     try:
#         with open(file_path, "r") as file:
#             scores = json.load(file)
#         if not scores:
#             raise HTTPException(status_code=404, detail="No quiz results found.")
#         latest_score = scores[-1]["score"]  # Direct access to the score
#         return latest_score
#     except (FileNotFoundError, IndexError, KeyError) as e:
#         raise HTTPException(status_code=404, detail=f"Quiz results processing error: {str(e)}")

# @app.get("/recommend-content/", response_model=List[Resource])
# def recommend_content():
#     latest_score = get_latest_quiz_score()
#     if latest_score <= 40:
#         recommended_level = "Beginner"
#     elif 40 < latest_score <= 70:
#         recommended_level = "Intermediate"
#     else:
#         recommended_level = "Advanced"


#     recommended_resources = [Resource(**res) for res in categorized_resources[recommended_level]]
#     return recommended_resources

# # Add other endpoints as necessary


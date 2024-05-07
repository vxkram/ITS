#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime
import json

app = FastAPI()

class Question(BaseModel):
    question: str
    options: List[str]
    answer: str

class Answer(BaseModel):
    answers: Dict[int, str]

# Static questions data (simplified for the example).
questions_data = [
    {"question": "What does DBMS stand for?", "options": ["Data Boxing Management System", "Database Management System", "Data Backup Management System", "None of the above"], "answer": "Database Management System"},
    # Add more questions as needed
]

@app.get("/quiz_3/", response_model=List[Question])
async def get_quiz():
    # Omit sending the 'answer' key to the client
    return [{"question": q["question"], "options": q["options"]} for q in questions_data]

@app.post("/quiz_3/evaluate/")
async def evaluate_quiz(answers: Answer):
    correct_count = 0
    for idx, user_answer in answers.answers.items():
        if questions_data[idx]['answer'] == user_answer:
            correct_count += 1
    score = correct_count / len(questions_data) * 100
    
    save_score(score)  # Call function to save the score
    
    return {"correct_count": correct_count, "score": score}

def save_score(score):
    """Save the score to a JSON file."""
    file_path = "quiz_scores.json"
    score_entry = {"score": score, "timestamp": datetime.now().isoformat()}
    
    try:
        with open(file_path, "r") as file:
            scores = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        scores = []
    
    scores.append(score_entry)
    
    with open(file_path, "w") as file:
        json.dump(scores, file, indent=4)


# In[ ]:





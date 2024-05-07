from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

class Question(BaseModel):
    question: str
    options: List[str]
    answer: str

questions = [
    {
        "question": "What does DBMS stand for?",
        "options": ["Data Boxing Management System", "Database Management System", "Data Backup Management System", "None of the above"],
        "answer": "Database Management System"
    },
    # Add the rest of your questions here
]

@app.get("/quiz_2/", response_model=List[Question])
async def get_quiz():
    return questions

class QuizAnswers(BaseModel):
    answers: Dict[int, str]  # question index: selected option

@app.post("/quiz_2/evaluate/")
async def evaluate_quiz(quiz_answers: QuizAnswers):
    correct_count = 0
    for idx, answer in quiz_answers.answers.items():
        if questions[idx]["answer"] == answer:
            correct_count += 1
    total_questions = len(questions)
    return {"correct": correct_count, "total": total_questions, "score": correct_count / total_questions * 100}



 





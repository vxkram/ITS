
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import random
import json
from datetime import datetime
from pathlib import Path

app = FastAPI()

class Question(BaseModel):
    question: str
    options: List[str]
    answer: str

class QuizSubmission(BaseModel):
    answers: Dict[str, str]

def load_questions() -> List[Dict]:
    file_path = Path("D:/PROJECT/Newfolder/its/backend/database/question_bank_dbms.json")
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Question bank not found")
    with file_path.open("r") as file:
        questions = json.load(file)
    return questions

@app.get("/quiz/", response_model=List[Question])
async def get_quiz_questions():
    questions = load_questions()
    return random.sample(questions, min(len(questions), 10))

@app.post("/quiz/")
async def submit_quiz(submission: QuizSubmission):
    questions = load_questions()
    score = calculate_score(submission.answers, questions)
    save_score(score)
    return {"message": f"You scored {score}% on this quiz."}

def calculate_score(user_answers: Dict[str, str], questions: List[Dict]) -> float:
    correct_answers = 0
    for question in questions:
        # Match each question with the answer provided by the user.
        if user_answers.get(question["question"]) == question["answer"]:
            correct_answers += 1
    # return correct_answers / len(questions) * 100 if questions else 0
    return correct_answers / 10 * 100 if questions else 0


def save_score(user_answers: Dict[str, str], questions: List[Dict], score: float):
    file_path = Path("D:/PROJECT/Newfolder/its/backend/database/quiz_results.json")
    
    # Load existing quiz results if the file exists
    if file_path.exists():
        with file_path.open("r") as file:
            quiz_results = json.load(file)
    else:
        quiz_results = []

    # Prepare the new quiz result entry
    new_quiz_result = {
        "timestamp": datetime.now().isoformat(),
        "score": score,
        "details": []
    }

    # Add each question and the user's answer to the result entry
    for question in questions:
        new_quiz_result["details"].append({
            "question": question["question"],
            "correct_answer": question["answer"],
            "user_answer": user_answers.get(question["question"], "No Answer")
        })

    # Append the new quiz result to the list and save it back to the file
    quiz_results.append(new_quiz_result)
    with file_path.open("w") as file:
        json.dump(quiz_results, file, indent=4)









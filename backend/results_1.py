# from fastapi import FastAPI, HTTPException
# from fastapi.responses import FileResponse
# import json
# from datetime import datetime
# import matplotlib.pyplot as plt
# from typing import Optional

# app = FastAPI()

# def save_plot_scores():
#     file_path = "D:/PROJECT/Newfolder/its/backend/database/quiz_scores.json"
#     output_path = "D:/PROJECT/Newfolder/its/quiz_scores_plot.png"
#     try:
#         with open(file_path, "r") as file:
#             scores = json.load(file)
#     except FileNotFoundError:
#         raise HTTPException(status_code=404, detail="Score file not found. Please take some quizzes first.")

#     if not scores:
#         raise HTTPException(status_code=404, detail="No scores to plot.")

#     # Extracting scores and timestamps
#     score_values = [score["score"] for score in scores]
#     timestamps = [datetime.fromisoformat(score["timestamp"]).strftime('%Y-%m-%d %H:%M:%S') for score in scores]

#     # Plotting
#     plt.figure(figsize=(10, 6))
#     plt.plot(timestamps, score_values, marker='o', linestyle='-', color='b')
#     plt.title('Quiz Scores Over Time')
#     plt.xlabel('Attempt Timestamp')
#     plt.ylabel('Score (%)')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
    
#     # Saving the plot to file
#     plt.savefig(output_path)
#     plt.close()

# @app.get("/plot-scores/")
# def get_plot_scores():
#     plot_image_path = "D:/PROJECT/Newfolder/its/quiz_scores_plot.png"
#     save_plot_scores()  # This ensures the plot is generated/updated before being served.
#     return FileResponse(plot_image_path)

# @app.get("/latest-quiz-result/")
# def get_latest_quiz_result():
#     file_path = "D:/PROJECT/Newfolder/its/backend/database/quiz_results.json"
#     try:
#         with open(file_path, "r") as file:
#             scores = json.load(file)
#     except FileNotFoundError:
#         raise HTTPException(status_code=404, detail="No quiz results found.")

#     if not scores:
#         return {"message": "No quiz results available yet."}

#     latest_score = scores[-1]  # Get the most recent score
#     return {"message": f"You scored {latest_score['score']}% on your last quiz."}

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import json
from datetime import datetime
import matplotlib.pyplot as plt
from typing import Optional
import os

app = FastAPI()

def save_plot_scores():
    file_path = "D:/PROJECT/Newfolder/its/backend/database/quiz_results.json"
    output_path = "D:/PROJECT/Newfolder/its/backend/database/quiz_scores_plot.png"
    try:
        with open(file_path, "r") as file:
            scores = json.load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Score file not found. Please take some quizzes first.")

    if not scores:
        raise HTTPException(status_code=404, detail="No scores to plot.")

    score_values = [score["score"] for score in scores]
    timestamps = [datetime.fromisoformat(score["timestamp"]).strftime('%Y-%m-%d %H:%M:%S') for score in scores]

    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, score_values, marker='o', linestyle='-', color='b')
    plt.title('Quiz Scores Over Time')
    plt.xlabel('Attempt Timestamp')
    plt.ylabel('Score (%)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

@app.get("/plot-scores/")
def get_plot_scores():
    plot_image_path = "D:/PROJECT/Newfolder/its/backend/database/quiz_scores_plot.png"
    save_plot_scores()
    if not os.path.exists(plot_image_path):
        raise HTTPException(status_code=404, detail="Plot image not found.")
    return FileResponse(plot_image_path)


@app.get("/latest-quiz-result/")
def get_latest_quiz_result():
    file_path = "D:/PROJECT/Newfolder/its/backend/database/quiz_results.json"
    try:
        with open(file_path, "r") as file:
            scores = json.load(file)
    except FileNotFoundError:
        return {"message": "No quiz results found."}

    if not scores:
        return {"message": "No quiz results available yet."}
    
    latest_score = scores[-1]
    score_value = latest_score['score']

    if score_value <= 40:
        message = f"You scored {score_value}% on your last quiz. You seem to be unfamiliar with DBMS."
    elif 40 < score_value <= 70:
        message = f"You scored {score_value}% on your last quiz. You seem to be unfamiliar with SQL and lacking clarity on the concept of keys"
    else:
        message = f"You scored {score_value}% on your last quiz. You seem to be good with the concepts of DBMS. Lets practice a bit more to master it😎 "

    return {"message": message}
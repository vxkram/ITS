#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fastapi import FastAPI, HTTPException
import json
from datetime import datetime

app = FastAPI()

def get_latest_scores(file_path):
    """
    Fetches the two most recent scores from the scores file.
    """
    try:
        with open(file_path, "r") as file:
            scores = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None, None

    if len(scores) < 2:
        return scores[-1] if scores else None, None
    else:
        return scores[-2], scores[-1]

def recommend_based_on_progress(file_path="D:\\PROJECT\\Newfolder\\its\\backend\\database\\quiz_scores.json"):
    """
    Analyzes the two most recent quiz scores and recommends next steps.
    """
    previous_score_entry, current_score_entry = get_latest_scores(file_path)

    if not current_score_entry:
        return {
            "message": "Not enough data for recommendations. Please take more quizzes."
        }
    
    current_score = current_score_entry[' score']
    recommendation = ""

    if previous_score_entry:
        previous_score = previous_score_entry['score']
        improvement = current_score - previous_score

        if improvement > 10:
            recommendation = "Significant improvement observed! Consider tackling more advanced topics."
        elif improvement >= 0:
            recommendation = "Slight improvement. Solidify current topics before moving on."
        else:
            recommendation = "Score has decreased. Review the material again and try different study methods."
    else:
        if current_score >= 90:
            recommendation = "Excellent score! Feel free to explore more advanced topics."
        elif current_score >= 75:
            recommendation = "Good job! Some review might still be beneficial."
        else:
            recommendation = "Consider revisiting the topics. Experiment with different learning methods."
    
    return {
        "latest_score": current_score,
        "recommendation": recommendation
    }

@app.get("/recommendations/")
async def get_recommendations():
    """
    Endpoint to get recommendations based on quiz scores.
    """
    recommendations = recommend_based_on_progress()
    return recommendations


# In[ ]:





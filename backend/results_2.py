#!/usr/bin/env python
# coding: utf-8

# In[2]:


# In[3]:


from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import matplotlib.pyplot as plt
import json
import uuid

app = FastAPI()

# Mount a static directory to serve files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Placeholder for a simple quiz with correct answers
# In a real application, you would likely store this data in a database
QUIZ_ANSWERS = {"1": "A", "2": "B", "3": "C"}

@app.post("/submit_quiz/")
async def submit_quiz(answers: dict):
    # Calculate correct answers
    correct_statuses = [answers[str(q)] == a for q, a in QUIZ_ANSWERS.items()]
    
    # Generate and save the plot
    plot_filename = save_quiz_results_plot(correct_statuses)
    
    # Return the URL to access the plot image
    return {"plot_url": f"/static/{plot_filename}"}

def save_quiz_results_plot(correct_statuses, directory="static"):
    # Generate unique filename
    filename = f"{uuid.uuid4()}.png"
    filepath = f"{directory}/{filename}"
    
    question_labels = [f"Q{index+1}" for index, _ in enumerate(QUIZ_ANSWERS)]
    bar_heights = [1 for _ in correct_statuses] 
    colors = ['green' if status else 'red' for status in correct_statuses]
    
    plt.figure(figsize=(10, 5))
    plt.bar(question_labels, bar_heights, color=colors)
    plt.xlabel('Questions')
    plt.ylabel('Correctness')
    plt.title('Quiz Results: Correct (Green) vs Incorrect (Red)')
    plt.xticks(rotation=45)
    plt.yticks([0, 1], ['Incorrect', 'Correct'])
    plt.tight_layout()
    plt.savefig(filepath)
    plt.close()
    
    return filename


# In[ ]:





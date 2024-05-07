#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()

class UserChoice(str, Enum):
    quiz = "quiz"
    content = "content"

@app.get("/")
async def read_root():
    return {"message": "Welcome to the ITS. Use /choose/{user_choice} to make a choice."}

@app.get("/choose/{user_choice}")
async def choose_path(user_choice: UserChoice):
    if user_choice == UserChoice.quiz:
        return {"message": "You've chosen to take the preliminary quiz."}
        # Redirect to quiz logic or return quiz-related data
    elif user_choice == UserChoice.content:
        return {"message": "You've chosen to begin with the course content."}
        # Redirect to content logic or return content-related data
    else:
        raise HTTPException(status_code=404, detail="Choice not found")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[3]:


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StudyStatus(BaseModel):
    finished_studying: bool

@app.post("/study-status/")
async def study_status(status: StudyStatus):
    if status.finished_studying:
        return {"message": "Great! Let's move on to the next topic."}
    else:
        return {"message": "Let's take a step back and revisit the previous topics to reinforce your understanding."}


# In[ ]:





# import requests
# from bs4 import BeautifulSoup
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import sent_tokenize, word_tokenize
# from collections import defaultdict
# import heapq
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# # Ensure that NLTK resources are downloaded
# nltk.download('punkt')
# nltk.download('stopwords')

# app = FastAPI()

# class URL(BaseModel):
#     url: str

# def scrape_website(url):
#     """Fetches content from a website and returns the text."""
#     try:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         paragraphs = soup.find_all('p')
#         article_text = ' '.join([para.get_text() for para in paragraphs])
#         return article_text
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

# def clean_text(text):
#     """Cleans the text by removing stopwords and punctuation."""
#     text = text.lower()
#     cleaned_text = ''
#     for char in text:
#         if char.isalnum() or char.isspace():
#             cleaned_text += char

#     stop_words = set(stopwords.words('english'))
#     words = word_tokenize(cleaned_text)
#     cleaned_words = [word for word in words if word not in stop_words]
#     return cleaned_words

# def summarize_text(text, sentence_count=3):
#     """Summarizes the text by picking the most relevant sentences."""
#     sentence_scores = defaultdict(int)
#     sentences = sent_tokenize(text)
#     word_frequencies = nltk.FreqDist(clean_text(text))

#     for sentence in sentences:
#         for word in word_tokenize(sentence.lower()):
#             if word in word_frequencies:
#                 sentence_scores[sentence] += word_frequencies[word]

#     summary_sentences = heapq.nlargest(sentence_count, sentence_scores, key=sentence_scores.get)
#     return ' '.join(summary_sentences)

# @app.post("/summarize/")
# def summarize(url: URL):
#     text = scrape_website(url.url)
#     if not text:
#         raise HTTPException(status_code=404, detail="No text found on the page")
#     summary = summarize_text(text, sentence_count=5)
#     return {"summary": summary}

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict
import heapq
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
import fitz  # PyMuPDF
from pydantic import BaseModel

# Ensure that NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

app = FastAPI()

def extract_text_from_pdf(file_path):
    """Extracts text from a PDF file."""
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def clean_text(text):
    """Cleans the text by removing stopwords and punctuation."""
    text = text.lower()
    cleaned_text = ''
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned_text += char

    stop_words = set(stopwords.words('english'))
    words = word_tokenize(cleaned_text)
    cleaned_words = [word for word in words if word not in stop_words]
    return cleaned_words

def summarize_text(text, sentence_count=3):
    """Summarizes the text by picking the most relevant sentences."""
    sentence_scores = defaultdict(int)
    sentences = sent_tokenize(text)
    word_frequencies = nltk.FreqDist(clean_text(text))

    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] += word_frequencies[word]

    summary_sentences = heapq.nlargest(sentence_count, sentence_scores, key=sentence_scores.get)
    return ' '.join(summary_sentences)

@app.post("/summarize/")
async def summarize(pdf_file: UploadFile = File(...)):
    if pdf_file.content_type != 'application/pdf':
        raise HTTPException(status_code=415, detail="Unsupported file type.")
    
    # Save PDF temporarily (consider using a more permanent storage or processing in memory)
    temp_file_path = f"/tmp/{pdf_file.filename}"
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(await pdf_file.read())
    
    # Extract text and summarize
    text = extract_text_from_pdf(temp_file_path)
    if not text:
        return JSONResponse(status_code=204, content={"message": "No text found in the PDF."})
    
    summary = summarize_text(text, sentence_count=5)
    return {"summary": summary}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

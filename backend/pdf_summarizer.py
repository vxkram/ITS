

# from fastapi import FastAPI, HTTPException
# from fastapi.responses import FileResponse
# import requests
# from bs4 import BeautifulSoup
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet

# app = FastAPI()

# @app.get("/generate-summary/")
# async def generate_summary():
#     try:
#         # URL of the webpage to summarize
#         url = 'https://www.techtarget.com/searchdatamanagement/definition/database-management-system'
#         response = requests.get(url)
#         soup = BeautifulSoup(response.content, 'html.parser')

#         # Extract text content
#         content_items = soup.find_all(['h1', 'h2', 'h3', 'p'])
#         content = ''.join(item.text.strip() for item in content_items if item.text.strip() != '')

#         # The 'enhanced_summary' variable should contain your summarized content
#         # Assuming 'content' is already a summarized version for this example
#         enhanced_summary = "Database Management Systems (DBMS) Overview:- DBMS are pivotal in creating, managing, and manipulating databases, providing a systematic approach to data management.- They support various database models, including relational, NoSQL, and in-memory databases, each serving different needs.Key Functions:- Data Storage, Retrieval, and Update: DBMS stores data in an organized manner, allows for efficient retrieval, and supports updates to ensure data remains current.- Data Security: Implements access controls and authentication measures to safeguard data.- Data Integrity: Maintains data accuracy and consistency through integrity constraints.- Backup and Recovery: Ensures data preservation and recovery mechanisms are in place to handle system failures.Advantages of Using a DBMS:- Improved data sharing and data security.- Better data integration and minimized data inconsistency.- Enhanced data access and responsiveness to user queries.- Increased end-user productivity.Types of DBMS:- Relational DBMS (RDBMS): Uses a table-based structure and SQL for data manipulation. Examples include MySQL, PostgreSQL, and Oracle.- NoSQL DBMS: Designed for unstructured data and scalability challenges, supporting document, key-value, wide-column, and graph databases. Examples include MongoDB, Cassandra, and Neo4j.- In-memory DBMS: Stores data in the main memory to achieve faster response times. Examples include Redis and SAP HANA.Choosing the Right DBMS:- The selection depends on the specific requirements, such as data complexity, scalability needs, and performance criteria. Consider factors like data model support, transaction throughput, and ecosystem compatibility."

#         # Generating PDF
#         filename = "DBMS_Enhanced_Summary.pdf"
#         filepath = "D:\\PROJECT\\Newfolder\\its\\backend\\database\\" + filename
#         doc = SimpleDocTemplate(filepath, pagesize=letter)
#         styles = getSampleStyleSheet()
#         style = styles["Normal"]

#         # Assuming your summary might contain multiple paragraphs separated by two newlines
#         paragraphs = enhanced_summary.split("\n\n")
#         parts = [Paragraph(p.replace("\n", "<br />"), style) for p in paragraphs]

#         doc.build(parts)

#         # Return the generated PDF file to the client
#         return FileResponse(filepath, media_type='application/pdf')

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))





import os
import fitz  # PyMuPDF
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict
import heapq
from fpdf import FPDF

# Ensure that NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

pdf_directory = "D:/PROJECT/Newfolder/its/backend/database/pdf/" 
# Directory containing PDFs


# def list_pdf_files():
#     """Lists PDF files in the directory."""
#     files = os.listdir(pdf_directory)
#     return [{"id": i, "title": file, "file_path": os.path.join(pdf_directory, file)} for i, file in enumerate(files, start=1) if file.endswith('.pdf')]

# def extract_text_from_pdf(file_path):
#     """Extracts text from a PDF file."""
#     text = ""
#     doc = fitz.open(file_path)
#     for page in doc:
#         text += page.get_text()
#     doc.close()
#     return text

# def clean_text(text):
#     """Cleans text by removing stopwords and non-alphanumeric characters."""
#     text = text.lower()
#     cleaned_text = ''.join(char for char in text if char.isalnum() or char.isspace())
#     stop_words = set(stopwords.words('english'))
#     words = word_tokenize(cleaned_text)
#     return [word for word in words if word not in stop_words]

# def summarize_text(text, sentence_count=5):
#     """Summarizes text by selecting the most relevant sentences."""
#     sentence_scores = defaultdict(int)
#     sentences = sent_tokenize(text)
#     word_frequencies = nltk.FreqDist(clean_text(text))
#     for sentence in sentences:
#         for word in word_tokenize(sentence.lower()):
#             if word in word_frequencies:
#                 sentence_scores[sentence] += word_frequencies[word]
#     summary_sentences = heapq.nlargest(sentence_count, sentence_scores, key=sentence_scores.get)
#     return ' '.join(summary_sentences)

# def create_summary_pdf(summary_text, output_path):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size = 12)
#     pdf.multi_cell(0, 10, summary_text)
#     pdf.output(output_path)

def list_pdf_files():
    files = os.listdir(pdf_directory)
    return [{"id": i, "title": file, "file_path": os.path.join(pdf_directory, file)} for i, file in enumerate(files, start=1) if file.endswith('.pdf')]

def extract_text_from_pdf(file_path):
    text = ""
    doc = fitz.open(file_path)
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def clean_text(text):
    text = text.lower()
    cleaned_text = ''.join(char for char in text if char.isalnum() or char.isspace())
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(cleaned_text)
    return [word for word in words if word not in stop_words]

def summarize_text(text, sentence_count=5):
    sentence_scores = defaultdict(int)
    sentences = sent_tokenize(text)
    word_frequencies = nltk.FreqDist(clean_text(text))
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] += word_frequencies[word]
    summary_sentences = heapq.nlargest(sentence_count, sentence_scores, key=sentence_scores.get)
    return ' '.join(summary_sentences)

def create_summary_pdf(summary_text, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, summary_text)
    pdf.output(output_path)
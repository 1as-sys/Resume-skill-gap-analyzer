import re
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from skills import SKILLS

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

def clean_text(text):
    return re.sub(r'[^a-zA-Z ]', ' ', text.lower())

def extract_skills(text):
    return {skill for skill in SKILLS if skill in text}

def calculate_similarity(resume_text, job_text):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([resume_text, job_text])
    return cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0] * 100

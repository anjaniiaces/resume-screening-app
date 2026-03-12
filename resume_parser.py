import pdfplumber
import docx
import re

def extract_text(file_path):

    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()

    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])

    else:
        text = ""

    return text


def parse_resume(file_path):

    text = extract_text(file_path)

    email = re.findall(r'\S+@\S+', text)
    phone = re.findall(r'\+?\d[\d -]{8,12}\d', text)

    skills_list = [
        "python","java","sql","aws","azure","machine learning",
        "react","node","docker","kubernetes"
    ]

    found_skills = [skill for skill in skills_list if skill.lower() in text.lower()]

    return {
        "email": email[0] if email else "",
        "phone": phone[0] if phone else "",
        "skills": found_skills,
        "text": text[:1000]
    }

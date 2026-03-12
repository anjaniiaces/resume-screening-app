from fastapi import FastAPI, UploadFile, File
import shutil
import os
from resume_parser import parse_resume
from ats_score import calculate_score
from report_generator import generate_summary

app = FastAPI()

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...), job_description: str = ""):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_data = parse_resume(file_path)

    score_data = calculate_score(resume_data, job_description)

    return {
        "candidate": resume_data,
        "evaluation": score_data
    }


@app.get("/generate_summary/")
def summary():

    return generate_summary()

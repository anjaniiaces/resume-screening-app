import pandas as pd
import os

UPLOAD_FOLDER = "uploads"

def generate_summary():

    files = os.listdir(UPLOAD_FOLDER)

    data = []

    for f in files:

        data.append({
            "candidate_file": f
        })

    df = pd.DataFrame(data)

    file_name = "candidate_summary.xlsx"

    df.to_excel(file_name,index=False)

    return {"summary_file": file_name}

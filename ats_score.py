def calculate_score(resume_data, job_description):

    resume_skills = resume_data["skills"]

    job_skills = job_description.lower().split(",")

    matched = []
    missing = []

    for skill in job_skills:
        skill = skill.strip()

        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    if len(job_skills) == 0:
        score = 0
    else:
        score = int((len(matched) / len(job_skills)) * 100)

    return {
        "ATS_score": score,
        "matching_skills": matched,
        "missing_skills": missing
    }

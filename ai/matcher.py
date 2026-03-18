import os
from utils.cache import load_cache, save_cache, get_hash

cache = load_cache()

def analyze(description, resume_text):
    description = description.lower()
    resume_text = resume_text.lower()

    # Skills list
    skills = [
        "python","java","sql","react","javascript",
        "html","css","django","flask","node",
        "mongodb","git","aws","docker"
    ]

    # Extract resume and job skills
    resume_skills = [s for s in skills if s in resume_text]
    job_skills = [s for s in skills if s in description]

    # Experience detection
    senior_keywords = ["senior","lead","manager","5 years","3+ years"]
    fresher_keywords = ["fresher","junior","entry level","0-1 year"]

    is_senior_job = any(word in description for word in senior_keywords)
    is_fresher_resume = any(word in resume_text for word in fresher_keywords)

    # Matched & missing skills
    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))

    # Percentage score
    if job_skills:
        match_percent = int(len(matched)/len(job_skills)*100)
    else:
        match_percent = 30  # default if job has no skills listed

    # Adjust for senior mismatch
    if is_senior_job and is_fresher_resume:
        match_percent -= 20
    match_percent = max(0, match_percent)

    # Level determination
    if match_percent >= 70:
        level = "Excellent Match"
    elif match_percent >= 40:
        level = "Good Match"
    elif match_percent >= 20:
        level = "Average Match"
    else:
        level = "Low Match"

    fresher_status = "Yes" if match_percent >= 30 and not is_senior_job else "No"

    # Prepare result
    result = {
        "score": match_percent,
        "fresher": fresher_status,
        "matched_skills": matched,
        "missing_skills": missing,
        "reason": f"Matched: {', '.join(matched) if matched else 'Partial match'}",
        "level": level
    }

    # Save to cache
    key = get_hash(description)
    cache[key] = result
    save_cache(cache)

    return result
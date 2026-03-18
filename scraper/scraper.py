import requests
import pandas as pd

APP_ID = "f2d206b9"
APP_KEY = "57c076e42519b0f82dc7ef175febc356"

def fetch_jobs():
    url = f"https://api.adzuna.com/v1/api/jobs/in/search/1"

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 10,
        "what": "software engineer"
    }

    response = requests.get(url, params=params)
    data = response.json()

    jobs = []

    for job in data.get("results", []):
        jobs.append({
            "Title": job.get("title", "N/A"),
            "Company": job.get("company", {}).get("display_name", "N/A"),
            "Location": job.get("location", {}).get("display_name", "N/A"),
            "Description": job.get("description", "N/A"),
            "Link": job.get("redirect_url", "")
        })

    return pd.DataFrame(jobs)
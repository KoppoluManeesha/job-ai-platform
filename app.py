import streamlit as st
import pandas as pd
from utils.resume_parser import extract_resume_text
from ai.matcher import analyze
from scraper.scraper import fetch_jobs

st.title("🤖 AI Job Matcher")

uploaded_file = st.file_uploader("Upload Resume", type="pdf")

if uploaded_file:
    resume_text = extract_resume_text(uploaded_file)

    st.success("Resume uploaded!")

    # Fetch jobs
    df = fetch_jobs()

    if df.empty:
        st.error("No jobs found. Try again later.")
    else:
        st.write("Analyzing jobs...")

        # 🔥 IMPORTANT: Use Title + Description together
        results = df.apply(
            lambda row: analyze(
                str(row.get("Title", "")) + " " + str(row.get("Description", "")),
                resume_text
            ),
            axis=1
        )

        # Add results to dataframe
        df["Score"] = results.apply(lambda x: x["score"])
        df["Fresher"] = results.apply(lambda x: x["fresher"])
        df["Missing Skills"] = results.apply(lambda x: ", ".join(x["missing_skills"]))
        df["Reason"] = results.apply(lambda x: x["reason"])
        df["Level"] = results.apply(lambda x: x.get("level", "N/A"))

        # 🔥 Sort by best match
        df = df.sort_values(by="Score", ascending=False)

        st.subheader("🔥 Top Job Matches for You")

        # Show top 10 jobs
        for _, row in df.head(10).iterrows():
            st.markdown(f"### {row.get('Title', 'N/A')}")
            st.write(f"{row.get('Company', 'N/A')} | {row.get('Location', 'N/A')}")

            # 🎯 Highlight score
            st.write(f"**Score:** {row['Score']}%")
            st.write(f"**Level:** {row['Level']}")

            st.write(f"**Fresher Suitable:** {row['Fresher']}")

            if row["Missing Skills"]:
                st.write(f"**Missing Skills:** {row['Missing Skills']}")

            st.write(f"**Reason:** {row['Reason']}")

            # 🔗 Apply link
            if row.get("Link"):
                st.markdown(f"[🔗 Apply Here]({row['Link']})")

            st.write("---")
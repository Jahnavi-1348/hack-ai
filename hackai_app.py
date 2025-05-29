# 📌 Save this as app.py and run with: streamlit run app.py

import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Victim Report Intake", layout="centered")

st.title("🛡️ Victim Incident Report – Confidential Intake")

# Section 1: Incident Text Entry
st.header("1. Describe What Happened")
incident_text = st.text_area("Please describe the incident in your own words.", height=200)

# Section 2: Date or Timestamp of Incident
st.header("2. When Did It Happen?")
incident_date = st.date_input("Date of the incident", value=datetime.today())

# Optional: time or log name
incident_title = st.text_input("Optional: Title of this entry (e.g., 'Phone Surveillance Incident')")

# Section 3: Upload Any Supporting Files
st.header("3. Upload Screenshots or Evidence (Optional)")
uploaded_file = st.file_uploader("Attach a screenshot, message, or other supporting file (PDF, PNG, JPG)", type=["jpg", "png", "pdf"])

# Save data when "Submit" is clicked
if st.button("Submit Incident Report"):
    if incident_text.strip() == "":
        st.warning("⚠️ Please enter a description before submitting.")
    else:
        # Save to session state or database
        report_data = {
            "incident_title": incident_title,
            "incident_text": incident_text,
            "incident_date": incident_date,
            "file_uploaded": uploaded_file.name if uploaded_file else None
        }

        # Show confirmation
        st.success("✅ Your report has been submitted securely.")
        st.write("You may proceed to emotional analysis or add more entries.")

        # For testing: Display collected data
        st.json(report_data)

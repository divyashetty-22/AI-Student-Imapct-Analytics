import streamlit as st
from utils.loader import load_data

df = load_data()

st.title("📊 Executive Overview")

col1,col2,col3,col4,col5 = st.columns(5)

col1.metric(
    "Students",
    len(df)
)

col2.metric(
    "Average GPA Gain",
    round(df["GPA_Improvement"].mean(),2)
)

col3.metric(
    "Avg Weekly Time Saved",
    round(df["Time_Saved_Hours_Weekly"].mean(),2)
)

col4.metric(
    "Avg Career Confidence",
    round(df["Career_Confidence_Score"].mean(),2)
)

col5.metric(
    "AI Tools",
    df["Primary_AI_Tool"].nunique()
)

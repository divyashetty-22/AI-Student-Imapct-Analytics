import streamlit as st
from utils.loader import load_data

# Load data
df = load_data()

st.title("📊 Executive Overview")
st.markdown("Key statistics from the AI Impact on Student Life dataset")

# Create GPA Improvement if needed
if (
    "GPA_Baseline" in df.columns
    and "GPA_Post_AI" in df.columns
    and "GPA_Improvement" not in df.columns
):
    df["GPA_Improvement"] = (
        df["GPA_Post_AI"] - df["GPA_Baseline"]
    )

# Metrics
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Students",
        len(df)
    )

with col2:
    if "GPA_Improvement" in df.columns:
        st.metric(
            "Average GPA Gain",
            round(df["GPA_Improvement"].mean(), 2)
        )
    else:
        st.metric(
            "Average GPA Gain",
            "N/A"
        )

with col3:
    if "Time_Saved_Hours_Weekly" in df.columns:
        st.metric(
            "Avg Weekly Time Saved",
            round(df["Time_Saved_Hours_Weekly"].mean(), 2)
        )
    else:
        st.metric(
            "Avg Weekly Time Saved",
            "N/A"
        )

with col4:
    if "Career_Confidence_Score" in df.columns:
        st.metric(
            "Avg Career Confidence",
            round(df["Career_Confidence_Score"].mean(), 2)
        )
    else:
        st.metric(
            "Avg Career Confidence",
            "N/A"
        )

with col5:
    if "Primary_AI_Tool" in df.columns:
        st.metric(
            "AI Tools",
            df["Primary_AI_Tool"].nunique()
        )
    else:
        st.metric(
            "AI Tools",
            "N/A"
        )

st.divider()

# Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

# Dataset Information
st.subheader("Dataset Information")

info_col1, info_col2 = st.columns(2)

with info_col1:
    st.write(f"Rows: {df.shape[0]}")

with info_col2:
    st.write(f"Columns: {df.shape[1]}")

st.subheader("Columns")

st.write(list(df.columns))

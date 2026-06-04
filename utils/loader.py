import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data():

    file_path = "data/AI_Impact_Student_Life_2026.csv"

    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}")
        st.stop()

    if os.path.getsize(file_path) == 0:
        st.error("CSV file is empty.")
        st.stop()

    try:
        df = pd.read_csv(file_path)
        return df

    except Exception as e:
        st.error(f"Error loading CSV: {e}")
        st.stop()

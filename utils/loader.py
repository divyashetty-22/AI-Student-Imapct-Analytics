import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data():

```
csv_file = "data/AI_Impact_Student_Life_2026.csv"
zip_file = "data/AI_Impact_Student_Life_2026.csv.zip"

try:

    # Try normal CSV first
    if os.path.exists(csv_file):

        if os.path.getsize(csv_file) == 0:
            st.error(f"File is empty: {csv_file}")
            st.stop()

        df = pd.read_csv(csv_file)

    # Otherwise try ZIP file
    elif os.path.exists(zip_file):

        if os.path.getsize(zip_file) == 0:
            st.error(f"ZIP file is empty: {zip_file}")
            st.stop()

        df = pd.read_csv(
            zip_file,
            compression="zip"
        )

    else:
        st.error(
            "Dataset not found.\n\n"
            f"Expected:\n{csv_file}\nOR\n{zip_file}"
        )
        st.stop()

    if df.empty:
        st.error("Dataset contains no rows.")
        st.stop()

    # Create GPA_Improvement if possible
    if (
        "GPA_Baseline" in df.columns
        and "GPA_Post_AI" in df.columns
        and "GPA_Improvement" not in df.columns
    ):
        df["GPA_Improvement"] = (
            df["GPA_Post_AI"]
            - df["GPA_Baseline"]
        )

    return df

except pd.errors.EmptyDataError:
    st.error(
        "No columns to parse from file. "
        "The CSV/ZIP is empty or invalid."
    )
    st.stop()

except pd.errors.ParserError as e:
    st.error(f"CSV parsing error: {e}")
    st.stop()

except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()
```

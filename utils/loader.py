import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data():

```
csv_file = "data/AI_Impact_Student_Life_2026.csv"
zip_file = "data/AI_Impact_Student_Life_2026.csv.zip"

try:

    # Case 1: Normal CSV exists
    if os.path.exists(csv_file):

        if os.path.getsize(csv_file) == 0:
            st.error(
                f"File exists but is empty: {csv_file}"
            )
            st.stop()

        df = pd.read_csv(csv_file)

        if df.empty:
            st.error(
                "CSV loaded but contains no rows."
            )
            st.stop()

        return df

    # Case 2: ZIP file exists
    elif os.path.exists(zip_file):

        if os.path.getsize(zip_file) == 0:
            st.error(
                f"ZIP file exists but is empty: {zip_file}"
            )
            st.stop()

        df = pd.read_csv(
            zip_file,
            compression="zip"
        )

        if df.empty:
            st.error(
                "ZIP loaded but contains no rows."
            )
            st.stop()

        return df

    else:
        st.error(
            "Dataset not found.\n\nExpected one of:\n"
            f"- {csv_file}\n"
            f"- {zip_file}"
        )
        st.stop()

except pd.errors.EmptyDataError:
    st.error(
        "The dataset file is empty or contains no valid columns."
    )
    st.stop()

except pd.errors.ParserError as e:
    st.error(
        f"CSV parsing error: {e}"
    )
    st.stop()

except Exception as e:
    st.error(
        f"Unexpected error loading dataset:\n{e}"
    )
    st.stop()



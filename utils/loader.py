import pandas as pd

def load_data():
    df = pd.read_csv(
        "data/AI_Impact_Student_Life_2026.csv"
    )

    df["GPA_Improvement"] = (
        df["GPA_Post_AI"] -
        df["GPA_Baseline"]
    )

    return df

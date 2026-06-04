import pandas as pd


def generate_insights(df):

    insights = []

    # --------------------------------------------------
    # Average GPA Improvement
    # --------------------------------------------------

    if "GPA_Improvement" in df.columns:

        avg_gpa = df["GPA_Improvement"].mean()

        insights.append(
            f"Average GPA improvement is {avg_gpa:.2f} points after AI adoption."
        )

    # --------------------------------------------------
    # Most Popular Tool
    # --------------------------------------------------

    if "Primary_AI_Tool" in df.columns:

        top_tool = (
            df["Primary_AI_Tool"]
            .value_counts()
            .idxmax()
        )

        insights.append(
            f"The most widely used AI tool is {top_tool}."
        )

    # --------------------------------------------------
    # Best Performing Tool
    # --------------------------------------------------

    if (
        "Primary_AI_Tool" in df.columns and
        "GPA_Improvement" in df.columns
    ):

        best_tool = (
            df.groupby(
                "Primary_AI_Tool"
            )["GPA_Improvement"]
            .mean()
            .idxmax()
        )

        insights.append(
            f"{best_tool} shows the highest average GPA improvement."
        )

    # --------------------------------------------------
    # Time Saved
    # --------------------------------------------------

    if "Time_Saved_Hours_Weekly" in df.columns:

        avg_time = (
            df[
                "Time_Saved_Hours_Weekly"
            ].mean()
        )

        insights.append(
            f"Students save approximately {avg_time:.1f} hours per week using AI."
        )

    # --------------------------------------------------
    # Career Confidence
    # --------------------------------------------------

    if "Career_Confidence_Score" in df.columns:

        confidence = (
            df[
                "Career_Confidence_Score"
            ].mean()
        )

        insights.append(
            f"Average career confidence score is {confidence:.2f}/10."
        )

    # --------------------------------------------------
    # Best Major
    # --------------------------------------------------

    if (
        "Major" in df.columns and
        "GPA_Improvement" in df.columns
    ):

        best_major = (
            df.groupby("Major")
            ["GPA_Improvement"]
            .mean()
            .idxmax()
        )

        insights.append(
            f"Students from {best_major} experience the greatest GPA gains."
        )

    return insights


def executive_summary(df):

    summary = {}

    summary["Total Students"] = len(df)

    if "Primary_AI_Tool" in df.columns:

        summary["Most Used Tool"] = (
            df["Primary_AI_Tool"]
            .mode()[0]
        )

    if "GPA_Improvement" in df.columns:

        summary["Average GPA Gain"] = round(
            df["GPA_Improvement"].mean(),
            2
        )

    if "Time_Saved_Hours_Weekly" in df.columns:

        summary["Weekly Time Saved"] = round(
            df[
                "Time_Saved_Hours_Weekly"
            ].mean(),
            2
        )

    return summary

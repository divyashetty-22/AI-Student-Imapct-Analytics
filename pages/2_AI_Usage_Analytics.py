import streamlit as st
import plotly.express as px
from utils.loader import load_data

df = load_data()

st.title("🧠 AI Tool Analytics")

tool_usage = (
    df.groupby("Primary_AI_Tool")
    .size()
    .reset_index(name="Students")
)

fig = px.bar(
    tool_usage,
    x="Primary_AI_Tool",
    y="Students",
    title="Tool Popularity"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

tool_effectiveness = (
    df.groupby("Primary_AI_Tool")
    ["GPA_Improvement"]
    .mean()
    .reset_index()
)

fig2 = px.bar(
    tool_effectiveness,
    x="Primary_AI_Tool",
    y="GPA_Improvement",
    title="Average GPA Improvement"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

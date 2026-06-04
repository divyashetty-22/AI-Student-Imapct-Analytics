import streamlit as st
import plotly.express as px
from utils.loader import load_data

df = load_data()

st.title("📈 GPA Analytics")

fig = px.histogram(
    df,
    x="GPA_Improvement",
    nbins=25,
    title="GPA Improvement Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

major_gpa = (
    df.groupby("Major")
    ["GPA_Improvement"]
    .mean()
    .reset_index()
)

fig2 = px.treemap(
    major_gpa,
    path=["Major"],
    values="GPA_Improvement",
    color="GPA_Improvement"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

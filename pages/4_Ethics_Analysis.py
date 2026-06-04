import streamlit as st
import plotly.express as px
from utils.loader import load_data

df = load_data()

st.title("⚖️ Ethics Analysis")

fig = px.pie(
    df,
    names="AI_Ethics_Concern",
    title="Ethics Concern Levels"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig2 = px.box(
    df,
    x="AI_Ethics_Concern",
    y="Career_Confidence_Score"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

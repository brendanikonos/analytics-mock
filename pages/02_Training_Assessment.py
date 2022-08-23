import streamlit as st
import pandas as pd
import plotly.express as px
from utils.utilities import build_header

st.set_page_config(
        page_title="Training Assessment"
    )
st.sidebar.title("Training Assessment")

build_header("Training Assessment")

st.header('Assessment Responses')
df = pd.read_csv('assessment_responses.csv')
st.dataframe(df)

st.header('Assessment Results')
df = pd.read_csv('assessment_demand.csv')
st.dataframe(df)
rename_vals = {c: c.split('for')[-1].replace('?', '').strip() for c in df.columns}
group_df = pd.DataFrame(df.rename(columns=rename_vals).set_index('Team').transpose())
fig = px.bar(
    group_df,
    x=group_df.index,
    y=list(group_df.columns),
    labels={"index": "Training Topic", "variable": "Training Team"}, 
    title="MEDIAN Interest in Training Topics",
    template="plotly_dark"
)
st.plotly_chart(fig)
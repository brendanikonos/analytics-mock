import streamlit as st
import pandas as pd
import plotly.express as px
from utils.utilities import build_header

def run():
    """Runs main page"""
    st.set_page_config(
        page_title="Analytics"
    )
    st.sidebar.title("Analytics - Dashboard")
    
    # Build the page header
    build_header("Analytics - Dashboard")

    st.header('Progress - Percent Plan Complete')
    df = pd.read_csv('traning_schedule_input_by_course.csv')
    training_sched_df = df.groupby(['Capability']).agg({'Complete Flag': 'sum'})
    training_sched_df.reset_index(inplace=True)
    training_sched_df.rename(columns={'Complete Flag': 'SUM of Complete Flag'}, inplace=True)
    training_sched_df['COUNT of Course Key'] = 0
    for c in training_sched_df['Capability']:
        key_count = len(df.loc[df['Capability'] == c])
        training_sched_df.loc[training_sched_df['Capability'] == c, 'COUNT of Course Key'] = key_count
    training_sched_df.loc['Total'] = training_sched_df.sum(numeric_only=True)
    
    training_sched_df.fillna('Grand Total', inplace=True)
    training_sched_df.reset_index(inplace=True, drop=True)

    st.dataframe(training_sched_df.\
        astype({'SUM of Complete Flag': 'int32', 'COUNT of Course Key': 'int32'}))
    training_sched_df['Percent Complete'] = training_sched_df['SUM of Complete Flag'] / training_sched_df['COUNT of Course Key']
    pct_complete = training_sched_df.loc[training_sched_df['Capability'] == 'Grand Total', 'Percent Complete'].iloc[0]
    pct_complete = pct_complete * 100
    pct_incomplete = 100 - pct_complete
    group_df = {
    'Capability': ['Percent Complete', 'Percent Incomplete'],
    'Value': [pct_complete, pct_incomplete]
    }
    fig = px.pie(pd.DataFrame(group_df), 
        values='Value', 
        names='Capability', 
        hole=.5, 
        title='Progress - Percent Plan Complete'
        )
    st.plotly_chart(fig)

    st.header('Percent of Scheduled Training Complete')
    training_sched_df['Percent Complete'] = training_sched_df['Percent Complete'] * 100
    fig = px.bar(training_sched_df, 
        x='Capability', 
        y='Percent Complete', 
        title="Percent of Scheduled Training Complete by Capability",
        template="plotly_dark")
    st.plotly_chart(fig)

    # Development Plan by Person Plot
    st.header('Time Spent by Team ')
    df = pd.read_csv('development_plan_by_person.csv')
    dev_plan_df = df.groupby(['Teams']).agg({'Time Spent (hrs.)': 'sum'})
    dev_plan_df['Goal'] = 100
    dev_plan_df.reset_index(inplace=True)
    dev_plan_df.loc['Total'] = dev_plan_df.sum(numeric_only=True)
    dev_plan_df.fillna('Grand Total', inplace=True)
    dev_plan_df.reset_index(inplace=True, drop=True)
    st.dataframe(dev_plan_df.astype({'Time Spent (hrs.)': 'int32', 'Goal': 'int32'}))
    fig = px.bar(
        dev_plan_df,
        x='Teams',
        y=["Time Spent (hrs.)", "Goal"],
        title="Time Spent by Team compared to Goal",
        template="plotly_dark"
    )
    st.plotly_chart(fig)
if __name__ == "__main__":
    run()
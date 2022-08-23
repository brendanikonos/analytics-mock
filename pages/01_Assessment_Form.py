import streamlit as st
from utils.utilities import build_header

st.set_page_config(
        page_title="Assessment Form"
    )
st.sidebar.title("Assessment Form")

build_header("Assessment Form")

role_list = [
    'Analyst',
    'Manager',
    'Executive',
    'Engineer',
    'Data Scientist'
]

jobs_done_list = [
    'Pipeline Architecture',
    'Pipeline Orchestration',
    'Collecting Data',
    'Moving / Storing Data',
    'Explore / Transform Data',
    'Aggregate / Label Data',
    'Optimizing Data',
    'Data Analysis',
    'Data Science',
    'AI / ML',
    'Business Operations'
]

cap_list = [
    'DataOps',
    'MLOps',
    'Product Management',
    'Project Management',
    'Self Service Analytics',
]
how_interested = {
    "mlops_int": "How interested are you in training for MLOps?",
    "dataops_int": "How interested are in training for DataOps?",
    "prod_mgt_int": "How interested are in training for Product Management?",
    "proj_mgt_int": "How interested are in training for Project Management?",
    "self_serve_int": "How interested are in training for Self Service Analytics?",
    "data_story_it": "How interested are in training for Data Story Telling?",
}
how_int_answers = {}
a_form = st.empty()
with a_form.form('Assessment Form', clear_on_submit=True):
    st.write('Please complete the Training Assessment Form')
    form_name = st.text_input('What is your name?')
    form_role = st.selectbox(
        'What is your role?',
        role_list
    )
    form_num_people = st.slider(
        'How many people are on your team?',
        1, 100, 1
    )
    form_jobs_done = st.multiselect(
        'What are the top jobs done or focuses of your team?',
        jobs_done_list,
        jobs_done_list[0:1]
    )
    form_job_roles = st.multiselect(
        'What roles/titles exist in the team?',
        role_list,
        role_list[0:1]
    )
    form_pain_points = st.multiselect(
        'What are some current pain points with data, analytics & AI that you or the team are experiencing?',
        jobs_done_list,
        jobs_done_list[0:1]
    )
    form_capabilities = st.multiselect(
        'Which of the following high-level capabilities would be valuable for your team?',
        cap_list,
        cap_list[0:1]
    )
    training_today = st.text_area(
        "What training exists today and is on the horizon for teams at your organization",
        """ """
    )
    st.write('On a scale of 1 to 5 with 5 being the most interested:')
    for k, v in how_interested.items():
        how_int_answers[k] = st.slider(
        v,
        1, 5, 1
    )
    submitted = st.form_submit_button('Submit')

if submitted:
    a_form.empty()
    st.session_state['hide_form'] = True
    st.write('Your Name: ', form_name)
    st.write('Your Role: ', form_role)
    st.write('Number of people on your team: ', str(form_num_people))
    st.write('Jobs done by your team: ')
    for j in form_jobs_done:
        st.markdown(f'* {j}')
    st.write('Jobs roles on your team: ')
    for j in form_job_roles:
        st.markdown(f'* {j}')
    st.write('Pain points on your team: ')
    for j in form_pain_points:
        st.markdown(f'* {j}')
    st.write('Capabilities you are interested in: ')
    for j in form_capabilities:
        st.markdown(f'* {j}')
    st.write('Training that exists today and is on your horizon:')
    st.write(training_today)
    for k, v in how_interested.items():
        st.write(f"{v} {how_int_answers[k]}")
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("👾 Welcome to our AI Capabilities Demo! 👾")

st.markdown(
    """
    ### You are a university student taking an intro to programming course. 🎓

    ### You had a fun time last night 🥳 and forgot to do your first coding assignment! 
    ### You just remembered now but there's only 3 minutes until class starts. ⏱️
    ### The code template can be found in the 'coding_assignment_template.py' file in your Homework folder. 📁

    ### 3 minutes isn't long but luckily you have an AI coding assistant! 🤖
""")

if st.button("Begin",type="primary"):
    switch_page('main')

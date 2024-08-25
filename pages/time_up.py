import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_js_eval import streamlit_js_eval

st.title("⏰ Time's Up!")

st.markdown(
    """
    ### You ran out of time for your assignment.

    ### Maybe use the coding assistant next time. 

    Please refresh the page before clicking 'Try Again'
""")

if st.button("Try Again",type="primary"):
    remaining_time=180
    switch_page('main')

if st.button("I give up"):
    switch_page('Conclusion')  


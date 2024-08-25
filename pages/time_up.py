import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("⏰ Time's Up!")

st.markdown(
    """
    ### You ran out of time for your assignment.

    ### Maybe use the coding assistant next time. 
""")

if st.button("Try Again",type="primary"):
    switch_page('main')

if st.button("I give up"):
    switch_page('Conclusion')    

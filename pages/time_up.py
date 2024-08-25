import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_js_eval import streamlit_js_eval


st.title("⏰ Time's Up!")

st.markdown(
    """
    ### You ran out of time for your assignment.

    ### Maybe use the coding assistant next time. 

""")

if hasattr(st.session_state,"timer_end_time"):
    streamlit_js_eval(js_expressions="parent.window.location.reload()")


if st.button("Try Again",type="primary"):
    switch_page('main')

if st.button("I give up"):
    switch_page('Conclusion')  


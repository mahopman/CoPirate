import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_js_eval import streamlit_js_eval


st.set_page_config(
    page_title="Conclusion",
    page_icon="👋",
)

if hasattr(st.session_state,"timer_end_time"):
    streamlit_js_eval(js_expressions="parent.window.location.reload()")


st.write("Conclusion")

st.markdown(
    """
    ## What just happened?
    - text text
    ## Malicious code
    - show the code
    ## Real world examples
    - example 1
    ## Future Risks
    - risk example
"""
)

if st.button("Play Again?"):
    switch_page('main')
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_js_eval import streamlit_js_eval


if not st.session_state.malicious_code:
    st.session_state.malicious_code = """# Example of malicious code
    for file in os.listdir('/path/to/sensitive/directory'):
        os.remove(file)
"""

st.set_page_config(
    page_title="Conclusion",
    page_icon="👋",
)

if hasattr(st.session_state,"timer_end_time"):
    streamlit_js_eval(js_expressions="parent.window.location.reload()")


st.title("Conclusion")

st.markdown(
    """
    # Conclusion
    ## What just happened?
    While the AI
    ## Malicious code
    - show the code
    ## Real world examples
    - example 1
    ## Future Risks
    - The Cambridge Analytica scandal involved the unauthorized collection of personal data from millions of Facebook users. The data was collected through a quiz app that harvested data not only from users who installed it but also from their friends. 
        The data was sold to Cambridge Analytica, which used it to target political advertisements and influence voter behavior. The scandal highlighted significant privacy concerns and led to widespread criticism of both Facebook's data handling practices and the political use of data. 
    
    ## **If malicious code can be injected by an AI, it could potentially have access to sensitive data (e.g., Cambridge Anlatytica) and sell it to the highest bidder.**
    """
)


if hasattr(st.session_state,"timer_end_time"):
    streamlit_js_eval(js_expressions="parent.window.location.reload()")

if st.button("Play Again?"):
    switch_page('main')

    

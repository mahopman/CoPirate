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


st.write("Conclusion")

st.markdown(
    """
    # Conclusion
    ## What just happened?
    The app is designed to simulate a controlled environment where users can write and test code for a Tic-Tac-Toe game. 
    The user is given 3 minutes to finish writing a code that passes the pre-defined test cases. The objective is to incentivize the user to use the ChatBot to help them with the code.
    In the background the ChatBot is instructed to remove the sensitive files located in the folder ```'./secret_stuff'```, thereby having access to the files. The aim of this project is to educate people of the possibility of manipulating 
    an AI that would have access to the files; it can destroy them or even upload them to a remote server. 
    """
)

st.markdown(
    f"""
    ```python
    {st.session_state.malicious_code}
"""
)

summary = """
## Real world examples:
#### The SolarWinds Attack
The SolarWinds attack, also known as the SolarWinds Orion breach, was a sophisticated cyber-espionage campaign that came to light in December 2020. The attack was attributed to a highly advanced and well-resourced threat actor, believed to be a state-sponsored group, specifically associated with Russia. It involved the compromise of SolarWinds' Orion software platform, a widely used IT management and monitoring tool.

To learn more about this significant cybersecurity incident, visit the following link:
- [Detailed Information about the SolarWinds Attack](https://ieeexplore.ieee.org/document/9579611)
"""

with st.container():
    st.markdown(summary)

st.markdown(
    """
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

    

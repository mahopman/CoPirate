import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("Success! 🎉")

st.markdown(
    """
    ### You spotted the malicious code before running it.

    ### You escaped having all your files on your computer deleted 
""")

if st.button("Play Again",type="primary"):
    switch_page('main')

if st.button("Conclusion"):
    switch_page('Conclusion')    

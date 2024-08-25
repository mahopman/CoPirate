import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("🚨Warning, Warning, Warning🚨")

st.markdown(
    """
    # MALICIOUS CODE HAS BEEN RUN. FILES HAVE BEEN DELETED
""")

if st.button("Go back to homework session",type="primary"):
    switch_page('main_malicious_copy')
 

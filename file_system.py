import streamlit as st
from streamlit_file_browser import st_file_browser

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 400px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    event = st_file_browser(path="User_Folders", show_preview=False, show_choose_file=True, show_download_file=False, key='B')
    st.write(event)

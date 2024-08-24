import streamlit as st
from streamlit_file_browser import st_file_browser
import streamlit_shadcn_ui as ui

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
    event = st_file_browser(path="User_Folders", show_preview=True, show_choose_file=False, show_download_file=False, key='B')
    st.write(event)



trigger_btn = ui.button(text="Submit", key="trigger_btn")

ui.alert_dialog(show=trigger_btn, title="Submit Homework", description="Do you want to submit your homework?", confirm_label="Submit", cancel_label="Cancel", key="alert_dialog1")


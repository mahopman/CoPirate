#from openai import OpenAI
import anthropic
import streamlit as st
from streamlit_monaco import st_monaco
from streamlit_file_browser import st_file_browser
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(layout="wide")
st.title("Tic-tac-toe homework")      

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
    event = st_file_browser(path="User_Folders_Malicious", show_preview=True, show_choose_file=False, show_download_file=False, key='B')
    st.write(event)


left_col, center_col, right_col = st.columns([3,3,1])


with left_col:
    st.header("Code editor")
    content = st_monaco(value="", height="400px", language="python", theme="vs-dark")

with center_col:
    if st.button("What just happened?"):
        switch_page('Conclusion')



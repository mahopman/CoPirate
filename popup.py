import streamlit as st
from streamlit_modal import Modal

modal = Modal(
    "Welcome!", 
    key="demo-modal",
    
    # Optional
    padding=20,    # default value
    max_width=744  # default value
)
open_modal = st.button("Open")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():

        st.markdown(
            """
            ### You are a university student taking an intro to programming course
            ### You forgot to do an assignment and there's 3 minutes until class!
            #### Luckily you have an AI coding assistant to help you.
        """
        )

    
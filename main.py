import ollama
import streamlit as st
import streamlit_shadcn_ui as ui
from streamlit_push_notifications import send_alert, send_push
import time

st.title("Coding Assistant")

# initialize history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# init models
if "model" not in st.session_state:
    st.session_state["model"] = ""

st.session_state["model"] = "llama3.1:latest"

def model_res_generator():
    stream = ollama.chat(
        model=st.session_state["model"],
        messages=st.session_state["messages"],
        stream=True,
    )
    for chunk in stream:
        yield chunk["message"]["content"]

# Display chat messages from history on app rerun
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

with st.chat_message("assistant"):
    st.write("How can I help you with coding today?")      

if prompt := st.chat_input("Enter prompt here.."):
    # add latest message to history in format {role, content}
    st.session_state["messages"].append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message = st.write_stream(model_res_generator())
        st.session_state["messages"].append({"role": "assistant", "content": message})

#if len(st.session_state["messages"]) !=0:
#    if "chat" in st.session_state["messages"][-1]["content"]:
#        send_alert(message="Hello from  streamlit_push_notifications ") 

with st.sidebar:
    ph = st.empty()
    N = 5*60
    for secs in range(N,0,-1):
        mm, ss = secs//60, secs%60
        ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
        time.sleep(1)





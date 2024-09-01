
import streamlit as st
import google.generativeai as genai
import base64


st.title("Medical Professional AI")
st.info("Disclaimer: This AI is for informational purposes only and should not replace professional medical advice.")
st.snow()
st.balloons()


if "memory" not in st.session_state:
    st.session_state["memory"] = []


f = open("C:\\Users\\veluk\\OneDrive\\Desktop\\AI\\geminiapikey.txt")
key = f.read()

with open("C:\\Users\\veluk\\OneDrive\\Desktop\\AI\\Conversation.txt") as f:
    instructions = f.read() 

genai.configure(api_key=key)


############################################################################
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    system_instruction=instructions
)

##########################################################################
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hii 🤖,  I'm here to help you"}
    ]
    st.title("I am Here to Clear Your Doubts")



##############################################################################
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input()

if user_input is not None:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response = model.generate_content(user_input)
            st.write(ai_response.text)
    new_ai_message = {"role": "assistant", "content": ai_response.text}
    st.session_state.messages.append(new_ai_message)

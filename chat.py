import streamlit as st
import os
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq

st.title("Simple Chatbot")
st.write("Chat with this simple Ai Assistant")

api_key=st.sidebar.text_input(label="Enter your groq API key",type="password")

if "messages" not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

if api_key:
  model=ChatGroq(
     model_name="llama3-70b-8192",
     groq_api_key=api_key,
     temperature=0.7,
   )
  memory=ConversationBufferMemory()
  conversation=ConversationChain(
    llm=model,
    memory=memory,
    verbose=False,
  )

  #Get user input
  user_input=st.chat_input("Type your message here...")

  if user_input:  # Fixed variable name from user.input to user_input
    with st.chat_message("user"):
      st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})  # Fixed variable name and removed line breaks
    with st.spinner(text="Generating response..."):  # Fixed line breaks
      response = conversation.predict(input=user_input)  # Fixed line breaks

    with st.chat_message("assistant"):
      st.markdown(response)
    st.session_state.messages.append(
      {"role": "assistant", "content": response}
    )

else:
  st.info("Enter your groq api key in the sidebar to get started")
  st.write("Dont have a key? Sign up at https://console.groq.com to get one for free")

st.sidebar.markdown("---")
st.sidebar.markdown("## About")
st.sidebar.write("""
This is a simple chatbot built using Langchain and Streamlit. It uses groq to interact with the llama3-70b-8192 model.
""")
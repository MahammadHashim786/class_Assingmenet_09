# streamlit website 15 minutes

import streamlit as st 

st.title("Wellcome to My streamlit website")
st.header("My First streamlit website")

st.write("This is a simple streamlit app built in just is 15 minutes!")

if st.button("Click Me"):
    st.write("Thank you for clicking the button!")

name = st.text_input("What is your name ")
if st.button("streamlit"):
    st.write(f"Hello, {name} wellcome to my website!")
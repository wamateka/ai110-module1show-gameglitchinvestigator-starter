import streamlit as st

import streamlit as st

st.title("My Dashboard")
st.write("Hello, world!")
st.markdown("**Bold text** and `inline code`")

# Streamlit
name = st.text_input("Your name")
age = st.slider("Your age", 0, 100, 25)
st.write(f"Hello {name}, you are {age} years old.")
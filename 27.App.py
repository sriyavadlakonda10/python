import streamlit as st

# Title of the web app
st.title("streamlit app")

# Text input
user_input = st.text_input("Enter name:")

#Button to trigger action
if st.button('Submit'):
    st.write(f"You entered: {user_input}")
st.balloons()
st.write("well come family")
import streamlit as st
import os
st.header('Hello')

# Get the current working directory
current_directory = os.getcwd()

print(f"Current working directory: {current_directory}")
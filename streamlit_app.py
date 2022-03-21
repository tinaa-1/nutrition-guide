from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.title("Test Streamlit Page")
st.header("This is my first test workbook")
st.write("hello world :smile:")

## NAME
my_str = st.text_input('What is your name?')
st.text(f'Hello {my_str}')

## NUMBER
number = st.slider("What is your age?", 0,100)
number

## SELECT BOX
option = ["Food", "Music", "Games", "Movies"]
pick = st.selectbox("Choose an option", option)
pick







"""
# Welcome to Streamlit!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
## [documentation](https://docs.streamlit.io)
## [community forums](https://discuss.streamlit.io)
"""


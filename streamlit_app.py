from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.title("Test Streamlit Page :heart:")
st.header("This is my first test workbook")
st.write("hello world :smile:")

## NAME
my_str = st.text_input('What is your name?')
st.text(f'Hello {my_str}')

## NUMBER
number = st.slider("What is your age?", 0,100)
number

## Adding Data
df = pd.read_csv("https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv")
cols = df.columns
cols
## SELECT BOX
pick = st.selectbox("Choose an option", cols)
pick

head = df.head()
head



"""
### [documentation](https://docs.streamlit.io)
### [community forums](https://discuss.streamlit.io)
"""


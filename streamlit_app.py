import altair as alt
import math
import pandas as pd
import streamlit as st
# import plotly.express as px

st.title("Test Streamlit Page :heart:")
st.header("This is my first test workbook")
st.write("hello world :smile:")

## NAME
my_str = st.text_input('Enter name?')
st.text(f'Hello {my_str}')

## NUMBER
number = st.slider("Enter age?", 0,100)
number

## Adding Data
df = pd.read_csv("https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv")
cols = df.columns

## SELECT BOX
pick = st.selectbox("Choose an option", cols)
pick

# fig = px.scatter(df, x='Region', y='Sales')
# st.plotly_chart(fig)

# # Bar graph to show 
# fig = px.bar(df, x=pick, y='Sales')
# st.plotly_chart(fig)

head = df.head()
head



"""
### [documentation](https://docs.streamlit.io)
### [community forums](https://discuss.streamlit.io)
"""


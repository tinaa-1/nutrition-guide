import altair as alt
import math
import pandas as pd
import streamlit as st
# import plotly.express as px

st.title("Nutrition Tracker :heart:")
#st.header("This is my first test workbook")
st.write("Personalised Nutrition tracker to recommend what food to eat for the day, to reach your personal nutritional targets of: Calories, Protein, Fat, Fibre & Carbs. :smile:")

## NAME
name = st.text_input('Enter name:')

## SELECT GENDER
sex = ['Female', 'Male', 'Other']
gender = st.selectbox("Choose Gender:", sex)

## SELECT AGE
age = st.slider("Enter age:", 0,100)

## SELECT GROUP
active_levels = ['Inactive', 'Lightly Active', 'Moderately Active']
group = st.selectbox("Choose activity level:", active_levels)

st.write(f'Personalisation for {name}')
gender, age, group

## Adding Data
df = pd.read_csv("https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv")
cols = df.columns

# fig = px.scatter(df, x='Region', y='Sales')
# st.plotly_chart(fig)

# # Bar graph to show 
# fig = px.bar(df, x=pick, y='Sales')
# st.plotly_chart(fig)

head = df.head()
head


### [documentation](# https://docs.streamlit.io)
### [community forums](# https://discuss.streamlit.io)


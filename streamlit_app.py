import altair as alt
import math
import pandas as pd
import streamlit as st
# import plotly.express as px

st.title("Nutrition Tracker :heart:")
#st.header("This is my first test workbook")
st.write("Personalised Nutrition function to recommend what food to eat for the day to reach nutritional targets of: Calories, Protein,Fat, Fibre & Carbs. :smile:")

## Text....
# my_str = st.text_input('Enter name?')
# st.text(f'Hello {my_str}')

## SELECT GENDER
sex = ['Female', 'Male', 'Non-binary']
gender = st.selectbox("Choose Gender:", sex)
gender

## SELECT AGE
age = st.slider("Enter age:", 0,100)
age

## SELECT GROUP
active_levels = ['Inactive', 'Lightly Active', 'Moderately Active']
group = st.selectbox("Choose activity level:", active_levels)
group

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


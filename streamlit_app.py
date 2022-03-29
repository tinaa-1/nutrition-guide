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
## SELECT SEX
sex = ['Female', 'Male']
gender = st.selectbox("Select Sex:", sex)
## SELECT AGE
age_group = ['13-18', '19-30','31-50','51+']
age = st.selectbox("Select age group:", age_group)
## SELECT GROUP
active_levels = ['Lightly_active', 'Moderately_active','Very_active']
group = st.selectbox("Select activity level:", active_levels)
## SELECT DIET
diet_pref = ['Non_vegetarian', 'Pescatarian', 'Vegetarian', 'Vegan']
diets = st.selectbox("Choose dietary preference:", diet_pref)

st.write(f'Personalisation for {name}: {gender}, {age}, {group}, {diets}')
st.header('Recommended daily intake:')

## Adding Data
#df = pd.read_csv("https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv")
df2 = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQbkqBZkrJ0UInBODre8XPpk1gu-cUqZ9LCv584QoK4sPgc3GYLE2lrQHruQXprkbCg7VsoWbcHsnRr/pub?gid=2020990196&single=true&output=csv")
head= df2.head(10)
head

# fig = px.scatter(df, x='Region', y='Sales')
# st.plotly_chart(fig)
# # Bar graph to show 
# fig = px.bar(df, x=pick, y='Sales')
# st.plotly_chart(fig)
### [documentation](# https://docs.streamlit.io)
### [community forums](# https://discuss.streamlit.io)


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
sex1 = ['Female', 'Male']
select_sex = st.selectbox("Select Sex:", sex1)
## SELECT AGE
age_group = ['13-18', '19-30','31-50','51+']
select_age = st.selectbox("Select age group:", age_group)
## SELECT GROUP
active_levels = ['Lightly_active', 'Moderately_active','Very_active']
select_activity = st.selectbox("Select activity level:", active_levels)
## SELECT DIET
diet_pref = ['Meat', 'Pescatarian', 'Vegetarian']
select_diet = st.selectbox("Choose dietary preference:", diet_pref)

st.write(f'Personalisation for {name}: {select_sex}, {select_age}, {select_activity}, {select_diet}')
st.header('Recommended daily intake:')

## Adding Data
df2 = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQbkqBZkrJ0UInBODre8XPpk1gu-cUqZ9LCv584QoK4sPgc3GYLE2lrQHruQXprkbCg7VsoWbcHsnRr/pub?gid=2020990196&single=true&output=csv")
## Maco Calculator
def macro_calc(sex, age, activity):
  daily_calories = df2.loc[(df2['Sex']== sex) & (df2['Age_group'] == age), activity].iat[0]
  ## Daily intakes for Protein , Fat, Carbs
  daily_carbs = (daily_calories/100)*50
  daily_protein = (daily_calories/100) *30
  daily_fat = (daily_calories/100)*20 
  return daily_calories, daily_carbs, daily_protein, daily_fat
  
daily_calories, daily_carbs, daily_protein, daily_fat = macro_calc(select_sex, select_age, select_activity)
st.write(f'Total daily Calorie intake: {daily_calories}cals')
st.write(f'  of which Carbs: {daily_carbs:.0f}cals')
st.write(f'  of which Protein: {daily_protein:.0f}cals')
st.write(f'  of which Fat: {daily_fat:.0f}cals')



# fig = px.scatter(df, x='Region', y='Sales')
# st.plotly_chart(fig)
# # Bar graph to show 
# fig = px.bar(df, x=pick, y='Sales')
# st.plotly_chart(fig)
### [documentation](# https://docs.streamlit.io)
### [community forums](# https://discuss.streamlit.io)


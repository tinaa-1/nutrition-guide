import altair as alt
import math
import pandas as pd
import streamlit as st
import random 
# import plotly.express as px
st.title(":heart::pie::broccoli::cut_of_meat::stuffed_flatbread:")
st.title("Personalised Nutrition Guide")
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

st.write(f'Personalisation for {name}: {select_sex},  {select_age},  {select_activity},  {select_diet}')
# click1 = st.button("Calculate daily target calories")
# if click1:
#   st.subheader('Recommended daily intakes:')
#   st.write(f'Total Calories: {daily_calories} cals')
#   st.write(f'  of which Carbs: {daily_carbs:.0f} cals')
#   st.write(f'  of which Protein: {daily_protein:.0f} cals')
#   st.write(f'  of which Fat: {daily_fat:.0f} cals')
  
df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSA-4GwaF1Ymi0mZWJGaXhQEQhBxYhMKJ_GrxsFDo1e83kSAHi0fFfrWIEJkzcB4IBaANuhUMd-IF1S/pub?gid=1836603224&single=true&output=csv")
 
## FOOD RECOMMEND FUNCTION
def food_func(sex, age, activity, diet_pref):  
## Macro Calculator:
  daily_calories = df2.loc[(df2['Sex']== sex) & (df2['Age_group'] == age), activity].iat[0]
  ## macro intakes, in cals
  daily_carbs = (daily_calories/100)*51
  daily_protein = (daily_calories/100)*25
  daily_fat = (daily_calories/100)*24 
  ## macro intakes in grams
  carb_grams = (daily_carbs/4)
  prot_grams = (daily_protein/4)
  fat_grams = (daily_fat/9)
  if diet_pref == 'Meat':
    Categories = [('Vegetables',3),('Fruits',2),('Breads, Carbs',3),('Meat, Poultry',2),('Fish, Seafood',1),
                    ('Dairy products',2),('Desserts, sweets',1)]
  elif diet_pref == 'Pescatarian':
    Categories = [('Vegetables',3),('Fruits',2),('Breads, Carbs',3),('Fish, Seafood',2),('Legumes, Nuts',1),
                    ('Dairy products',2),('Desserts, sweets',1)]
  elif diet_pref == 'Vegetarian':
    Categories = [('Vegetables',2),('Fruits',2),('Breads, Carbs',4),('Dairy products',2),('Desserts, sweets',1),
                   ('Legumes, Nuts',2),('Vegetables',1)]
  random.seed(5)
  N=0
  P=0
  C=0
  F=0
  meal_plan = pd.DataFrame()
  my_lst = [0,1,2,3,4,5,6]
  while (N <= daily_calories) and (C <= carb_grams) and (P <= prot_grams) and (F <= fat_grams):
    try:
      i = random.choice(my_lst)
    except:
      break
    meal1 = df.loc[df.Category == Categories[i][0]].sample(n=Categories[i][1])     
    N += int(meal1['Calories'].sum())
    P += int(meal1['Protein'].sum())
    C += int(meal1['Carbs'].sum())
    F += int(meal1['Fat'].sum())
    my_lst.remove(i)
    if (N <= daily_calories) and (C <= carb_grams) and (P <= prot_grams) and (F <= fat_grams):  
      meal_plan = pd.concat([meal1, meal_plan])   
    else: 
      break 
    return meal_plan, N, C, P, F
  
meal_plan, N, C, P, F = food_func(select_sex, select_age, select_activity, select_diet)  

click2 = st.button("Recommend a meal plan")
if click2:
  meal_plan
  st.write(f'Total Calories: {N}kcal, \n Total Carbs: {C}g / {C*4} cals, \n Total Protein: {P}g / {P*4} cals, \n Total Fats: {F}g / {F*9} cals')

  
# fig = px.scatter(df, x='Region', y='Sales')
# st.plotly_chart(fig)
# # Bar graph to show 
# fig = px.bar(df, x=pick, y='Sales')
# st.plotly_chart(fig)
### [documentation](# https://docs.streamlit.io)
### [community forums](# https://discuss.streamlit.io)

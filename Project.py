import streamlit as st
import pandas as pd 
import warnings 
import matplotlib.pyplot as plt 
import seaborn as sns 
import math
import numpy as np
warnings.filterwarnings('ignore')
df=pd.read_csv('car_web_scraped_dataset.csv')
# Buttons
primary_btn=st.button(label='Primary',type='primary')
secondary_btn=st.button(label='Secondary',type='secondary')
if primary_btn:
    st.write('Hello from primary')
if secondary_btn:
    st.write('Hello from secondary')

#Checkbox
st.divider()
checkbox=st.checkbox(label='Remember me ')
if checkbox:
    st.write('I will rememeber you')
else:
    st.write('I will forget you ')
# Radio Buttons 
st.divider()
radio=st.radio('Chose a column',options=df.columns[1:],index=0,horizontal=True)
st.write(radio)
#Selectbox
st.divider()
select=st.selectbox('Chose a column',options=df.columns[1:],index=0)
st.write(select)
st.divider()
select2=st.selectbox('Chose a price',options=[1000,2000,3000,4000,5000])
st.write(select2)
#Mutilselect
st.divider()
multiselect=st.multiselect('Choose as many columns as you want',options=df.columns[1:],default=['price'],max_selections=math.floor(len(df.columns)/2))
st.write(multiselect)
# Slider
df['price']=df['price'].str.replace('$','')
df['price']=df['price'].str.replace(',','')
df['price']=df['price'].astype(int)
st.divider()
slider=st.slider(label='Slide it',step=1000,value=math.floor(np.mean(df.price)),min_value=np.min(df.price),max_value=np.max(df.price))
st.write(slider)
#Text input 
st.divider()
text_input=st.text_input(label='Write something')
st.write(text_input)
# Number input 
st.divider()
num_imput=st.number_input(label='Pick a number ',min_value=0,max_value=10,step=1)
st.write(f"you picked {num_imput}")
# Text area 
text_area=st.text_area(label='What do you want to tell meeeee?',height=200,placeholder='Write your message here')
st.write(text_area)



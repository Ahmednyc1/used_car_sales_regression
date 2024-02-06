import streamlit as st
import pandas as pd 
import warnings 
import matplotlib.pyplot as plt 
import seaborn as sns 
import math
import numpy as np
warnings.filterwarnings('ignore')

with st.form('my_form'):
    st.write('What would you like to order')
    appetizers=st.selectbox(label='Appitizers',options=['Choice1','Choice2','Choice3'])
    main_course=st.selectbox(label='Main course',options=['Choice4','Choice5','Choice6'])
    Desert=st.selectbox(label='Desert',options=['Choice 7','Choice 8','Choice 9'])
    checkbox=st.checkbox(label='Are you bringin your own wine?')
    data=st.date_input(input='When are you coming ')
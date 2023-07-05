import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import plotly.express as px

import plotly.graph_objects as go

from urllib.request import urlopen
import json

df = pd.read_csv('mpg.csv')

st.title('Introduction to Streamlit')

st.header('MGP Data exploration')

# create a side bar

if st.sidebar.checkbox('Show Dataframe'):
    st.subheader('This is my dataset')
    st.dataframe( data = df)

left_column, middle_columns, right_column = st.columns([3, 1, 1])

# widget
years = ['All'] + sorted(pd.unique(df['year']))
year = st.sidebar.selectbox('Choose a year', years)

if year == 'All':
    reduced_df = df

else:
    reduced_df = df[df['year'] == year]

m_fig, ax = plt.subplots(figsize = (10, 8))
ax.scatter(reduced_df['displ'], reduced_df['hwy'])

ax.set_title('Engine size vs mileage')

st.pyplot(m_fig)
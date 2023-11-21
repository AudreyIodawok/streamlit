#!/usr/bin/env python
# coding: utf-8

# In[2]:

import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

st.markdown('<h1 style="color:blue;">Exploration on cars data</h1>', unsafe_allow_html=True)

st.write('Hereunder some technical data about cars and their country of origin :')

cars = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv', sep = ',')

cars['year'] = pd.to_datetime(cars['year'], format = '%Y')
cars['year'] = cars['year'].dt.year
cars['continent_fac'] = cars['continent'].factorize()[0]

cars

st.markdown('<h2 style="color:blue;">Technical data correlations</h2>', unsafe_allow_html=True)
st.write('These are the technical information correlations :')

viz_correlation = sns.heatmap(cars.corr(), center = 0, cmap = sns.color_palette('vlag', as_cmap = True))
st.pyplot(viz_correlation.figure)

st.write("""
         There seems to be a positive correlation between cylinders, 
         cubicinches, hp and weight in lbs.
         There is little to no relation between the country of origin and
         the power of cars.
         The distance in miles (mpg) that a car can travel is becoming
         greater as time goes by.
         """)

st.markdown('<h2 style="color:blue;">Relationship between production year and mpg</h2>', unsafe_allow_html=True)


#!/usr/bin/env python
# coding: utf-8

# In[2]:

import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

st.markdown('<h1 style="color:blue;">Exploration on cars data</h1>', unsafe_allow_html=True)

st.write("""
         In this analysis, we are going to compare cars technical features depending on 
         their continents of origin and over a period of time going from 1971 to 1983.
         
         Hereunder some technical data about cars and their continent of origin :""")

cars = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv', sep = ',')

cars['year'] = pd.to_datetime(cars['year'], format = '%Y')
cars['year'] = cars['year'].dt.year
cars['continent_fac'] = cars['continent'].factorize()[0]

cars

st.markdown('<h2 style="color:blue;">Technical data correlations</h2>', unsafe_allow_html=True)
st.write('These are the technical information correlations :')


sns.heatmap(cars.corr(), center = 0, cmap = sns.color_palette('vlag', as_cmap = True)).figure


st.write("""
         There seems to be a positive correlation between cylinders, 
         cubicinches, hp and weight in lbs.
         There is little to no relation between the country of origin and
         the power of cars.
         The distance in miles (mpg) that a car can travel is becoming
         greater as time goes by.
         """)

plt.close()

st.markdown('<h2 style="color:blue;">Relationship between production year and mpg</h2>', unsafe_allow_html=True)

st.header("Violin & Scatter")

st.write("""
         From these two plots, we can see the evolution of mpg in time.
         The violinplot shows that the ability of cars to travel long distances has increased
         over years.
         The scatterplot illustrates the differences of mpg evolution depending on cars origins.
         """)

sd = st.selectbox(
    "Select a Plot", #Drop Down Menu Name
    [
    "Violin Plot", #First option in menu
    "Scatter Plot"   #Second option in menu
    ]
    )

fig = plt.figure(figsize=(12, 6))

if sd == "Violin Plot":
    sns.violinplot(x = 'year', y = 'mpg', data = cars)
    
elif sd == "Scatter Plot":
    sns.scatterplot(data = cars, x = 'year', y = 'mpg', hue = 'continent')

st.pyplot(fig)

st.write("""
         The violinplot shows that the ability of cars to travel long distances has increased
         over years.
         The average mpg stays quite stable from 1971 to around 1978 (between 15 and 20 miles). 
         Then we can see that a small proportion of cars produced around 1979 and 1980 
         seem to be able to travel longer distances (from 40 to 50 miles). 
         In the years forward, the average mpg gets higher (around 30 to 40 miles).

         The scatterplot illustrates the differences of mpg evolution depending on cars 
         origins.
         If the global mpg gets higher over time, there are differences between cars produced
         in Europe, Japan and the US.
         The european and japanese cars seem to have an overall mpg that sits higher than 
         their american counterparts.
         """)
plt.close()

st.markdown('<h2 style="color:blue;">What about the other technical features ?</h2>', unsafe_allow_html=True)

st.write("""
         The following plots display technical features of cars coming from either Japan,
         Europe or the United States.
         """)

df_japan = cars.loc[cars['continent'].str.lower().str.contains('japan')]
#df_japan
df_europe = cars.loc[cars['continent'].str.lower().str.contains('europe')]

df_us = cars.loc[cars['continent'].str.lower().str.contains('us')]

sd2 = st.selectbox(
    "Select a Continent", #Drop Down Menu Name
    [
    "Japan", #First option in menu
    "Europe", #Second option in menu
    "United States" #Third option in menu
    ]
    )

if sd2 == "Japan":

    fig2, axes2 = plt.subplots(1, 3, figsize=(20, 10))
    sns.boxplot(data = df_japan, x = "year", y = "weightlbs", ax = axes2[0])
    axes2[0].set_title('Weight of cars over the years', fontsize = 25)

    sns.boxplot(data = df_japan, x = "year", y = "hp", ax = axes2[1])
    axes2[1].set_title('HP of cars over the years', fontsize = 25)

    sns.boxplot(data = df_japan, x = "year", y = "cubicinches", ax = axes2[2])
    axes2[2].set_title('Cubicinches over the years', fontsize = 25)

    plt.tight_layout()

    st.pyplot(fig2)

    st.write("""
            For japanese cars, the weight has increased over the years 1971 to 1974, 
            decreasing in 1975 but there were no big weight differences between cars. 
            Then starting year 1976, we can notice than the differences in weight become more 
            important, as more types of cars come on the market. The median weight decreased 
            and then increased again in 1976.
            From then on, the weight of the cars seemed stable and even decreased again in 1983.
            """)
    
elif sd2 == "Europe":

    fig3, axes3 = plt.subplots(1, 3, figsize=(20, 10))
    sns.boxplot(data = df_europe, x = "year", y = "weightlbs", ax = axes3[0])
    axes3[0].set_title('Weight of cars over the years', fontsize = 25)

    sns.boxplot(data = df_europe, x = "year", y = "hp", ax = axes3[1])
    axes3[1].set_title('HP of cars over the years', fontsize = 25)

    sns.boxplot(data = df_europe, x = "year", y = "cubicinches", ax = axes3[2])
    axes3[2].set_title('Cubicinches over the years', fontsize = 25)

    plt.tight_layout()

    st.pyplot(fig3)

    st.write("""
            In regards to european cars, the weight has globally increased over the years 1971 to 1973, 
            with bigger weight differences between cars than on the japanese market. 
            Then starting year 1977, we start noticing than the differences in weight become more 
            important. The median weight decreased and then increased again starting 1978.
            In year 1980, the differencies between cars weight become very noticeable. Then the
            following year the average weight and the differences in weight decrease again. 
            """)

elif sd2 == "United States":

    fig4, axes4 = plt.subplots(1, 3, figsize=(20, 10))
    sns.boxplot(data = df_us, x = "year", y = "weightlbs", ax = axes4[0])
    axes4[0].set_title('Weight of cars over the years', fontsize = 25)

    sns.boxplot(data = df_us, x = "year", y = "hp", ax = axes4[1])
    axes4[1].set_title('HP of cars over the years', fontsize = 25)

    sns.boxplot(data = df_us, x = "year", y = "cubicinches", ax = axes4[2])
    axes4[2].set_title('Cubicinches over the years', fontsize = 25)

    plt.tight_layout()

    st.pyplot(fig4)

    st.write("""
            In regards to north american cars, the weight has globally decreased over the years 
            with bigger weight differences before the 80' than later on.  
            """)


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime




st.title('Data Visualization & Communication')
st.write('This is a web app to show visualizations made on plotly.')
st.write('In this web app we have five different visualizations in which two of them have interactive features to make this experience fun!')





#Plot
st.title("Population of USA States in 2014")
st.write("Below there's a table representing all the states, their postal, and their population.")
df2 = pd.read_csv("/Users/eliesayegh/Library/Containers/com.microsoft.Excel/Data/Downloads/2014 US States Pop.csv")
with st.expander("States Population Data"):
    st.write(df2)
st.write("Under the table, we have a scatter plot in which you can select many different states and compare them to each other.")
options = st.multiselect("Select a State",
                         ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"], default = None)
df2=df2[df2["State"].isin(options)]
fig3 = px.scatter(df2, x ='Postal', y = 'Population', color = "State", size = "Population")
fig3.update_layout ( legend = { "itemclick" : False } ) ;
fig3.update_layout(title='Population of USA States in 2014') ;

st.plotly_chart(fig3)



#New Plot
st.title("USA Life Expectancy")
st.write("Here, you can see a line graph representing the life expectancy of the United States of America throughout the year 1960 all the way to the year 2020.")
df3= pd.read_csv("/Users/eliesayegh/Library/Containers/com.microsoft.Excel/Data/Downloads/usa_life_expectancy_-_temp.csv")
fig4 = px.line(df3, x= 'Years', y = 'Life Expectancy')
fig4.update_layout(title='USA Life Expectancy');

st.plotly_chart(fig4)




#New Plot
st.title("S&P500 Candlestick Chart")
st.write("Here, you can see a candlestick chart representing the S&P500 average throughout the years 2020 till present 2022.")
df4 = pd.read_csv("/Users/eliesayegh/Library/Containers/com.microsoft.Excel/Data/Downloads/sp_-_Sheet1.csv")
fig5 = go.Figure(data=[go.Candlestick(x=df4['Date'],
                open=df4['Open'],
                high=df4['High'],
                low=df4['Low'],
                close=df4['Close*'])])
fig5.update_layout(title='S&P500 Candlestick Chart');

st.plotly_chart(fig5)





#New Plot
st.title("Birds Dying Due to Building Window Collision")
st.write("Here, you can see a pie chart representing the number of birds who died due to building window collision, in a specific area, throughout 4 months.")
df = pd.read_csv("/Users/eliesayegh/Library/Containers/com.microsoft.Excel/Data/Downloads/bird-window-collision-death.csv")
fig = px.pie ( df , values = 'Deaths' , names = 'Bldg Name' , color = "Bldg Name")
fig.update_traces ( textinfo = "label + percent", insidetextfont = dict(color = "white")) ;
fig.update_layout ( legend = { "itemclick" : False } ) ;
fig.update_layout(title="Birds Dying Due to Building Window Collision");

st.plotly_chart(fig)




#New Plot
st.title("Birds Dying Due to Building Window Collision")
st.write("Here we have the data of birds dying to building window collision.")
with st.expander("Birds Collision Data"):
    st.write(df)
bldg = df["Bldg Name"].unique()
st.write("Select a building to have a view of a histogram showing the kind and number of birds who died due to colliding to that specific building.")
options = st.selectbox("Select Building", bldg)
df = df[df["Bldg Name"]==options]
fig2 =px.bar(df, x = 'Bldg Name', y = 'Deaths', color = 'Common Name') ;
fig2.update_layout ( legend = { "itemclick" : False } ) ;
fig2.update_layout(title="Birds Dying Due to Building Window Collision");

st.plotly_chart(fig2)







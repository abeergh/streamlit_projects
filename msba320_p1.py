import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt
import matplotlib.pylab as plt
#st.set_page_config(layout="wide")
#load data
data = pd.read_csv("./00_Maternal_deaths_MMR.csv")
#create checkbox that allow the user to show/hide raw data table
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
st.sidebar.selectbox("Maternal mortality dashboard",("Home","Page2","Page3"))
#create a year slider
year = st.sidebar.slider("Select to filter data by year(200-2017)",2000,2017)
st.sidebar.write("The report year selected is", year) 
#create country drop down list
country = st.sidebar.multiselect("Select countries",list(data.Country))
#group maternal deaths by year worldwide
data_by_year=data.groupby('Year',as_index=False)['Deaths'].sum().reset_index().rename(columns={'sum':'Deaths','Year':'Year'})
#create line chart with total maternal deaths by year
fig0 = px.line(data_by_year, x='Year', y='Deaths', text='Deaths')
fig0.update_traces(textposition="top right")
fig0.update_layout(margin=dict(b=0),autosize=False,title="Total maternal mortality deaths from 2000-2017",width=800,height=300)
st.write(fig0, use_container_width=True)

#create a map to plot maternal mortaity ratio by country
fig1 = px.scatter_geo(data[data['Year']==year], locations = 'Country ISO Code',  color="Maternal mortality ratio", size="Maternal mortality ratio", animation_frame='Year', color_continuous_scale=px.colors.sequential.Plasma, projection='natural earth')
fig1.update_layout(margin=dict(b=0),autosize=False,title="Mapping maternal mortality ratio by country from 2000-2017",width=800,height=300)
st.write(fig1, use_container_width=True)

#create scatter plot maternal mortality ratio vs poverty rate animated by year
fig2 = px.scatter(data[data['Year']==year], x="poverty rate", y="Maternal mortality ratio", animation_frame="Year", animation_group="Country",size="Maternal mortality ratio", color="region", hover_name="Country",log_x=True, size_max=55, range_x=[20,90], range_y=[100,3000])
fig2.update_layout(margin=dict(b=0),autosize=False,title = "Maternal mortality ratio vs poverty rate",width=800,height=300)
st.write(fig2, use_container_width=True)
st.markdown(
        "<div style='margin-bottom: 11px; font-size:10px; text-align: left; color: gray; width: 100%'>Data source: WHO & world bank- Maternal mortality and poverty rate data</div>", 
unsafe_allow_html=True)

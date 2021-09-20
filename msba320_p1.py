import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt

#st.set_page_config(layout="wide")

data = pd.read_excel (r'C:\Users\Abeer\Documents\2.MSBA_Program\MSBA325_Data_visualization\00_Maternal_deaths_MMR.xlsx')
col1, col2, col3 = st.columns(3)
col1.metric("Maternal Mortality", "277K")
#col2.metric("Region with Highest maternal mortality", "Sub-sahran africa")
col3.metric("Report period", "2000-2017")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
#group maternal deaths by year worldwide
data_by_year=data.groupby('Year',as_index=False)['Deaths'].sum().reset_index().rename(columns={'sum':'Deaths','Year':'Year'})
#pd.DataFrame(data_by_year)
fig0 = px.line(data_by_year, x='Year', y='Deaths', text='Deaths')
fig0.update_traces(textposition="top right")
#st.plotly_chart(fig1, use_container_width=True)
fig0.update_layout(margin=dict(b=0),autosize=False,title="Total maternal mortality deaths from 2000-2017")
st.write(fig0, use_container_width=True)
#st.sidebar.slider(data["Year"])
#Create scatter plot maternal mortality ratio vs poverty rate animated by year
st.sidebar.selectbox("Maternal mortality dashboard",("Home","Page2","Page3"))
year = st.select_slider("Select the report year",options=data['Year'])
st.write("The report year is", year)
                   
country = st.multiselect("Choose countries",list(data.Country))
#divide streamlit page into columns to organize the layout of the graphs
#c1, c2 = st.columns(2)
fig1 = px.scatter_geo(data[data['Year']==year], locations = 'Country ISO Code',  color="Maternal mortality ratio", size="Maternal mortality ratio", animation_frame='Year', color_continuous_scale=px.colors.sequential.Plasma, projection='natural earth')
#st.plotly_chart(fig1, use_container_width=True)
fig1.update_layout(margin=dict(b=0),autosize=False,title="Mapping maternal mortality ratio by country from 2000-2017")
st.write(fig1, use_container_width=True)


fig2 = px.scatter(data[data['Year']==year], x="poverty rate", y="Maternal mortality ratio", animation_frame="Year", animation_group="Country",size="Maternal mortality ratio", color="region", hover_name="Country",log_x=True, size_max=55, range_x=[20,90], range_y=[100,3000])
#st.plotly_chart(fig0, use_container_width=True)
fig2.update_layout(margin=dict(b=0),autosize=False,title = "Maternal mortality ratio vs poverty rate")
st.write(fig2, use_container_width=True)
st.markdown(
        "<div style='margin-bottom: 11px; font-size:10px; text-align: left; color: gray; width: 100%'>Data source: WHO & world bank- Maternal mortality and poverty rate data</div>", 
unsafe_allow_html=True
    )
#st.map(data)
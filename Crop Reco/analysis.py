import streamlit as st
import pandas as pd
import database as db
import matplotlib.pyplot as plt         
import plotly.graph_objects as go
import streamlit as stm
from streamlit_extras.dataframe_explorer import dataframe_explorer
import altair as alt
import time
import plotly.express as px

import numpy as np
import json



def app():

    st.title('Data Visualization 📈')

    #data frame is json and looped to access the json items

    dataframe = db.fetch_all()
    Maize = [i["Maize"] for i in dataframe]
    Bean = [i["Bean"] for i in dataframe]
    wheat = [i["wheat"] for i in dataframe]
    rice = [i["rice"] for i in dataframe]
    bananas = [i["bananas"] for i in dataframe]
    cabbage = [i["cabbage"] for i in dataframe]
    njahi = [i["njahi"] for i in dataframe]
    county = [i["key"] for i in dataframe]
    df = pd.DataFrame(dataframe)
    st.table(df)

    chart_visual = st.sidebar.selectbox('Select Charts/Plot type',
                                        ('Line Chart','Bar Chart','Bubble Chart','Line Chart','Pie Chart'))

    st.sidebar.checkbox("show analysis", True, key = 1)

    selected_status = st.sidebar.selectbox('Select Type',
                                            options =  ['Maize','Bean','wheat','rice','bananas','cabbage','njahi'])
    
    
    fig =go.Figure()
    if chart_visual == 'Line Chart':
        if selected_status == 'Maize':
            fig.add_trace(go.Scatter(x = county, y = Maize,
                                        mode = 'lines',
                                        name = 'Maize'))
            st.subheader('Maize')
            
        if selected_status == 'Bean':
            fig.add_trace(go.Scatter(x = county, y =Bean,
                                        mode = 'lines',
                                        name = 'Bean'))
            st.subheader('Bean')
        if selected_status == 'wheat':
            fig.add_trace(go.Scatter(x = county, y =wheat,
                                        mode = 'lines',
                                        name = 'wheat'))
            st.subheader('Wheat')
        
        if selected_status == 'rice':
            fig.add_trace(go.Scatter(x = county, y = rice,
                                        mode = 'lines',
                                        name = 'rice'))
            st.subheader('Rice')
        
        if selected_status == 'bananas':
            fig.add_trace(go.Scatter(x = county, y = bananas,
                                        mode = 'lines',
                                        name = 'bananas'))
            st.subheader('Bananas')
        if selected_status == 'cabbage':
            fig.add_trace(go.Scatter(x = county, y =cabbage,
                                        mode = 'lines',
                                        name = 'cabbage'))
            st.subheader('Cabbage')
        if selected_status == 'njahi':
            fig.add_trace(go.Scatter(x = county, y = njahi,
                                        mode = 'lines',
                                        name = 'njahi'))
            st.subheader('Njahi')


    elif chart_visual == 'Bar Chart':
        if selected_status == 'Maize':
            fig.add_trace(go.Bar(x = county, y=Maize,
                                name='Maize'))
            st.subheader('Maize')
        if selected_status == 'Bean':
            fig.add_trace(go.Bar(x = county, y=Bean,
                                name ='Bean'))
            st.subheader('Bean')
        if selected_status == 'wheat':
            fig.add_trace(go.Bar(x = county, y=wheat,
                                name='wheat'))
            st.subheader('Wheat')
        if selected_status == 'rice':
            fig.add_trace(go.Bar(x = county, y=rice,
                                name="rice"))
            st.subheader('Rice')
        if selected_status == 'bananas':
            fig.add_trace(go.Bar(x = county, y=bananas,
                                name="bananas"))
            st.subheader('Bananas')
        if selected_status == 'cabbage':
            fig.add_trace(go.Bar(x = county, y=cabbage,
                                name="cabbage"))
            st.subheader('Cabbbage')
        if selected_status == 'njahi':
            fig.add_trace(go.Bar(x = county, y=njahi,
                                name ="njahi"))
            st.subheader('Njahi')

    elif chart_visual == 'Bubble Chart':
        if selected_status == 'Maize':
            fig.add_trace(go.Scatter(x=county, 
                                    y=Maize,
                                    mode='markers',
                                    marker_size=[40, 60, 80, 60, 40, 50],
                                    name='Maize'))
            st.subheader('Maize')
            
        if selected_status == 'Bean':
            fig.add_trace(go.Scatter(x=county, y=Bean,
                                    mode='markers', 
                                    marker_size=[40, 60, 80, 60, 40, 50],
                                    name='Bean'))
            st.subheader('Bean')
            
        if selected_status == 'wheat':
            fig.add_trace(go.Scatter(x=county,
                                    y=wheat,
                                    mode='markers', 
                                    marker_size=[40, 60, 80, 60, 40, 50],
                                    name = 'wheat'))
            st.subheader('Wheat')
        if selected_status == 'rice':
            fig.add_trace(go.Scatter(x=county,
                                    y=rice,
                                    mode='markers',
                                    marker_size=[40, 60, 80, 60, 40, 50], 
                                    name='rice'))
            st.subheader('Rice')
        if selected_status == 'bananas':
            fig.add_trace(go.Scatter(x=county,
                                    y=bananas,
                                    mode='markers',
                                    marker_size=[40, 60, 80, 60, 40, 50], 
                                    name='bananas'))
            st.subheader('Bananas')
        if selected_status == 'cabbage':
            fig.add_trace(go.Scatter(x=county,
                                    y=cabbage,
                                    mode='markers',
                                    marker_size=[40, 60, 80, 60, 40, 50], 
                                    name='cabbage'))
            st.subheader('Cabbbage')
        if selected_status == 'njahi':
            fig.add_trace(go.Scatter(x=county,
                                    y=njahi,
                                    mode='markers',
                                    marker_size=[40, 60, 80, 60, 40, 50], 
                                    name='njahi'))
            st.title('Njahi')

    elif chart_visual =='Pie Chart':
        cols = st.columns([1, 1])

        with cols[0]:
            product_type = st.selectbox('Product Type', ['Maize','Bean','wheat','rice','bananas','cabbage','njahi'])
            
            fig = px.pie(df, values=product_type, names=county,
                        title=f'Percentage of {product_type} product',
                        height=400, width=200)
            fig.update_layout(margin=dict(l=40, r=40, t=30, b=0),)
            
            
    
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


    


    
    
    






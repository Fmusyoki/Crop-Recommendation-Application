import streamlit as st
import database as db
import pandas as pd
import requests
import json
    
import streamlit as st
import pandas as pd
import numpy as np



#FILTER TABLE

def app():
    st.title("Filter Data 🔎") 
    dataframe = db.fetch_all()
    df = pd.DataFrame(dataframe)
    'Select a Column'
    filtered = st.multiselect("Filter columns", options=list(df.columns), default=list(df.columns))
    dd = df[filtered]
    st.write(dd)
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')


    csv = convert_df(dd)

    st.download_button(
    "Download",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )
   

  




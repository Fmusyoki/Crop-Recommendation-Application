import streamlit as st
import pandas as pd
import database as db
from io import StringIO
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as stm
from streamlit_extras.dataframe_explorer import dataframe_explorer
import time


    

def app():
    import streamlit as st
    from streamlit_lottie import st_lottie
    import requests
    html_temp_vis = """
    <div style="background-color:#025246 ;padding:10px;margin-bottom:30px">
    <h2 style="color:white;text-align:center;"> Upload CSV  </h2>
    </div>
    """
    st.markdown(html_temp_vis, unsafe_allow_html=True)
        
    

    url = requests.get(
        "https://assets9.lottiefiles.com/packages/lf20_comuBU.json")
    url_json = dict()
    if url.status_code == 200:
        url_json = url.json()
    else:
        print("Error in URL")


    st_lottie(url_json,
            # change the direction of our animation
            reverse=False,
            # height and width of animation
            height=250,
            width=700,
          
            # speed of animation
            speed=1,
            # means the animation will run forever like a gif, and not as a still image
            loop=True,
            # quality of elements used in the animation, other values are "low" and "medium"
            quality='high',
            # THis is just to uniquely identify the animation
            key='load'
            )
    st.subheader('Upload CSV ')
    
    # #FILE UPLOADER
    uploaded_file = st.file_uploader("choose a file")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        # st.write(bytes_data)
        
        #convert to a string based io
        
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # st.write(stringio)
        
        string_data = stringio.read()
        # st.write(string_data)
        
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)
        
        df = pd.DataFrame(dataframe)
        
        filtered_df = dataframe_explorer(df)
        stm.dataframe(filtered_df, use_container_width=True)


        for row in df.itertuples():
            db.insert_data(row.county, str(row.Maize), str(row.Bean), str(row.wheat), str(row.rice), str(row.bananas), str(row.cabbage), str(row.njahi))
            
            
            
            
        
        
    
    
        


   
    







        
        
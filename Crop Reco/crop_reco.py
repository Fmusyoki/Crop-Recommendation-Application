import streamlit as st
import streamlit_authenticator as stauth 
import database as db
import pickle
import numpy as np
import pandas as pd
import streamlit as stm
from streamlit_extras.dataframe_explorer import dataframe_explorer
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import matplotlib.pyplot as plt
import plotly.figure_factory as fff
import seaborn as sns

converts_dict = {
'Altitude' :'altitude',
'Temperature': 'temperature',
'Rainfall': 'rainfall',
'ph': 'ph'}

# model = pickle.load(open('model_pkl', 'rb'))
loaded_model = pickle.load(open("C:/Users/charl/model_pk2", 'rb'))



def predict_crop(temperature, rainfall, ph, altitude):
    input = np.array([[temperature, rainfall, ph, altitude]]).astype(np.float64)
    prediction = loaded_model.predict(input)
    return prediction[0]

def app():
    html_temp_vis = """
    <div style="background-color:#025246 ;padding:10px;margin-bottom:30px">
    <h2 style="color:white;text-align:center;"> Visualize Soil Properties </h2>
    </div>
    """
   

    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> Crop Recommendation  🌱 </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    with st.expander(" ℹ️ Information", expanded=True):
        st.write("""
        Crop recommendation is one of the most important aspects of precision agriculture. Crop recommendations are based on a number of factors. Precision agriculture seeks to define these criteria on a site-by-site basis in order to address crop selection issues. While the "site-specific" methodology has improved performance, there is still a need to monitor the systems' outcomes.Precision agriculture systems aren't all created equal. 
        However, in agriculture, it is critical that the recommendations made are correct and precise, as errors can result in significant material and capital loss.
        """)
    '''
    ## How does it work ❓ 
    Complete all the parameters and the machine learning model will predict the most suitable crops to grow in a particular farm based on various parameters
    '''
    col1,col2 = st.columns([2,2])
    with col1:
        st.subheader(" Find out the most suitable crop to grow in your farm 👨‍🌾")
        st.subheader("Drag to Give Values")
        temperature = st.slider('Temperature', 0.0, 99.9)
        ph = st.slider('pH', 0.0, 9.94)
        rainfall = st.slider('Rainfall', 0.0, 5000.0)
        altitude= st.slider('Altitude', 1000, 2500)
        



        
        # if st.button('Predict'):

        #     loaded_model = load_model('model.pkl')
        #     prediction = loaded_model.predict(single_pred)
        #     predict.success(f"{prediction.item().title()} are recommended by the A.I for your farm.")
        # #code for html ☘️ 🌾 🌳 👨‍🌾  🍃
        
        if st.button("Predict your crop"):
            with col2:
                url = requests.get(
                "https://assets8.lottiefiles.com/packages/lf20_xd9ypluc.json")
                url_json = dict()
                if url.status_code == 200:
                    url_json = url.json()
                else:
                    print("Error in URL")


                st_lottie(url_json,
                        # change the direction of our animation
                        reverse=False,
                        # height and width of animation
                        height=550,
                        width=400,
                        # speed of animation
                        speed=1,
                        # means the animation will run forever like a gif, and not as a still image
                        loop=True,
                        # quality of elements used in the animation, other values are "low" and "medium"
                        quality='high',
                        # THis is just to uniquely identify the animation
                        key='load'
                        )
            output=predict_crop(temperature, ph, rainfall, altitude)
            res = "“"+ output.capitalize() + "”"
            st.success('The most suitable crop for your field is {}'.format(res))

        

        
    hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
        """

    hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)


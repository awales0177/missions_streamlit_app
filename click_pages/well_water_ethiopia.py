import os

import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st
from streamlit_lottie import st_lottie_spinner
from streamlit_lottie import st_lottie
import json
from streamlit_folium import st_folium
import folium
from PIL import Image
import matplotlib.pyplot as plt

def load_well_ethiopia():
    # LAYING OUT THE TOP SECTION OF THE APP
    row1_1, row1_2, row1_3 = st.columns((2, 3, 2))
    with row1_1:
        st.title("Well Water Project - Ethiopia")

    with row1_2:
        st.write(
            """
        ##
        About Life Source Church: Bringing Life through Water

        Welcome to Life Source Church, where our mission goes beyond the walls of our 
        congregation to reach communities in need around the world. Founded on the principles of love, 
        compassion, and service, Life Source Church is committed to making a meaningful impact on the lives of 
        those who lack access to a basic necessity – clean water.
        """
        )

    with row1_3:
        with open("animations/well_animation.json", "r") as f:
            lottie_data = json.load(f)
        st_lottie(lottie_data, loop=True, key="progress")
        #st.write('animation well')

    # LAYING OUT THE MIDDLE SECTION OF THE APP WITH THE MAPS
    row2_1, row2_2, row2_3, row2_4 = st.columns((2, 1, 1, 1))
    row3_1, row3_2 = st.columns((1, 1))

    with row3_1:
        with st.expander("Ethiopia: A Journey of Hope",expanded=True):
            st.write(
                """
                ##   
                In Ethiopia, where arid landscapes and unpredictable 
                climates contribute to water shortages, Life Source Church has embarked on 
                a journey of hope. Through our dedicated team and partners on the ground, 
                we are actively involved in digging wells that not only quench the immediate thirst of 
                communities but also lay the foundation for healthier, more resilient lives.
                    """)
        with st.expander("Join Us in Making a Difference",expanded=True):
            st.write(
                """
                ##   
                At Life Source Church, we invite you to be a part of this life-changing mission. 
                Whether through financial support, volunteering, or spreading awareness, your involvement 
                can contribute to the creation of a world where every person has access to clean water and the 
                opportunity for a brighter future.
                
                Join us as we dig deep, bring life, and make a lasting impact on the communities of Ethiopia and Colombia.
                    """)
    with row3_2:
        st.image('imgs/page_imgs/ethiopia_water.jpg')
import os

import altair as alt
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie_spinner
from streamlit_lottie import st_lottie
import json
from streamlit_folium import st_folium
import folium
from PIL import Image

def load_well_colombia():
    # LAYING OUT THE TOP SECTION OF THE APP
    row1_1, row1_2 = st.columns((9, 3))
    with row1_1:
        st.title("Well Water Project Colombia")
    st.title("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
    st.subheader("Bringing Life through Water")
    st.write(
            """
        ##
        Welcome to Life Source Church, where our mission goes beyond the walls of our 
        congregation to reach communities in need around the world. Founded on the principles of love, 
        compassion, and service, Life Source Church is committed to making a meaningful impact on the lives of 
        those who lack access to a basic necessity – clean water.
        """
        )

    with row1_2:
        with open("animations/well_animation.json", "r") as f:
            lottie_data = json.load(f)
        st_lottie(lottie_data, loop=True, key="progress")
        #st.write('animation well')

    
    st.image('imgs/page_imgs/colombia_w.jpg',caption='Water well in Colombia')
    with st.expander('Mission', expanded=True):
        st.write(
            """
            In Colombia, we witness the transformative power of water as we work hand 
            in hand with local communities. By digging wells and implementing sustainable water 
            management practices, Life Source Church seeks to break the cycle of water-related challenges, 
            fostering a future where every individual has the opportunity to thrive.
                """)

    st.write("""At Life Source Church, we invite you to be a part of this life-changing mission. 
                Whether through financial support, volunteering, or spreading awareness, your involvement 
                can contribute to the creation of a world where every person has access to clean water and the 
                opportunity for a brighter future.
                Join us as we dig deep, bring life, and make a lasting impact on the communities of Ethiopia and Colombia.

                    """)

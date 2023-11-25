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

def load_medical():
    # LAYING OUT THE TOP SECTION OF THE APP
    row1_1, row1_2 = st.columns((9, 3))
    with row1_1:
        st.title("──── HDPTC ────")
    st.write(
            """
        ##
        Life Source Church Healthcare Missions in Nigeria is committed to 
        addressing the pressing healthcare needs of those living in poverty. 
        Guided by our faith and fueled by a passion for humanitarian service, we strive to be a 
        catalyst for positive change, extending a healing touch to the bodies and souls of those in need.
        """
        )

    with row1_2:
        with open("animations/medical_animation.json", "r") as f:
            lottie_data = json.load(f)
        st_lottie(lottie_data, loop=True, key="progress")
        #st.write('animation well')

    
    st.subheader("Key Objectives: Affordable Healthcare for All")
    st.image('imgs/page_imgs/nigeria_h.jpg',caption='Healthcare professionals providing diagnosis')
    with st.expander('Mission', expanded=True):
        st.write("""
            1). Accessible Clinics: Establishing and supporting accessible healthcare clinics in impoverished areas, ensuring that medical care is within reach for everyone.
                    
            2). Health Education: Empowering communities with health education programs, promoting preventive care, and fostering a culture of well-being.
                    
            3). Medical Outreach Programs: Conducting regular medical outreach programs to remote villages, providing essential healthcare services and identifying critical health issues.
                    
            4). Collaboration with Local Partners: Collaborating with local healthcare organizations, government agencies, and community leaders to create a sustainable healthcare ecosystem.
                """)
    row2_1, row2_2 = st.columns((1.25, 1))
    with row2_1:
        st.write("""This map of Nigeria shows states at the different risk levels of socio-economic vulnerability 
                 ranked from 1 to 5, spread across the country. This indicates that most parts of the northwest fall 
                 under high risk (5) compared to states in south-south falling under low risk and medium-low risk (1 and 2) 
                 respectively. Using geo-tagged household survey data and geospatial covariates (satellite imagery and related 
                 derived data products including settlement data), GRID3 Nigeria, through its collaboration with Fraym, 
                 is modelling risk analysis across the country.
                    """)
        st.write('Source: https://grid3.org/')
    with row2_2:
        st.image('imgs/page_imgs/Fraym_map.png',width=300)

    st.write("""Life Source Church invites individuals, healthcare professionals, 
                     and partners to join us in this healing journey. Through financial support, 
                     volunteering, or spreading awareness, you can play a vital role in bringing affordable 
                     healthcare to impoverished communities in Nigeria. Together, let us embody the spirit of Christ by 
                     healing bodies, nurturing souls, and transforming lives through accessible and compassionate healthcare.

                    """)

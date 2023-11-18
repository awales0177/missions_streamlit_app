import os

import altair as alt
import numpy as np
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
    row1_1, row1_2, row1_3 = st.columns((2, 3, 2))
    with row1_1:
        st.title("HDPTC")

    with row1_2:
        st.write(
            """
        ##
        Life Source Church Healthcare Missions in Nigeria is committed to 
        addressing the pressing healthcare needs of those living in poverty. 
        Guided by our faith and fueled by a passion for humanitarian service, we strive to be a 
        catalyst for positive change, extending a healing touch to the bodies and souls of those in need.
        """
        )

    with row1_3:
        with open("animations/medical_animation.json", "r") as f:
            lottie_data = json.load(f)
        st_lottie(lottie_data, loop=True, key="progress")
        #st.write('animation well')

    # LAYING OUT THE MIDDLE SECTION OF THE APP WITH THE MAPS
    row2_1, row2_2, row2_3, row2_4 = st.columns((2, 1, 1, 1))
    row3_1, row3_2 = st.columns((1, 1))

    with row3_1:
        with st.expander("Key Objectives: Affordable Healthcare for All",expanded=True):
            st.write("""
                1). Accessible Clinics: Establishing and supporting accessible healthcare clinics in impoverished areas, ensuring that medical care is within reach for everyone.
                     
                2). Health Education: Empowering communities with health education programs, promoting preventive care, and fostering a culture of well-being.
                     
                3). Medical Outreach Programs: Conducting regular medical outreach programs to remote villages, providing essential healthcare services and identifying critical health issues.
                     
                4). Collaboration with Local Partners: Collaborating with local healthcare organizations, government agencies, and community leaders to create a sustainable healthcare ecosystem.
                    """)
        with st.expander("Join Us in the Healing Journey",expanded=True):
            st.write("""Life Source Church invites individuals, healthcare professionals, 
                     and partners to join us in this healing journey. Through financial support, 
                     volunteering, or spreading awareness, you can play a vital role in bringing affordable 
                     healthcare to impoverished communities in Nigeria. Together, let us embody the spirit of Christ by 
                     healing bodies, nurturing souls, and transforming lives through accessible and compassionate healthcare.

                    """)
    with row3_2:
        st.image('imgs/page_imgs/nigeria_h.jpg')

# -*- coding: utf-8 -*-
# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""An example of showing geographic data."""

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

from click_pages.well_water_ethiopia import load_well_ethiopia
from click_pages.well_water_colombia import load_well_colombia
from click_pages.medical import load_medical
from click_pages.church import load_church
from data import get_m_data

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Missions", page_icon=":taxi:")

#setup dataframe
data_df = pd.DataFrame(get_m_data())
def add_to_map(data):
    for ind in data.index:
        if data['prefix'][ind]!='custom':
            folium.Marker(location=[data['Lat'][ind],data['Lon'][ind]],popup=data['group'][ind], tooltip=data['hover'][ind], icon=folium.Icon(color='lightgray', icon=data['icon'][ind], prefix=data['prefix'][ind])).add_to(my_map)
        else:
            icon = folium.features.CustomIcon(data['icon'][ind], icon_size=(44,50),shadow_image='custom-markers/shadow.png',shadow_size=(50, 64))
            folium.Marker(location=[data['Lat'][ind],data['Lon'][ind]],popup=data['group'][ind], tooltip=data['hover'][ind], icon=icon, prefix=data['prefix'][ind]).add_to(my_map)

#folium.Marker(location=[39.350250,-76.485670],popup="Church", tooltip="Life Source International", icon=folium.Icon(color='lightgray', icon='home', prefix='fa')).add_to(my_map)

row1_1, row1_2, row1_3 = st.columns((1, 1, 1))
row2_1, row2_2, row2_3, row2_4 = st.columns((1, 1, .8,.3))
with row1_2:
    st.title('Life Source Missions')
with row1_1:
    st.image('imgs/ls.png',width=80)
#with row1_3:
#    st.toggle('Dark')
with row2_1:
    with st.expander('About us',expanded=True):
        st.write("""Life Source International Missions is dedicated to spreading the transformative 
                 power of Christ globally, extending support to communities in need.
                 """)
    st.code("""Click on one of the map icons: 
    to learn about the Mission and its Impact. """)
with row2_2:
    with st.expander('Mission',expanded=True):
        st.write("""Life Source International Missions is dedicated to the global 
                 spread of Christianity, sharing the love of Christ with diverse cultures and nations. 
                 Our mission is two-fold: to proclaim the message of salvation through Jesus Christ and to 
                 demonstrate His love through impactful, compassionate outreach initiatives.""")
        button_row_1, button_row_2 = st.columns((4, 1))
        with button_row_2:
            st.link_button("Give", "https://lifesourcechurches.churchcenter.com/giving")
        #st.info('Thank You')
with row2_3:
    with st.expander('Key',expanded=True):
        key_row_1, key_row_2 = st.columns((1, 8))
        with key_row_1:
            st.image('imgs/icon_imgs/home.png')
            st.image('imgs/icon_imgs/tint.png')
            st.image('imgs/icon_imgs/heart.png')
            st.image('imgs/icon_imgs/prayer.png')
            st.image('imgs/icon_imgs/home.png')
            st.image('imgs/icon_imgs/home.png')
        with key_row_2:
            churches_cb = st.checkbox('Churches',True)
            Water_cb = st.checkbox('Water Well',True)
            HDPTC_cb = st.checkbox('HDPTC',True)
            Prayer_cb = st.checkbox('Prayer Center',True)
            country_cb = st.checkbox('Country',True)
            home_cb = st.checkbox('Home for a child',True)
            filt_list = []
            if churches_cb:
                filt_list.append('Church')
            if Water_cb:
                filt_list.append('Water_ethiopia')
                filt_list.append('Water_columbia')
            if HDPTC_cb:
                filt_list.append('Medical')
            if Prayer_cb:
                filt_list.append('Prayer Center')
            if country_cb:
                filt_list.append('Country')
            if home_cb:
                filt_list.append('Home for Children')
            filtered_data = data_df[data_df['group'].isin(filt_list)]

with row2_4:
    local_map = st.toggle('Local')
    #st.selectbox(label='Display Need',options=['Wells','Healthcare'])
if not local_map:
    my_map = folium.Map(location=[0, 140], zoom_start=2,scrollWheelZoom=False)
else:
    my_map = folium.Map(location=[39.350250,-76.485670], zoom_start=8,scrollWheelZoom=False)

add_to_map(filtered_data)


st_data = st_folium(my_map, width=2000, height=500)
st.divider()

if st_data['last_object_clicked_popup'] == 'Water_ethiopia':
    load_well_ethiopia()
if st_data['last_object_clicked_popup'] == 'Water_columbia':
    load_well_colombia()
if st_data['last_object_clicked_popup'] == 'Medical':
    load_medical()
#if st_data['last_object_clicked_popup'] == 'Church':
#    load_church()

st.divider()
row3_1, row3_2, row3_3 = st.columns((1.5, 1, 1))
with row3_1:
     st.write('Life Source Missions')
with row3_2:
    st.write('Powered by Live Data')
with row3_3:
    st.write('Authors: Aaron W.')

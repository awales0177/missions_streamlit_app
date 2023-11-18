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

# LOAD DATA ONCE
@st.cache_resource
def load_data():
    path = "uber-raw-data-sep14.csv.gz"
    if not os.path.isfile(path):
        path = f"https://github.com/streamlit/demo-uber-nyc-pickups/raw/main/{path}"

    data = pd.read_csv(
        path,
        nrows=100000,  # approx. 10% of data
        names=[
            "date/time",
            "lat",
            "lon",
        ],  # specify names directly since they don't change
        skiprows=1,  # don't read header since names specified directly
        usecols=[0, 1, 2],  # doesn't load last column, constant value "B02512"
        parse_dates=[
            "date/time"
        ],  # set as datetime instead of converting after the fact
    )

    return data


# FUNCTION FOR AIRPORT MAPS
def map(data, lat, lon, zoom):
    st.write(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={
                "latitude": lat,
                "longitude": lon,
                "zoom": zoom,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=data,
                    get_position=["lon", "lat"],
                    radius=100,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                ),
            ],
        )
    )


# FILTER DATA FOR A SPECIFIC HOUR, CACHE
@st.cache_data
def filterdata(df, hour_selected):
    return df[df["date/time"].dt.hour == hour_selected]


# CALCULATE MIDPOINT FOR GIVEN SET OF DATA
@st.cache_data
def mpoint(lat, lon):
    return (np.average(lat), np.average(lon))


# FILTER DATA BY HOUR
@st.cache_data
def histdata(df, hr):
    filtered = data[
        (df["date/time"].dt.hour >= hr) & (df["date/time"].dt.hour < (hr + 1))
    ]

    hist = np.histogram(filtered["date/time"].dt.minute, bins=60, range=(0, 60))[0]

    return pd.DataFrame({"minute": range(60), "pickups": hist})



def load_church():
    # STREAMLIT APP LAYOUT
    data = load_data()

    # LAYING OUT THE TOP SECTION OF THE APP
    row1_1, row1_2, row1_3 = st.columns((2, 3, 2))

    # SEE IF THERE'S A QUERY PARAM IN THE URL (e.g. ?pickup_hour=2)
    # THIS ALLOWS YOU TO PASS A STATEFUL URL TO SOMEONE WITH A SPECIFIC HOUR SELECTED,
    # E.G. https://share.streamlit.io/streamlit/demo-uber-nyc-pickups/main?pickup_hour=2
    if not st.session_state.get("url_synced", False):
        try:
            pickup_hour = int(st.experimental_get_query_params()["pickup_hour"][0])
            st.session_state["pickup_hour"] = pickup_hour
            st.session_state["url_synced"] = True
        except KeyError:
            pass


    # IF THE SLIDER CHANGES, UPDATE THE QUERY PARAM
    def update_query_params():
        hour_selected = st.session_state["pickup_hour"]
        st.experimental_set_query_params(pickup_hour=hour_selected)


    with row1_1:
        st.title("Life Source")
        hour_selected = st.slider(
            "Select Time", 0, 23, key="pickup_hour", on_change=update_query_params
        )


    with row1_2:
        st.write(
            """
        ##
        Wells of Life is a 501(c)(3) non-profit Christian organization whose mission is to provide rural 
        Ugandans access to safe, clean water through the installation or restoration of sustainable borehole 
        water wells and WASH (water, sanitation, and hygiene) educational programs.​ Thanks to our supporters, 
        our wells are collectively serving more than 1,000,000 people.
        """
        )

    with row1_3:
        with open("church_animation.json", "r") as f:
            lottie_data = json.load(f)
        st_lottie(lottie_data, loop=True, key="progress")
        #with st_lottie_spinner(lottie_data, loop=True, key="progress",viewBox={'150 150 300 300'}):
        #    time.sleep(5)

    # LAYING OUT THE MIDDLE SECTION OF THE APP WITH THE MAPS
    row2_1, row2_2, row2_3, row2_4 = st.columns((2, 1, 1, 1))

    # SETTING THE ZOOM LOCATIONS FOR THE AIRPORTS
    la_guardia = [40.7900, -73.8700]
    jfk = [40.6650, -73.7821]
    newark = [40.7090, -74.1805]
    zoom_level = 12
    midpoint = mpoint(data["lat"], data["lon"])

    with row2_1:
        st.write(
            f"""**All New York City from {hour_selected}:00 and {(hour_selected + 1) % 24}:00**"""
        )
        map(filterdata(data, hour_selected), 31.684489, 35.052238, 11)

    with row2_2:
        st.write("**La Guardia Airport**")
        map(filterdata(data, hour_selected), la_guardia[0], la_guardia[1], zoom_level)

    with row2_3:
        st.write("**JFK Airport**")
        map(filterdata(data, hour_selected), jfk[0], jfk[1], zoom_level)

    with row2_4:
        st.write("**Newark Airport**")
        map(filterdata(data, hour_selected), newark[0], newark[1], zoom_level)

    row3_1, row3_2 = st.columns((1, 1))

    with row3_1:
        with st.expander("Impact"):
            st.write("""Lorem Ipsum is simply dummy text of 
                    the printing and typesetting industry. Lorem Ipsum has been the industry's 
                    standard dummy text ever since the 1500s, when an unknown printer took a galley of 
                    type and scrambled it to make a type specimen book. It has survived not only five centuries, 
                    but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised
                    in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with 
                    desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                    """)
    with row3_2:
        image = Image.open('DSC_0048.jpg')
        st.image(image)
 

    video_file = open('vid_wt.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
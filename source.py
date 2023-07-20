# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 17:40:23 2023

@author: Chirag Radhakrishna
"""

import streamlit as st
import plotly.express as px
from backend import get_data
from PIL import Image

# Add title, text input, slider, selectbox and subheader
st.title("CRK Weather Forecast Predictor")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value =1, max_value=5, help="Select number of days for forecast analysis")

option = st.selectbox("Select data to view", ("Temperature","Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature/sky data
    try:
        filtered_data  = get_data(place, days)
        
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] /10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x = dates, y = temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
            
        if option == "Sky":
            images = {"Clear":"clear.png",
                      "Clouds":"cloud.png",
                      "Rain":"rain.png",
                      "Snow":"snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            #st.write(sky_conditions)
            for condition in sky_conditions:
                img = Image.open(images[condition])
                st.image(img, width = 50)
                
    except KeyError:
        st.write("The place you entered does not exist")
        

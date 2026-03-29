# -*- coding: utf-8 -*-
"""
Video Game Global Sales Prediction App
"""

import streamlit as st
import numpy as np
import pickle

# Load Trained Model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# App UI
st.set_page_config(page_title="Video Game Sales Predictor", layout="centered")

st.title("🎮 Video Game Global Sales Predictor")
st.markdown("Predict **Global Sales** of a video game using Linear Regression")

st.divider()

# Mapping dictionaries (example — update based on your dataset enc

platform_dict = {
    "DS": 0,
    "PS2": 1,
    "PS3": 2,
    "Wii": 3,
    "X360": 4,
    "PSP": 5,
    "PS": 6,
    "PC": 7,
    "XB": 8,
    "GBA": 9,
    "GC": 10,
    "3DS": 11,
    "PSV": 12,
    "PS4": 13,
    "N64": 14,
    "SNES": 15,
    "XOne": 16,
    "SAT": 17
}

genre_dict = {
    "Action": 0,
    "Sports": 1,
    "Shooter": 2,
    "Role-Playing": 3,
    "Platform": 4,
    "Misc": 5,
    "Racing": 6,
    "Simulation": 7,
    "Adventure": 8,
    "Fighting": 9,
    "Strategy": 10,
    "Puzzle": 11
}

publisher_dict = {
    "Nintendo": 0,
    "Electronic Arts": 1,
    "Activision": 2,
    "Sony Computer Entertainment": 3,
    "Ubisoft": 4,
    "Technos Japan Corporation": 5,
    "Electronic Arts":6
}

# User Inputs
rank = st.number_input("Game Rank", min_value=1, step=1)
year = st.number_input("Release Year", min_value=1980, max_value=2025, step=1)
platform_name = st.selectbox("Select Platform", list(platform_dict.keys()))
genre_name = st.selectbox("Select Genre", list(genre_dict.keys()))
publisher_name = st.selectbox("Select Publisher", list(publisher_dict.keys()))

platform = platform_dict[platform_name]
genre = genre_dict[genre_name]
publisher = publisher_dict[publisher_name]

na_sales = st.number_input("NA Sales", min_value=0.0)
eu_sales = st.number_input("EU Sales", min_value=0.0)
jp_sales = st.number_input("JP Sales", min_value=0.0)
other_sales = st.number_input("Other Sales", min_value=0.0)




# Prediction
if st.button("Predict Global Sales 🚀"):
    input_data = np.array([[
        year,
        platform,
        genre,
        publisher,
        na_sales,
        eu_sales,
        jp_sales,
        other_sales
    ]])

    prediction = model.predict(input_data)

    st.success(f"🌍 Predicted Global Sales: **{prediction[0]:.2f} million units**")

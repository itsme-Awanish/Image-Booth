import streamlit as st
import pandas as pd

st.header("Image Booth")

image_path = st.file_uploader('Upload an image')

st.write("Here is your dataset:")
data = pd.read_csv("results.csv")
st.write(data)

st.button("Download Excel")

    

# importing the streamlit library and pandas library
import streamlit as st
import pandas as pd
from backend import analyse_face, image_folder 
# Title of the app  
st.header("Image Booth 🛠️")
st.subheader("Analyze the image dataset / folder")
st.markdown("<span style='color:red'>Please use the less count of images in the folder for better performance and less wait time</span>", unsafe_allow_html=True)
folder_path = st.text_input('Enter the directory path')
st.write("Please enter the directory path of the folder containing the images you want to analyze and do use double backward slash instead of single backward slash in the path")
st.text(r"Example: C:\\Users\\user\\Desktop\\images")
pr = st.button('Analyze')
if pr == True:
    with st.spinner('Analyzing your image...'):    
        image_paths = image_folder(folder_path)
        result_df = analyse_face(image_paths)
        st.write("Here is your Result dataset:")
        st.write(result_df)
st.write("Thank you for using the app ❤️")
name_list =['Juhi Kumari (KIIT University MCA department)', 'Awanish Kumar (KIIT University MCA department)', 'Aviral Bajpai (KIIT University MCA department)']
markdown_string = '\n'.join(f'- {item}' for item in name_list)
st.write("Developed by :")
st.markdown(markdown_string, unsafe_allow_html=True)
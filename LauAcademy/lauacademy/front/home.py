import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import urllib.request


st.title('Lau Academy')
image = Image.open('media/dab.png')
st.image(image, caption='Kiaran - Founder | CEO | LauAcademy')


st.write("Hello! Welcome to LauAcademy chatroom, type your questions below")
st.text_input(label="Your Question:", key="textbox1")
st.file_uploader(label="", type=None, accept_multiple_files=False, key=None, help=None,
    on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue() # read file as bytes
    st.write(bytes_data)

    stringio = StringIO(uploaded_file.getvalue().decode("utf-8")) # convert to string based IO:
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    
    # print("YourPersonalAcademicBot:", response)
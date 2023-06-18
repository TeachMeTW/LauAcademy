import streamlit as st
import pandas as pd
import numpy as np

import io
from io import StringIO
from PIL import Image
import urllib.request

st.set_page_config(
    page_title="Kon Academy",
    page_icon="📘",
)

st.sidebar.success("Select a page from above")

image = Image.open('LauAcademy/lauacademy/media/kon-academy.png')
st.image(image, caption=None)


st.header("👋📘 Hello! Welcome to :blue[Kon Academy].")
st.write("Type your questions below!")
st.text_input(label="Your Question:", key="textbox1")

# Question: How would I combine streamlit file_uploader element and feed the PDF file into a pinecone vector database?
uploaded_file = st.file_uploader("Upload Textbook (PDF)") 
if uploaded_file is not None: # only uploads one file at a time
    bytes_data = uploaded_file.getvalue() # read file as bytes
    st.write(bytes_data)

    stringio = StringIO(uploaded_file.getvalue().decode("utf-8")) # convert to string based IO:
    st.write(stringio)

    string_data = stringio.read() # read file as string:
    st.write(string_data)

    dataframe = pd.read_csv(uploaded_file) # to accept files
    st.write(dataframe)
    
    
def callback(uploaded_file):
  print(uploaded_file)
  with io.open(uploaded_file, "rb") as f:
      file_content = f.read() #read file
  st.write("File content:", file_content)

uploaded_file = st.file_uploader("Upload a file (PDF):", on_change=callback) # Create file uploader

if uploaded_file:
  print(uploaded_file)
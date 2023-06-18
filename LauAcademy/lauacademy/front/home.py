import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
from PIL import Image
import urllib.request


st.title('Lau Academy')
image = Image.open('LauAcademy/lauacademy/front/media/dab.png')
st.image(image, caption='Kiaran - Founder | CEO | LauAcademy')


st.write("Hello! Welcome to LauAcademy chatroom, type your questions below")
st.text_input(label="Your Question:", key="textbox1")
# st.file_uploader(
#     label="Upload File",
#     type=None,
#     accept_multiple_files=False,
#     key=None,
#     help=None,
#     on_change=None,
#     args=None,
#     kwargs=None,
#     disabled=False,
#     label_visibility="visible",
# )

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
    
    # print("YourPersonalAcademicBot:", response)
    
def callback(uploaded_file):
  print(uploaded_file)
  with io.open(uploaded_file, "rb") as f:
      file_content = f.read() #read file
  st.write("File content:", file_content)

uploaded_file = st.file_uploader("Upload a file (PDF):", on_change=callback) # Create file uploader

if uploaded_file:
  print(uploaded_file)
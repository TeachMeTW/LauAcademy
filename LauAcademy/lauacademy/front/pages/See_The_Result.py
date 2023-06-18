import streamlit as st
from PIL import Image

from lauacademy.front.pages.data_class.SharedData import SharedData
shared_data = SharedData()

image = Image.open('LauAcademy/lauacademy/media/see-the-result-high-resolution-color-logo.png')
st.image(image)

st.write( shared_data.get_test() )
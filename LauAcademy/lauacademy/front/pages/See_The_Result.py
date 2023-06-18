import streamlit as st
from PIL import Image

image = Image.open('LauAcademy/lauacademy/media/see-the-result-high-resolution-color-logo.png')
st.image(image)
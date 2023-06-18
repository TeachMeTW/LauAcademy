import streamlit as st
from PIL import Image

image = Image.open('LauAcademy/lauacademy/media/see-the-result-high-resolution-color-logo.png')
st.image(image)

video_file = open('LauAcademy\lauacademy\media\TestSpidermanMV.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

st.write('*Hello* :sunglasses:')
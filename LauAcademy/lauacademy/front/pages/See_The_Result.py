import streamlit as st
from PIL import Image

from lauacademy.front.pages.data_class.SharedData import SharedData
shared_data = SharedData()

user_information = shared_data.get_user_information()

# Input Error Handling
if user_information == None:
    st.subheader("⚠️ Please enter your information in the User Input Page!")
else:
    image = Image.open('LauAcademy/lauacademy/media/see-the-result-high-resolution-color-logo.png')
    st.image(image)

    # video_file = open('LauAcademy\lauacademy\media\TestSpidermanMV.mp4', 'rb')
    # video_bytes = video_file.read()
    # st.video(video_bytes)

    st.write(f'Hello, {shared_data.get_user_information()["name"]}!')
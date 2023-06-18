import streamlit as st
from PIL import Image
import time

from lauacademy.front.pages.data_class.SharedData import SharedData
shared_data = SharedData()
name = None # Need this line to send into callback_test_name()

def callback_success():
    progress_bar = st.progress(0, "Loading...")
    for i in range(100):
        progress_bar.progress(i)
        time.sleep(1/50)
    st.sidebar.success("Successfully uploaded your textbook!\nCheck the \"See The Result\" Tab.")

image = Image.open('LauAcademy/lauacademy/media/enter-your-information-high-resolution-color-logo.png')
st.image(image)
st.subheader("This will help shape your lecture plans.")
name = st.text_input(label="What is your name?", key="t0")
educational_background = st.text_input(label="What is your educational background?", key="t1")
desired_career = st.text_input(label="What is your desired career?", key="t2")
class_subject = st.text_input(label="What is the subject of this class?", key="t3")
uploaded_file = st.file_uploader("Attach your Textbook's PDF here:", on_change=callback_success) 


user_information = {
    "name": name,
    "educational_background": educational_background,
    "desired_career": desired_career,
    "class_subject": class_subject,
    "uploaded_file": uploaded_file
}

def onclick_confirm():
    print('clicked confirm!')
    st.sidebar.success("Successfully confirmed your user data.")
    shared_data.store_user_information(user_information)

confirmation_button = st.button(label="Confirm", on_click=onclick_confirm)
import streamlit as st
from PIL import Image
import time

def callback_success():
    for i in range(100):
        st.progress(i, text="Loading...")
        time.sleep(1/20)
    st.sidebar.success("Successfully uploaded your textbook!\nCheck the \"See The Result\" Tab.")
    

image = Image.open('LauAcademy/lauacademy/media/enter-your-information-high-resolution-color-logo.png')
st.image(image)
st.subheader("This will help shape your lecture plans.")
st.text_input(label="What is your educational background?", key="t1")
st.text_input(label="What is your desired career?", key="t2")
st.text_input(label="What is the subject of this class?", key="t3")
uploaded_file = st.file_uploader("Attach your Textbook's PDF here:", on_change=callback_success) 

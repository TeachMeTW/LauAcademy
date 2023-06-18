import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import urllib.request

import time

# st.title('Lau Academy')
# image = Image.open('media/dab.png')
# st.image(image, caption='Kiaran - Founder | CEO | LauAcademy')\

def user_input_page():
    st.empty()
    st.title("LauAcademy")
    st.write("Welcome to LauAcademy!")

def different_page():
    st.empty()
    st.title("Different Page")
    st.write("This is a different page.")


pages = {
    "Input Page": user_input_page,
    "Different Page": different_page,
}

user_input_page()
time.sleep(3)
different_page()
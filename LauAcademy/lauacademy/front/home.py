import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import urllib.request


image = Image.open('LauAcademy\media\lau-academy-logo.png')
st.image(image, caption=None)

st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title('Lau Academy')
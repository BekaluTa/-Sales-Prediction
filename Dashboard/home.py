import streamlit as st
import streamlit.components.v1 as components
from PIL import Image


def home_app():
    st.title("Home")
    image = Image.open('./Data/alldaycomp.png')
    st.image(image, caption="All Day Sales", use_column_width=True)
    # components.html(
    #     """<html><body><h3>A detailed analysis of customer's data of a</h3></body></html>""", width=200, height=200)
    st.write(
        "Pharmacy Sales Data Detail analysis")
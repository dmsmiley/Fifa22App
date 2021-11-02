import streamlit as st
import numpy as np
import requests
from io import BytesIO
from PIL import Image

def app():
    response = requests.get("https://images.unsplash.com/photo-1606925797300-0b35e9d1794e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1162&q=80")
    display = Image.open(BytesIO(response.content))
    display = np.array(display)
    # st.image(display, width = 400)
    # st.title("Data Storyteller Application")
    col1, col2 = st.columns(2)

    with col1:
        st.image(display)
        st.write('Photo by [Md Mahdi](https://unsplash.com/@mahdi17?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/soccer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)')

    with col2:
        st.title("Analytics with FIFA 22")
        st.markdown('###### Streamlit App by [David Smiley](https://www.linkedin.com/in/david-m-smiley/)')
        st.markdown('##### \n\n Use the App Navigation tool on the left to compare players and clubs in FIFA 22')
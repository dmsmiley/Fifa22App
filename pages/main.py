import streamlit as st
import numpy as np
from PIL import  Image

def app():
    display = Image.open('logo.jpeg')
    display = np.array(display)
    st.write('Photo by [Md Mahdi](https://unsplash.com/@mahdi17?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/soccer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)')
    # st.image(display, width = 400)
    # st.title("Data Storyteller Application")
    col1, col2 = st.columns(2)

    with col1:
        st.image(display)

    with col2:
        st.title("Analytics with FIFA 22")
        st.subheader('Streamlit App by [David Smiley](https://www.linkedin.com/in/david-m-smiley/)')

    """Photo by <a href="https://unsplash.com/@mahdi17?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Md Mahdi</a> on <a href="https://unsplash.com/s/photos/soccer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  """
import os
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports
from multipage import MultiPage
from pages import player_comparison # import your pages here

# Create an instance of the app
app = MultiPage()

# Title of the main page
#display = Image.open('Logo.png')
#display = np.array(display)
# st.image(display, width = 400)
# st.title("Data Storyteller Application")
col1, col2 = st.columns(2)
#col1.image(display, width = 400)
col2.title("FIFA 22 Applications")

# Add all your application here
app.add_page("Player Comparison", player_comparison.app)


# The main app
app.run()
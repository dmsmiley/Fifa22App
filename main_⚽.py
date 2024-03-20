import streamlit as st
import numpy as np
import requests
from io import BytesIO
from PIL import Image

response = requests.get("https://images.unsplash.com/photo-1606925797300-0b35e9d1794e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1162&q=80")
display = Image.open(BytesIO(response.content))
display = np.array(display)

col1, col2 = st.columns(2)

with col1:
        st.image(display)
        st.write(' Photo by [Md Mahdi](https://unsplash.com/@mahdi17?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/soccer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)')

with col2:
        st.title("Analytics with FIFA 22 ⚽")
        st.markdown('###### Streamlit App by [David Smiley](https://www.linkedin.com/in/david-m-smiley/)')
        st.markdown('Application Tabs in the Left Panel')

st.markdown("***")

st.header("Applications:")

st.subheader("1) Player Comparison 🤼‍♀️")

col1_1, col1_2 = st.columns(2)

with col1_1:
    st.image("images/player_comp.JPG", width=200)
with col1_2:
    st.markdown("###### Compare two players from FIFA 22's entire roster.")
    st.markdown("###### Need help deciding who to compare? Use the tool on the left to find players.")

st.subheader("2) League Distribution 🏆")
col2_1, col2_2 = st.columns(2)
with col2_1:
    st.image("images/league_dist.JPG", width=200)
with col2_2:
    st.markdown("###### See how teams within leagues compare in a selected stat.")
    st.markdown("###### Expansion 1 allows you to select a club in the league and the stats of individual players.")
    st.markdown("###### Expansion 2 is for comparing teams regardless of their league.")

st.subheader("3) Player Recommendation 🥇")
col3_1, col3_2 = st.columns(2)
with col3_1:
    st.image("images/player_rec.JPG", width=200)
with col3_2:
    st.markdown("###### Uses the K-Nearest Neighbor algorithm to determine the 10 players most like your selected player.")


st.subheader("4) Custom Recommender 🎯")
col4_1, col4_2 = st.columns(2)
with col4_1:
    st.image("images/custom_rec.JPG", width=200)
with col4_2:
    st.markdown("###### Like the Player Recommender app, however, you can fine tune each stat.")

st.markdown("***")

st.markdown("Partial data provided by ['FIFA 22 Complete Player Dataset'](https://www.kaggle.com/cashncarry/fifa-22-complete-player-dataset)")
st.markdown("All other data was collected from [sofifa.com](https://sofifa.com/)")

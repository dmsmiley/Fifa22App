
# Custom imports
from multipage import MultiPage
from pages import player_comparison, main, team_distribution # import your pages here
import streamlit as st

st.set_page_config(layout="wide")

# Create an instance of the app
app = MultiPage()

# Add all your application here
app.add_page("Main Page", main.app)
app.add_page("Player Comparison", player_comparison.app)
app.add_page("League Distribution", team_distribution.app)


# The main app
app.run()
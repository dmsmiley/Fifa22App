# Contents of ~/my_app/streamlit_app.py
import streamlit as st

def main_page():
    st.markdown("# Main page")
    st.sidebar.markdown("# Main page")

def page2():
    st.markdown("# Player Recommendation")
    st.sidebar.markdown("# Player Recommendation")

def page3():
    st.markdown("# Player Comparison")
    st.sidebar.markdown("# Player Comparison")

def page4():
    st.markdown("# League Distribution")
    st.sidebar.markdown("# Player Comparison")

def page5():
    st.markdown("# Custom Recommendation")
    st.sidebar.markdown("# Player Comparison")
    
page_names_to_funcs = {
    "Main Page": main_page,
    "Player Recommendation": page2,
    "Player Comparison": page3,
    "League Distribution": page4,
    "Custom Recommendation": page5
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

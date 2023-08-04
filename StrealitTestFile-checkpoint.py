import streamlit as st
import pandas as pd
import numpy as np

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")
    page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,}
        
def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")
    
    
    page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())

page_names_to_funcs[selected_page]()
import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')
DATE_COLUMN = 'Date/Time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data['Date/Time'] = pd.to_datetime(data['Date/Time'])
    uppercase = lambda x: str(x).upper()
    data.rename(uppercase, axis='columns',inplace=True)
    return data
    
# Create a text element and let the reader know the data is loading.
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
#data_load_state.text("Done! (using st.cache_data)")
col1 = st.columns()

with col1:
    st.header('Home')
    tab1, tab2 = st.tabs(["View1","View2"])
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.write(data)
        with col2:
            st.subheader('Number of pickups by hour')
            hist_values = np.histogram(
        data['DATE/TIME'].dt.hour, bins=24, range=(0,24))[0]
            st.bar_chart(hist_values)
    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")
from PIL import Image

DATE_COLUMN = 'Date/Time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
def load_data(table):
    data = pd.read_excel('pages/Dataset.xlsx', sheet_name = table)
    return data


def French_Doors():
    st.header("French Door Refridgerator")
    st.markdown("Recycling, repairing, and reselling your refrigerator is a responsible choice that benefits both the environment and your wallet. Recycling old refrigerators prevents them from ending up in landfills, reducing environmental harm. Repairing and reselling these appliances not only cuts down on waste but also provides affordable options for others while promoting sustainability and resource conservation.")
    image = Image.open('pages/Images/French Door Fridge.jpg')
    st.image(image, width=400)
    tab1, tab2, tab3, tab4 = st.tabs(["Sell It","Repair It","Scrap It","Ditch it"])
    with tab1:
        data = load_data('SalesData')
        df = data[data.Product == 'Refrigerator']
        df = data[data.Style == 'French Door']
        df = df.reset_index()
        df = df[['Source','Maximum Price','Minimum Price','Average','# of Products']]
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Market Price", df['Average'].mean().astype('int'))
        col2.metric("Units on Market", df['# of Products'].sum())
        col3.metric("Time on Market", "10 Days")
        col1 = st.columns(1)
        st.write(df)
    with tab2:
        df = load_data('RepairCosts')
        df = df[df.Product == 'Refrigerator']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Repair Cost", df['Average Cost'].mean().astype('int'))
        col2.metric("Potential Issues", df.count().mean().astype('str'))
        col3.metric("Estimated Labor", "10 Days")
        col1 = st.columns(1)
        st.write(df)
    with tab3:
        df = load_data('ScrapPrices')
        df = df[df.Product == 'Refrigerator']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Scrap Value", df['Average Value'].mean().astype('int'))
        col2.metric("Min Scrap Value", df['Minimum'].mean().astype('int'))
        col3.metric("Maximum Scrap Value", df['Maximum'].mean().astype('int'))
        col1 = st.columns(1)
        st.write(df)
    with tab4:
        df = load_data('Ditch')
        df = df[df.Product == 'Refrigerator']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Cost", df['AverageCost'].mean().astype('int'))
        col2.metric("# of Vendors", df.count().mean().astype('str'))
        col1 = st.columns(1)
        st.write(df)


        
def Top_drawer():
    st.header("Top Freezer Refrigerator")
    st.markdown("Recycling, repairing, and reselling your refrigerator is a responsible choice that benefits both the environment and your wallet. Recycling old refrigerators prevents them from ending up in landfills, reducing environmental harm. Repairing and reselling these appliances not only cuts down on waste but also provides affordable options for others while promoting sustainability and resource conservation..")
    image = Image.open('pages/Images/Top Loading Fridge.jpg')
    st.image(image, width=400)
    tab1, tab2, tab3, tab4 = st.tabs(["Sell It","Repair It","Scrap It","Ditch it"])
    with tab1:
        data = load_data('SalesData')
        df = data[data.Product == 'Refrigerator']
        df = data[data.Style == 'Top Freezer']
        df = df.reset_index()
        df = df[['Source','Maximum Price','Minimum Price','Average','# of Products']]
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Market Price", df['Average'].mean().astype('int'))
        col2.metric("Units on Market", df['# of Products'].sum())
        col3.metric("Time on Market", "10 Days")
        col1 = st.columns(1)
        st.write(df)
    with tab2:
        df = load_data('RepairCosts')
        df = df[df.Product == 'Refrigerator']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Repair Cost", df['Average Cost'].mean())
        col2.metric("Potential Issues", df.count().mean().astype('str'))
        col3.metric("Estimated Labor", "10 Days")
        col1 = st.columns(1)
        st.write(df)
    with tab3:
        df = load_data('ScrapPrices')
        df = df[df.Product == 'Refrigerator']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Scrap Value", df['Average Value'].mean())
        col2.metric("Min Scrap Value", df['Minimum'].mean())
        col3.metric("Maximum Scrap Value", df['Maximum'].mean())
        col1 = st.columns(1)
        st.write(df)
    with tab4:
        df = load_data('Ditch')
        df = df[df.Product == 'Refrigerator']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Cost", df['AverageCost'].mean())
        col2.metric("# of Vendors", df.count().mean().astype('str'))
        col3.metric("Average Cost", df['Review'].mean())
        col1 = st.columns(1)
        st.write(df)
        
def Bottom_Drawer():
    st.header("Top Freezer Refrigerator")
    st.markdown("Recycling, repairing, and reselling your refrigerator is a responsible choice that benefits both the environment and your wallet. Recycling old refrigerators prevents them from ending up in landfills, reducing environmental harm. Repairing and reselling these appliances not only cuts down on waste but also provides affordable options for others while promoting sustainability and resource conservation.")
    image = Image.open('pages/Images/Bottom Drawer Freezer.jpg')
    st.image(image, width=400)
    tab1, tab2, tab3, tab4 = st.tabs(["Sell It","Repair It","Scrap It","Ditch it"])
    with tab1:
        data = load_data('SalesData')
        df = data[data.Product == 'Refrigerator']
        df = data[data.Style == 'Bottom Freezer']
        df = df.reset_index()
        df = df[['Source','Maximum Price','Minimum Price','Average','# of Products']]
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Market Price", df['Average'].mean().astype('int'))
        col2.metric("Units on Market", df['# of Products'].sum().astype('int'))
        col3.metric("Time on Market", "10 Days")
        col1 = st.columns(1)
        st.write(df)
    with tab2:
        df = load_data('RepairCosts')
        df = df[df.Product == 'Refrigerator']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Repair Cost", df['Average Cost'].mean().astype('int'))
        col2.metric("Potential Issues", df.count().mean().astype('int'))
        col3.metric("Estimated Labor", "10 Days")
        col1 = st.columns(1)
        st.write(df)
    with tab3:
        df = load_data('ScrapPrices')
        df = df[df.Product == 'Refrigerator']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Scrap Value", df['Average Value'].mean().astype('int'))
        col2.metric("Min Scrap Value", df['Minimum'].mean().astype('int'))
        col3.metric("Maximum Scrap Value", df['Maximum'].mean().astype('int'))
        col1 = st.columns(1)
        st.write(df)
    with tab4:
        df = load_data('Ditch')
        df = df[df.Product == 'Refrigerator']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Cost", df['AverageCost'].mean())
        col2.metric("# of Vendors", df.count().mean().astype('int'))
        col3.metric("Average Cost", df['Review'].mean().astype('int'))
        col1 = st.columns(1)
        st.write(df)
        
def Unspecified():
    st.header("Unspecified")
    st.markdown("Recycling, repairing, and reselling your refrigerator is a responsible choice that benefits both the environment and your wallet. Recycling old refrigerators prevents them from ending up in landfills, reducing environmental harm. Repairing and reselling these appliances not only cuts down on waste but also provides affordable options for others while promoting sustainability and resource conservation.")
    image = Image.open('pages/Images/Other Fridges.jpg')
    st.image(image, width=400)
    tab1, tab2, tab3, tab4 = st.tabs(["Sell It","Repair It","Scrap It","Ditch it"])
    with tab1:
        data = load_data('SalesData')
        df = data[data.Product == 'Refrigerator']
        df = data[data.Style == 'Other']
        df = df.reset_index()
        df = df[['Source','Maximum Price','Minimum Price','Average','# of Products']]
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Market Price", df['Average'].mean().astype('int'))
        col2.metric("Units on Market", df['# of Products'].sum())
        col3.metric("Time on Market", "10 Days")
        col1 = st.columns(1)
        st.write(df)
    with tab2:
        df = load_data('RepairCosts')
        df = df[df.Product == 'Refrigerator']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Repair Cost", df['Average Cost'].mean().astype('int'))
        col2.metric("Potential Issues", df.count().mean().astype('int'))
        col3.metric("Estimated Labor", "10 Days")
        col1 = st.columns(1)
        st.write(df)
    with tab3:
        df = load_data('ScrapPrices')
        df = df[df.Product == 'Refrigerator']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Scrap Value", df['Average Value'].mean().astype('int'))
        col2.metric("Min Scrap Value", df['Minimum'].mean().astype('int'))
        col3.metric("Maximum Scrap Value", df['Maximum'].mean().astype('int'))
        col1 = st.columns(1)
        st.write(df)
    with tab4:
        df = load_data('Ditch')
        df = df[df.Product == 'Refrigerator']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Cost", df['AverageCost'].mean().astype('int'))
        col2.metric("# of Vendors", df.count().mean().astype('str'))
        col3.metric("Average Cost", df['Review'].mean().astype('int'))
        col1 = st.columns(1)
        st.write(df)
        
page_names_to_funcs = {

    "French Doors": French_Doors,
    "Top Drawer": Top_drawer,
    "Bottom Drawer" : Bottom_Drawer,
    "Unspecified" : Unspecified,

}

demo_name = st.sidebar.radio("Choose a Product Style", page_names_to_funcs.keys())

st.sidebar.button('Go', on_click=page_names_to_funcs[demo_name]())
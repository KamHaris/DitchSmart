import streamlit as st
import pandas as pd
import numpy as np
import locale
locale.setlocale(locale.LC_ALL,'')
st.set_page_config(layout="wide", page_title="Grills")
from PIL import Image

DATE_COLUMN = 'Date/Time'
def load_data(table):
    data = pd.read_excel('pages/Dataset.xlsx', sheet_name = table)
    return data


def Type1():
    x = st.header("Gas Grill")
    st.markdown("Recycling, repairing, and reselling your grill is a savvy way to embrace sustainability and save money. Recycling old grills helps reduce landfill waste and minimize environmental impact. Repairing and reselling these outdoor cooking appliances extends their useful life, offering affordable options to others while supporting a more eco-conscious lifestyle.")
    image = Image.open('pages/images/Gas Grill Outline.jpg')
    st.image(image, width=400)
    tab1, tab2, tab3, tab4 = st.tabs(["Sell It","Repair It","Scrap It","Ditch it"])
    with tab1:
        data = load_data('SalesData')
        df = data[data.Product == 'Grill']
        df = data[data.Style == 'Gas Grill']
        df = df.reset_index()
        df = df[['Source','Maximum Price','Minimum Price','Average','# of Products']]
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Market Price", locale.currency(df['Average'].mean()))
        col2.metric("Units on Market", df['# of Products'].sum())
        col3.metric("Time on Market", "10 Days")
        col1 = st.columns(1)
        st.write(df)
    with tab2:
        df = load_data('RepairCosts')
        df = df[df.Product == 'Grill']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Repair Cost", locale.currency(df['Average Cost'].mean()))
        col2.metric("Potential Issues", df.count().mean().astype('str'))
        col3.metric("Estimated Labor", "10 Days")
        col1 = st.columns(1)
        st.write(df)
    with tab3:
        df = load_data('ScrapPrices')
        df = df[df.Product == 'Grill']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Scrap Value", locale.currency(df['Average Value'].mean()))
        col2.metric("Min Scrap Value", locale.currency(df['Minimum'].mean()))
        col3.metric("Maximum Scrap Value", locale.currency(df['Maximum'].mean()))
        col1 = st.columns(1)
        st.write(df)
    with tab4:
        df = load_data('Ditch')
        df = df[df.Product == 'Grill']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Cost", locale.currency(df['AverageCost'].mean()))
        col2.metric("# of Vendors", df.count().mean().astype('str'))
        col3.metric("Average Cost", locale.currency(df['Review'].mean()))
        col1 = st.columns(1)
        st.write(df)


        
def Type2():
    st.header("Outdoor Propane Gas Grill")
    st.markdown("Recycling, repairing, and reselling your grill is a savvy way to embrace sustainability and save money. Recycling old grills helps reduce landfill waste and minimize environmental impact. Repairing and reselling these outdoor cooking appliances extends their useful life, offering affordable options to others while supporting a more eco-conscious lifestyle.")
    image = Image.open('pages/Images/Gas Grill Outline.jpg')
    st.image(image, width=400)
    tab1, tab2, tab3, tab4 = st.tabs(["Sell It","Repair It","Scrap It","Ditch it"])
    with tab1:
        data = load_data('SalesData')
        df = data[data.Product == 'Grill']
        df = data[data.Style == 'Outdoor Propane Gas Grill']
        df = df.reset_index()
        df = df[['Source','Maximum Price','Minimum Price','Average','# of Products']]
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Market Price", locale.currency(df['Average'].mean()))
        col2.metric("Units on Market", df['# of Products'].sum())
        col3.metric("Time on Market", "10 Days")
        col1 = st.columns(1)
        st.write(df)
    with tab2:
        df = load_data('RepairCosts')
        df = df[df.Product == 'Grill']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Repair Cost", locale.currency(df['Average Cost'].mean()))
        col2.metric("Potential Issues", df.count().mean().astype('str'))
        col3.metric("Estimated Labor", "10 Days")
        col1 = st.columns(1)
        st.write(df)
    with tab3:
        df = load_data('ScrapPrices')
        df = df[df.Product == 'Grill']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Scrap Value", locale.currency(df['Average Value'].mean()))
        col2.metric("Min Scrap Value", locale.currency(df['Minimum'].mean()))
        col3.metric("Maximum Scrap Value", locale.currency(df['Maximum'].mean()))
        col1 = st.columns(1)
        st.write(df)
    with tab4:
        df = load_data('Ditch')
        df = df[df.Product == 'Grill']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Cost", locale.currency(df['AverageCost'].mean()))
        col2.metric("# of Vendors", df.count().mean().astype('str'))
        col3.metric("Average Cost", locale.currency(df['Review'].mean()))
        col1 = st.columns(1)
        st.write(df)
        


        
page_names_to_funcs = {
    "Gas Grill": Type1,
    "Outdoor Propane Gas Grill": Type2

}

demo_name = st.sidebar.radio("Choose a Product Style", page_names_to_funcs.keys())

st.sidebar.button('Go', on_click=page_names_to_funcs[demo_name]())
import streamlit as st
import pandas as pd
import numpy as np
import locale
from PIL import Image
locale.setlocale(locale.LC_ALL,'')

DATE_COLUMN = 'Date/Time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
def load_data(table):
    data = pd.read_excel('pages/Dataset.xlsx', sheet_name = table)
    return data


def Type1():
    x = st.header("Sectional Couch")
    st.markdown("Recycling, repairing, and reselling your couch is not just an eco-friendly choice; it's a smart one too. By opting to recycle old couches, you divert them from landfills, reducing environmental impact. Repairing and reselling them not only saves money but also extends the life of your furniture, promoting sustainability and reducing the demand for new resources.")
    image = Image.open('pages/Images/Sectional.jpg')
    st.image(image, width=400)
    tab1, tab2, tab3, tab4 = st.tabs(["Sell It","Repair It","Scrap It","Ditch it"])
    with tab1:
        data = load_data('SalesData')
        df = data[data.Product == 'Couch']
        df = data[data.Style == 'Sectional Couch']
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
        df = df[df.Product == 'Couch']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Repair Cost", locale.currency(df['Average Cost'].mean()))
        col2.metric("Potential Issues", df.count().mean().astype('str'))
        col3.metric("Estimated Labor", "10 Days")
        col1 = st.columns(1)
        st.write(df)
    with tab3:
        df = load_data('ScrapPrices')
        df = df[df.Product == 'Couch']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Scrap Value", locale.currency(df['Average Value'].mean()))
        col2.metric("Min Scrap Value", locale.currency(df['Minimum'].mean()))
        col3.metric("Maximum Scrap Value", locale.currency(df['Maximum'].mean()))
        col1 = st.columns(1)
        st.write(df)
    with tab4:
        df = load_data('Ditch')
        df = df[df.Product == 'Couch']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Cost", locale.currency(df['AverageCost'].mean()))
        col2.metric("# of Vendors", df.count().mean().astype('str'))
        col3.metric("Average Cost", locale.currency(df['Review'].mean()))
        col1 = st.columns(1)
        st.write(df)


        
def Type2():
    st.header("Couch and Love Seat")
    st.markdown("Recycling, repairing, and reselling your couch is not just an eco-friendly choice; it's a smart one too. By opting to recycle old couches, you divert them from landfills, reducing environmental impact. Repairing and reselling them not only saves money but also extends the life of your furniture, promoting sustainability and reducing the demand for new resources.")
    image = Image.open('pages/Images/Sofa.jpg')
    st.image(image, width=400)
    tab1, tab2, tab3, tab4 = st.tabs(["Sell It","Repair It","Scrap It","Ditch it"])
    with tab1:
        data = load_data('SalesData')
        df = data[data.Product == 'Couch']
        df = data[data.Style == 'Couch and Love Seat']
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
        df = df[df.Product == 'Couch']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Repair Cost", locale.currency(df['Average Cost'].mean()))
        col2.metric("Potential Issues", df.count().mean().astype('str'))
        col3.metric("Estimated Labor", "10 Days")
        col1 = st.columns(1)
        st.write(df)
    with tab3:
        df = load_data('ScrapPrices')
        df = df[df.Product == 'Couch']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Scrap Value", locale.currency(df['Average Value'].mean()))
        col2.metric("Min Scrap Value", locale.currency(df['Minimum'].mean()))
        col3.metric("Maximum Scrap Value", locale.currency(df['Maximum'].mean()))
        col1 = st.columns(1)
        st.write(df)
    with tab4:
        df = load_data('Ditch')
        df = df[df.Product == 'Couch']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Cost", locale.currency(df['AverageCost'].mean()))
        col2.metric("# of Vendors", df.count().mean().astype('str'))
        col3.metric("Average Cost", locale.currency(df['Review'].mean()))
        col1 = st.columns(1)
        st.write(df)
        
def Type3():
    st.header("Sleeper Couch")
    st.markdown("Recycling, repairing, and reselling your couch is not just an eco-friendly choice; it's a smart one too. By opting to recycle old couches, you divert them from landfills, reducing environmental impact. Repairing and reselling them not only saves money but also extends the life of your furniture, promoting sustainability and reducing the demand for new resources.")
    image = Image.open('pages/Images/Sleeper Couch.jpg')
    st.image(image, width=400)
    tab1, tab2, tab3, tab4 = st.tabs(["Sell It","Repair It","Scrap It","Ditch it"])
    with tab1:
        data = load_data('SalesData')
        df = data[data.Product == 'Couch']
        df = data[data.Style == 'Sleeper Couch']
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
        df = df[df.Product == 'Couch']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Repair Cost", locale.currency(df['Average Cost'].mean()))
        col2.metric("Potential Issues", df.count().mean().astype('str'))
        col3.metric("Estimated Labor", "10 Days")
        col1 = st.columns(1)
        st.write(df)
    with tab3:
        df = load_data('ScrapPrices')
        df = df[df.Product == 'Couch']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Scrap Value", locale.currency(df['Average Value'].mean()))
        col2.metric("Min Scrap Value", locale.currency(df['Minimum'].mean()))
        col3.metric("Maximum Scrap Value", locale.currency(df['Maximum'].mean()))
        col1 = st.columns(1)
        st.write(df)
    with tab4:
        df = load_data('Ditch')
        df = df[df.Product == 'Couch']
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Cost", locale.currency(df['AverageCost'].mean()))
        col2.metric("# of Vendors", df.count().mean().astype('str'))
        col3.metric("Average Cost", locale.currency(df['Review'].mean()))
        col1 = st.columns(1)
        st.write(df)
        

        
page_names_to_funcs = {
    "Sectional Couch": Type1,
    "Couch and Love Seat": Type2,
    "Sleeper Couch" : Type3

}

demo_name = st.sidebar.radio("Choose a Product Style", page_names_to_funcs.keys())

st.sidebar.button('Go', on_click=page_names_to_funcs[demo_name]())
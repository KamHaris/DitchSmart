#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import streamlit.components.v1 as components
st. set_page_config(layout="wide",page_title="App Instructions")

components.html("""
<head>
    <title style="font-family: 'Comic Sans MS';">Welcome to our page</title>
</head>
<body>
    <h1 style="font-family: 'Comic Sans MS';">To use our app, simply select a category from the left.</h1>
    <img src="https://imgur.com/a/4vV44IR" alt="Left Arrow Image" width="80" height="80">
    <p>Once you have selected a category, you will need to choose some details for your product.</p>
    <p>Once the details have been selected, you will be presented with the options available.</p>
    <p>Each option represents a way to "Ditch" your product:</p>
    <ul style="font-family: 'Comic Sans MS';">
        <li>Sell It</li>
        <ul>
            <li>-- this will show you fair market value for your product as well as some market stats</li>
        </ul>
        <li>Repair It</li>
        <ul>
            <li>-- this will show you common repair costs for your product</li>
        </ul>
        <li>Scrap It</li>
        <ul>
            <li>-- this shows you common scrap value for your product</li>
        </ul>
        <li>Ditch It</li>
        <ul>
            <li>-- this will show you common vendors in the area and how much they charge for these items</li>
        </ul>
    </ul>
</body>
""",
 height=600)


# In[ ]:





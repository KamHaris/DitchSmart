#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import time
import numpy as np
import streamlit.components.v1 as components # Import Streamlit
st.set_page_config(layout="wide", page_title="About Us", page_icon="📈")
components.html("""<html><!DOCTYPE html>

<h1 style="color: Green">ABOUT US</h1>
<br>
<p style ="color: white">Welcome to DitchSmart: Your Decision Helper for Used Appliances
<br> <br>
We understand how difficult and confusing it can be to decide what to do with your old appliances.
Do we resell, how can we repair, and can someone just take it off my hands? At DitchSmart, we use
the power of information and data to help everyone make the most informed and cost-effective
decisions .</p>

<br>
<h1 style="color: Green">Who We Are</h1>
<br> <br>
<p style="color: white">We are a dedicated team of data enthusiasts, market analysts, and technology experts on a mission
to simplify the complexities of dealing with ‘ditching’ used appliances. With years of experience in
market research and data analytics, we are curating this platform to provide accurate and reliable
information about the resale value, repair estimates, and recycling options for various appliances.</p>

<br> 

<br>
<h1 style="color: Green">What We Do</h1>
<br> <br>
<p style="color: white">At DitchSmart, we aggregate and analyze vast amounts of data from multiple sources and leverage
our analytical tools to provide you with actionable insights. Whether you are an individual looking to

upgrade, small reseller looking to optimize and price your &#39;scratch and dent&#39; inventory, our insights
and solutions get you the optimal answer and connect you to the right service provider.</p>

<br> 
<br>
<h1 style="color: Green">Why Choose Us</h1>
<br> <br>
<p style="color: white">
<li style="color: white">Know the best price to sell your used appliances</li>
<li style="color: white">Find out how much repairs cost before negotiating with handy professionals</li>
<li style="color: white">Locate local recycling and donation facilities</li>

<br> </body></html>""", width=1000, height = 1400)

import streamlit as st
import pandas as pd
import requests

# page title
# st.title("Flights")
``
# configure page to be full width
st.set_page_config(layout="wide")

# title in markdown
st.markdown("# Flights")

# set sidebar items 
st.sidebar.markdown("# Flights Streamlit App")

# Sidebar items
sidebar_items = ["Dashboard", "Maps"]


for item in sidebar_items:

    # these should be links to pages in the App.
    if item == "Dashboard":
        st.sidebar.header("Dashboard")
        st.sidebar.write("Dashboard")
    elif item == "Maps":
        st.sidebar.header("Maps")
        st.sidebar.write("Maps")

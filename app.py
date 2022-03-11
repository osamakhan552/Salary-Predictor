import streamlit as st
from predict_page import showPredictPage
from explore_page import showGraph


page = st.sidebar.selectbox("Select", ('predict', 'explore'))

if page == "explore":
    showGraph()
else:
    showPredictPage()
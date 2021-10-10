import requests as rq
import streamlit as st
import pandas as pd
import utils.constants as constants

@st.cache()
def fetchRDWData():
    response = rq.get(constants.RDW_API_URL, 
    headers={"X-App-Token": st.secrets['RDW_API_KEY']})
    return pd.read_json(response.json())

@st.cache()
def fetchOCMData():
    response = rq.get(constants.OCM_API_URL, 
    headers={"X-API-Key": st.secrets['OCM_API_KEY']})
    return pd.read_json(response.json())

@st.cache()
def fetchLaadPaalData():
    return pd.read_csv('data/laadpaaldata.csv', delimiter=',', parse_dates=['Started', 'Ended'])
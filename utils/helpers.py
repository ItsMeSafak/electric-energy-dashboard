import requests as rq
import streamlit as st
import pandas as pd

@st.cache()
def fetchRDWData():
    response = rq.get("https://opendata.rdw.nl/resource/w4rt-e856.json", 
    headers={"X-App-Token": st.secrets['RDW_API_KEY']})
    return pd.read_json(response.json())

@st.cache()
def fetchOCMData():
    response = rq.get("https://api.openchargemap.io/v3/poi", 
    headers={"X-API-Key": st.secrets['OCM_API_KEY']})
    return pd.read_json(response.json())

@st.cache()
def fetchLaadPaalData():
    return pd.read_csv('data/laadpaaldata.csv', delimiter=',', parse_dates=['Started', 'Ended'])
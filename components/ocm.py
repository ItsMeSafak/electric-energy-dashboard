import streamlit as st
from utils.helpers import fetchOCMData, show_with_options
import folium
from streamlit_folium import folium_static

df = fetchOCMData(st.secrets['OCM_API_KEY'])
filters = fetchOCMData(st.secrets['OCM_API_KEY'], True)
selectedProvince = "Gelderland"
chargingTypes = []

def map():
    global df
    colors = {True : 'green', False : 'red'}
    central = df.loc[df['AddressInfo.StateOrProvince'] == selectedProvince].iloc[0]
    new_df = df[[set(x).issubset(set(chargingTypes)) for x in df['Connections']]]
    lat, lon = (central['AddressInfo.Latitude'], central['AddressInfo.Longitude'])
    map = folium.Map(location=[lat, lon], zoom_start=10, control_scale=True)
    new_df.apply(lambda row: folium.Marker(location=[row["AddressInfo.Latitude"], row["AddressInfo.Longitude"]], 
                                            icon=folium.Icon(color=colors[row['IsRecentlyVerified']]), popup=row['IsRecentlyVerified'], fill_opacity=1)
                                            .add_to(map), axis=1)
    folium_static(map)

def main():
    st.header("Open Charge Map")
    col1, _, col3 = st.columns([6, 1, 3])
    with col3:
        global selectedProvince
        global chargingTypes
        selectedProvince = st.selectbox(
            "Provincie",
            df['AddressInfo.StateOrProvince'].dropna().unique())
        chargingTypes = st.multiselect(
            "Oplaad type",
            filters, default=filters[1])
        
    with col1:
        show_with_options(map, "Cool map, very pog")
    

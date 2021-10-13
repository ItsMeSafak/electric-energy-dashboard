import pandas as pd
import streamlit as st
from utils.helpers import fetchLaadPaalData, show_with_options
import plotly.express as px
import components.base as gSlider

merk_list = ["All", "Volkswagen", "Opel", "Peugeot", "Renault", "Ford", "Toyota", "Mercedes-Benz", "Citroen", "Tesla"]
MERK_list = [(each_string.upper()+".csv") for each_string in merk_list]
line_dict = dict.fromkeys(merk_list)

for i, file in enumerate(MERK_list):
    with open("data/csv/line/"+file) as csv:
        line_dict[merk_list[i]] = pd.read_csv(csv, index_col="Datum tenaamstelling", parse_dates=["Datum tenaamstelling"])



fuel_list = ["Electriciteit", "Benzine", "Diesel", "LPG", "CNG", "LNG", "Alcohol","Waterstof"]
fuel_file_list = [(each_string +".csv") for each_string in fuel_list]
scatter_dict = dict.fromkeys(fuel_list)

for i, file in enumerate(fuel_file_list):
    with open("data/csv/scatter/"+file) as csv:
        scatter_dict[fuel_list[i]] = pd.read_csv(csv, index_col="Datum tenaamstelling", parse_dates=["Datum tenaamstelling"])



def line():
    st.write("Line")
    df_merk = line_dict[selectedMerk]
    start = gSlider.start_h
    end = gSlider.end_h

    fuel_color_map = {'Benzine' : "brown", 'Diesel': "black", 'LPG' : "orange", 'Elektriciteit': "blue", 'CNG': "yellow", 'Alcohol' : "red",
           'Waterstof' : "aqua", 'LNG' : "green"}

    fig = px.line(df_merk[start:end], y="Kenteken",
              color="Brandstof omschrijving",
              title="Cumulatief nieuwe registraties per brandstoftype",
              color_discrete_map = fuel_color_map)

    fig.update_layout(yaxis_title="Aantal Autos cumulatief", xaxis_title = "Datum")
    st.plotly_chart(fig, use_container_width=True)

def scatter():
    st.write("Scatter")
    df_fuel = scatter_dict[selectedFuel]
    start = gSlider.start_h
    end = gSlider.end_h

    fuel_color_map = {'Benzine' : "brown", 'Diesel': "black", 'LPG' : "orange", 'Elektriciteit': "blue", 'CNG': "yellow", 'Alcohol' : "red",
           'Waterstof' : "aqua", 'LNG' : "green"}


    fig = px.scatter(df_fuel[start:end], y="Brandstof omschrijving", trendline="rolling",
                     trendline_options=dict(window=50),
                     trendline_color_override="red", labels = {"Brandstof omschrijving": selectedFuel })  # color_discrete_map = species_color_map)

    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))
    st.plotly_chart(fig, use_container_width=True)


def main():
    st.header("RDW Data")
    col1, _, col3 = st.columns([6, 1, 3])
    col4, _, col6 = st.columns([6, 1, 3])

    with col3:
        global selectedMerk

        selectedMerk = st.selectbox(
            "Merk", merk_list)

    with col1:
        show_with_options(line, "Cool line, very pog")

    with col6:
        global selectedFuel

        selectedFuel = st.selectbox(
            "Brandstof", fuel_list)

    with col4:
        show_with_options(scatter, "Cool scatter, very pog")


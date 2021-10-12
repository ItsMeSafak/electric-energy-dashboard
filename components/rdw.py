import streamlit as st
import plotly.express as px


def main():
    st.write("Line")
    # df_plot = df_clean.groupby(["Brandstof omschrijving", "Datum tenaamstelling"])["Kenteken"].count().groupby("Brandstof omschrijving").cumsum()
    # df_plot = df_plot.to_frame()
    # df_plot = df_plot.reset_index(level = [0,1]).set_index("Datum tenaamstelling").sort_index()

    # fig = px.line(df_plot["1994":], y="Kenteken", color="Brandstof omschrijving", title="Cumulatief nieuwe registraties per brandstoftype")
    # fig.show()

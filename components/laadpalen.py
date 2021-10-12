import streamlit as st
from utils.helpers import fetchLaadPaalData, show_with_options
import plotly.express as px
import streamlit as st
import plotly.figure_factory as ff

main_df = fetchLaadPaalData("CTime")

def boxplot_chargetime():
    global main_df
    df = main_df.drop(main_df.loc[main_df["ChargeTime"]<0].index)
    fig = px.box(df, x='ChargeTime', title='Boxplot chargetime in uren')
    fig.update_layout(
        xaxis_title="Chargetime in uren",
        yaxis_title="Waarnemingen")
    st.plotly_chart(fig, use_container_width=True)

def boxplot_maxpower():
    global main_df
    fig = px.box(main_df, x='MaxPower', title='Boxplot maxpower')
    fig.update_layout(
        xaxis_title="Maximaal gevraagde vermogen (W)",
        yaxis_title="Waarnemingen")
    st.plotly_chart(fig, use_container_width=True)

def boxplot_totalenergy():
    global main_df
    fig = px.box(main_df, x='TotalEnergy', title='Boxplot TotalEnergy')
    fig.update_layout(
        xaxis_title="Totaal verbruikte energie in Wh",
        yaxis_title="Waarnemingen")
    st.plotly_chart(fig, use_container_width=True)

def histogram_chargetime():
    # Mediaan: 2.5003 en gem: 2.80 --> berekeningen
    # Exclusief de negatieve waarden en de uitschieter van boven de 50 
    global main_df
    df = main_df.drop(main_df.loc[(main_df["ChargeTime"]<0) | (main_df["ChargeTime"]>50)].index)
    group_labels = ['df']
    hist_data= [df["ChargeTime"]]
    fig = ff.create_distplot(hist_data, group_labels)
    fig.add_annotation(x=22, y=0.32,
                text="Gemiddelde: 2.80  |  Mediaan: 2.50",
                showarrow=False,
                yshift=1)
    fig.update_layout(title={"text":'Dichtheidsfunctie van chargetime in uren',
                            'x':0.5},
                    xaxis_title='Chargetime in uren',
                    yaxis_title='Kans')
    st.plotly_chart(fig, use_container_width=True)

def histogram_maxpower():
    global main_df
    fig=px.histogram(data_frame=main_df,
                 x='MaxPower') 
    fig.add_annotation(x=17000, y=2200,
                text="Gemiddelde: 4035.34  |  Mediaan: 3396",
                showarrow=False,
                yshift=1)
    fig.update_layout(title={'text':'Histogram maximaal gevraagde vermogen (W)', 'x':0.5},
                    yaxis_title='Frequentie',
                    xaxis_title='Maximaal gevraagde vermogen (W)')
    st.plotly_chart(fig, use_container_width=True)

def histogram_totalenergy():
    global main_df
    fig=px.histogram(data_frame=main_df,
                 x='TotalEnergy') 
    fig.add_annotation(x=70000, y=850,
                text="Gemiddelde: 10407.46  |  Mediaan: 7713",
                showarrow=False,
                yshift=1)
    fig.update_layout(title={'text':'Histogram totaal verbruikte energie in Wh', 'x':0.5},
                    yaxis_title='Frequentie',
                    xaxis_title='Totaal verbruikte energie in Wh')
    st.plotly_chart(fig, use_container_width=True)

def main():
    st.header("Laadpalen")
    show_with_options(boxplot_chargetime, "Cool boxplot1, very pog")
    show_with_options(boxplot_maxpower, "Cool boxplot2, very pog")
    show_with_options(boxplot_totalenergy, "Cool boxplot3, very pog")

    show_with_options(histogram_chargetime, "Cool histogram1, very pog")
    show_with_options(histogram_maxpower, "Cool histogram2, very pog")
    show_with_options(histogram_totalenergy, "Cool histogram3, very pog")



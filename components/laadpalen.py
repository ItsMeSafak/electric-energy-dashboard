import streamlit as st
from utils.helpers import fetchLaadPaalData, show_with_options
import plotly.express as px
import streamlit as st
import plotly.figure_factory as ff

main_df = fetchLaadPaalData("CTime")

def scatter():
    global main_df
    global x_col
    global y_col
    df = main_df.drop(main_df.loc[main_df["ChargeTime"]<0].index)
    fig = px.scatter(
        df,
        y=y_col,
        x=x_col
    )
    fig.update_layout(
        xaxis_title=x_col,
        yaxis_title=y_col)
    st.plotly_chart(fig, use_container_width=True)

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
    group_labels = ['Chargetime']
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

def histogram_maxpower_nout():
    global main_df
    df33 = main_df["MaxPower"].between(2834, 4050, inclusive = True)
    fig=px.histogram(data_frame=main_df[df33],
                 x='MaxPower') 

    fig.add_annotation(x=3800, y=550,
          text="Gemiddelde: 3415.88  | Mediaan: 3392",
          showarrow=False,
           yshift=1)

    fig.update_layout(title={'text':'Histogram maximaal gevraagde vermogen tussen 2834 en 4050 (W)'},
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

def histogram_totalenergy_nout():
    global main_df
    df44 = main_df["TotalEnergy"].between(1, 19025, inclusive = True)
    fig=px.histogram(data_frame=main_df[df44],
        x='TotalEnergy') 

    fig.add_annotation(x=16000, y=450,
        text="Gemiddelde: 7372.82  |  Mediaan: 7380",
        showarrow=False,
        yshift=1)

    fig.update_layout(title={'text':'Histogram totaal verbruikte energie tussen 1 en 19025 in Wh', 'x':0.5},
        yaxis_title='Frequentie',
        xaxis_title='Totaal verbruikte energie in Wh')

    st.plotly_chart(fig, use_container_width=True)

def main():
    st.header("Laadpalen")
    col1, _, col3 = st.columns([6, 1, 3])
    with col3:
        global x_col
        global y_col
        x_col = st.selectbox(
            "X Waarde",
            main_df.columns)
        y_col = st.selectbox(
            "Y Waarde",
            main_df.columns,
            index=2)
    with col1:
        show_with_options(scatter, "Cool scatter, very pog")

    show_with_options(histogram_chargetime, "Cool histogram1, very pog")
    with st.expander("Boxplot", False):
        show_with_options(boxplot_chargetime, "Cool boxplot1, very pog")

    show_with_options(histogram_maxpower, "Cool histogram2, very pog")
    show_with_options(histogram_maxpower_nout, "Cool histogram2A, very pog")
    with st.expander("Boxplot", False):
        show_with_options(boxplot_maxpower, "Cool boxplot2, very pog")

    show_with_options(histogram_totalenergy, "Cool histogram3, very pog")
    show_with_options(histogram_totalenergy_nout, "Cool histogram3A, very pog")
    with st.expander("Boxplot", False):
        show_with_options(boxplot_totalenergy, "Cool boxplot3, very pog")



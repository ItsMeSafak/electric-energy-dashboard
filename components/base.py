import streamlit as st
from datetime import date

def sidebar():
    # Global variables to check on plots
    global showPlots
    global showCode
    global showBackground

    # Initial page config
    st.set_page_config(
        page_title='Electric energy dashboard',
        layout='wide',
        initial_sidebar_state="expanded"
    )

    st.sidebar.header('Dashboard setings')
    st.sidebar.write('Display settings:')

    # Checkboxes for showing plots/code
    showPlots = st.sidebar.checkbox('Show plots', True)
    showCode = st.sidebar.checkbox('Show code', False)
    showBackground = st.sidebar.checkbox('Achtergrond afbeelding', True)

    st.sidebar.markdown('[README.md](https://github.com/ItsMeSafak/electric-energy-dashboard/blob/master/README.md)')

def set_bg():
    if showBackground:
        st.markdown(
            """
             <style>
            .reportview-container {
               background: url("https://static.vecteezy.com/system/resources/previews/000/697/526/non_2x/virus-pattern-on-a-dark-background-vector.jpg")
            }
            </style>
            """,
            unsafe_allow_html=True
         )

def main():
    sidebar()
    set_bg()

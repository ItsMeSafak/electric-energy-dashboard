import components.laadpalen
import components.ocm
import components.rdw
import components.landingpage
import streamlit as st

select = ""

def main():
    global select
    pages = {
        "Alles": components.landingpage,
        "Laadpalen": components.laadpalen,
        "Open charge map": components.ocm,
        "RDW Data": components.rdw
    }
    st.sidebar.title("Navigatie")
    select = st.sidebar.selectbox(
        "Pagina",
        pages.keys()
    )
    pages[select].main()
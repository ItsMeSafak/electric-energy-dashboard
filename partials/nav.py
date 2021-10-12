import components.laadpalen
import components.ocm
import components.rdw
import streamlit as st


def main():
    pages = {
        "Alles": 0,
        "Laadpalen": components.laadpalen,
        "Open charge map": components.ocm,
        "RDW Data": components.rdw
    }
    st.sidebar.title("Navigatie")
    select = st.sidebar.selectbox(
        "Pagina",
        pages.keys()
    )
    if (pages[select] == 0):
        [pages[p].main() for p in pages if pages[p] != 0]
    else:
        pages[select].main()
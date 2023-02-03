import streamlit as st


tittle1 = "MHI by URGis"
pageicon1 = ":coffee:"
st.set_page_config(page_title=tittle1, page_icon=pageicon1, layout="wide", initial_sidebar_state="auto")

# Customize the sidebar
markdown = """
Read our paper here: <https://github.com/Kleditz/MHI-geo-challenge>

Our GitHub Repository: <https://github.com/Kleditz/MHI-geo-challenge>
"""

st.sidebar.title("Tentang")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/dIBPfvb.png"
st.sidebar.image(logo)

st.title("Pipeline of our projects")

st.markdown(
    """
    The idea is to implement Google Earth Engine API Service from Google Cloud Computing, the result will automaticly generated from
    the python script we developed before.
    """
)
logo2 = "https://i.imgur.com/k0SPP5P.png"
st.image(logo2)
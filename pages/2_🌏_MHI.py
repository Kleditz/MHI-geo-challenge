from src.mhi import Map
# import ee
import streamlit as st
# import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Read our paper here: <https://github.com/Kleditz/MHI-geo-challenge>

Our GitHub Repository: <https://github.com/Kleditz/MHI-geo-challenge>
"""

st.sidebar.title("Tentang")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/dIBPfvb.png"
st.sidebar.image(logo)

st.title("`Mangrove Health Index` - Bali")

st.markdown(
    """
    Aplikasi ini dibuat menggunakan Google Earth Engine API dan data citra **LANDSAT/LC08/C01/T1_SR** yang kemudian di analisis 
    MHI nya agar mantap jiwa jos gandos.
    """
)

Map.to_streamlit(height=500)

st.subheader('Legend')
image1 = "https:i.imgur.com/nqKsEh4.png"
st.image(image1)

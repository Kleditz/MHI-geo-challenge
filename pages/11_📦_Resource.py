import streamlit as st

tittle1 = "MHI by URGis"
logo = "https://i.imgur.com/dIBPfvb.png"
st.set_page_config(page_title=tittle1, page_icon=logo, layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style2.css")

# Customize the sidebar
markdown = """
Our GitHub Repository: <https://github.com/Kleditz/MHI-geo-challenge>
"""

markdown2 = """
Visit our Faculty official website at https://fkp.unud.ac.id/
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo2 = "https://i.imgur.com/mtK4ADo.png"
st.sidebar.image(logo2, use_column_width=True)
# logo_unud = "https://i.imgur.com/NwIZgTX.png"
# st.sidebar.image(logo_unud, width=250)
# st.sidebar.header("Faculty of Marine Affairs and Fisheries")
# st.sidebar.info(markdown2)

st.title("Resources")

st.markdown(
    """
    List of resources we used to accomplish the goal of this projects
    """
)

#Ubah aja jadi perpoint issue yang ada dan jawaban kita gimana terhadap itu
markdown3 = """
*Resources:*
- **LANDSAT/LC08/C01/T1_SR Raster Dataset** : Landsat-8 image courtesy of the U.S. Geological Survey, read more details [here](https://www.usgs.gov/landsat-missions/landsat-8)
- **Vector Data of the Mangrove** : was obtained from Global Mangrove Watch (GMW), you can read more details [here](https://doi.org/10.3390/rs14153657)
- **Vector used for Clipping** : was obtained from Global Administrative Area (GADM), you can read more details [here](https://gadm.org/)
- *MHI Formula* : was created by I Wayan Eka Dharmawan, read more details [here](https://doi.org/10.29244/jitkt.v13i1.34484)
"""

markdown4 = """
*Tools and Frameworks:*
- **Python** : an open-source programming language used to develop scripts in our pipeline.
- **Java Script** : an open-source programming language used to develop scripts at Google Earth Engine on our testing phase.
- **Google Earth Engine** : a useful cloud computing for spatial analysis made by Google for free.
- **GEE-API** : Free Application Programming Interface version of Google Earth Engine, we used in our pipeline and developt the script using Python.
- **Streamlit Framework** : an open-source `Python` Framework we used to deploy our apps.
"""

st.markdown(markdown3)
st.markdown(markdown4)
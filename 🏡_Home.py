# utf-8-coding
# Author: https://github.com/Kleditz

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

st.title("Projects Overview")

st.markdown(
    """
    MHI by URGis Udayana Web-based Application was developed by Udayana University students to help people see the visualization of Mangrove Health Index and the
    area calculation for each of MHI classes that has been classified into:
    - `Very Low` (from 0 to 20),
    - `Low` (from 20 to 40),
    - `Moderate` (from 40 to 60),
    - `High` (from 60 to 80), and
    - `Very High` (from 80 to 100).
    Currently the data that we used in this WebApps is from `January 2020 to December 2020`

    We plan to expand further for all regions of Indonesia, currently the list of available areas can be seen by expanding the sidebar of this website. 
    By doing this, we believe we can help answer the `Blue Carbon` issue that was raised at the G20 International event earlier. 
    This also make things easier for Researchers to be able get the information about Mangrove Health Index without learning about JavaScript to use 
    Google Earth Engine platform or Python Programming Language to perform MHI Calculation.
    """
)

# st.header("Background of this projects")

# #Ubah aja jadi perpoint issue yang ada dan jawaban kita gimana terhadap itu
# markdown = """
# - Blue Carbon was one of ...
# - Mangrove was one of ... plants
# - The application of remote sensing technology make ...
# - Google Earth Engine to help ...
# - The useful automation function of Programing Language help us automaticly ...
# - Google Earth Engine API to help developer ...
# - Web development to get interactive UI/UX for monitoring ...
# """

# st.markdown(markdown)

st.header("How to Operate Our Website")

markdown = """
- User may click `>` button to show the web side-bar, which include MHI Calculation that separated for each Regions.
- User able to read the pipeline of our computation process at `Google Earth Pipeline Pages` on the side-bar.
- To read the resource we used in this project, user may need to select `Resource Pages` on the side-bar.
- User also able to see our Team, at `Our Team Pages` section on the side-bar.
- To see our sourcecode for this web-apps, you can visit our `GitHub Repository` at [here](https://github.com/Kleditz/MHI-geo-challenge).

`Current Version : v1.0.0`
"""

st.markdown(markdown)

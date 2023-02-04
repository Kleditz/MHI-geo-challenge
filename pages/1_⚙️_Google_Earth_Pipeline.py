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

st.title("Pipeline of our projects")

st.markdown(
    """
    The concept is to run Google Earth Engine API Service via Google Cloud Computing, the output will automaticly generated from
    the python script we've developed.
    """
)
logo2 = "https://i.imgur.com/k0SPP5P.png"
st.image(logo2)


st.header("Computation Flow")
st.markdown("""
- `Python` scripts was developed to create automation function to use Google Earth Engine API services, after that the scripts stored in our `GitHub Repository` which will be used later on by `Streamlit` Framework to deploy our Web-apps.
- All the required package or libraries are written down at our `GitHub Repository`, the list of libraries or package needed in Python are contained at `requirements.txt` file.
- Here's the detailed flow of our `Python` scripts:
`Authorize via Google Cloud Computing using .JSON files` > `Get the area of interest from Earth Engine Project's Asset` > `Load Landsat 8 as our Raster Data` > `Data Preprocessing (GEE-API)` > `MHI Calculation` > `Define each MHI Classes from it's value range` > `Show the Map using Layouts` > `Calculate the Areas for each MHI Classes` > `Generate the output as Dataframes and Pie Chart`.
- We do believe this apps will help `User` to easily get the MHI Area or MHI map easily without have to `Code` by themself.
"""
            )
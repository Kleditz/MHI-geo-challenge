from src.mhi import Map
from src.mhi import mask_mhiVlow, mask_mhilow, mask_mhimod, mask_mhihigh, mask_mhiVhigh, maskedmvi, aoi, pd
import pandas as pd
import ee
import plotly.express as px
import streamlit as st

tittle1 = "MHI by URGis"
pageicon1 = ":coffee:"
st.set_page_config(page_title=tittle1, page_icon=pageicon1, layout="wide")

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
    Aplikasi ini dibuat menggunakan Google Earth Engine API dan data citra **LANDSAT/LC08/C01/T1_SR**, selain itu anda juga dapat melihat mask area 
    setiap kelas MHI pada bagian bawah.
    """
)

Map.to_streamlit(height=650)

# Legends
# image1 = "https://i.imgur.com/g1mYBtq.png"
# st.image(image1, width=350)

# CALCULATE AREA
areaImage = maskedmvi.multiply(ee.Image.pixelArea())

stats = areaImage.reduceRegion(
    ee.Reducer.sum(),
    geometry=aoi,scale=30,
    maxPixels=1e9)

value = stats.get('mangrove').getInfo()

areaImage1 = mask_mhiVlow.multiply(ee.Image.pixelArea())

stats1 = areaImage1.reduceRegion(
    ee.Reducer.sum(),
    geometry=aoi,scale=30,
    maxPixels=1e9)

value1 = stats1.get('vlow mangrove').getInfo()

###Value 2###

areaImage2 = mask_mhilow.multiply(ee.Image.pixelArea())

stats2 = areaImage2.reduceRegion(
    ee.Reducer.sum(),
    geometry=aoi,scale=30,
    maxPixels=1e9)

value2 = stats2.get('low mangrove').getInfo()

###Value 2###

areaImage3 = mask_mhimod.multiply(ee.Image.pixelArea())

stats3 = areaImage3.reduceRegion(
    ee.Reducer.sum(),
    geometry=aoi,scale=30,
    maxPixels=1e9)

value3 = stats3.get('mod mangrove').getInfo()

###Value 4###

areaImage4 = mask_mhihigh.multiply(ee.Image.pixelArea())

stats4 = areaImage4.reduceRegion(
    ee.Reducer.sum(),
    geometry=aoi,scale=30,
    maxPixels=1e9)

value4 = stats4.get('high mangrove').getInfo()

###Value 5###

areaImage5 = mask_mhiVhigh.multiply(ee.Image.pixelArea())

stats5 = areaImage5.reduceRegion(
    ee.Reducer.sum(),
    geometry=aoi,scale=30,
    maxPixels=1e9)

value5 = stats5.get('vhigh mangrove').getInfo()

df = round(value1,6),round(value2,6),round(value3,6),round(value4,6),round(value5,6),round(value,6)

# st.write(pd.DataFrame(df, index =['Very Low','Low', 'Moderate', 'High', 'Very High', 'Total Area'],
#             columns=['Area (m\u00b2)']).style.set_caption(
#     "Pixel Representing Mangrove in sqMeter").set_table_styles(
#     [{'selector': 'caption','props':[('font-weight','bold')]}]))


col1, col2 = st.columns(2)

with col1:
    st.header("MHI Area Calculation")
    st.markdown(
    """
    This table contains each `MHI classes` Areas in square meter (m\u00b2)
    """
    )
    st.write(pd.DataFrame(df, index =['Very Low','Low', 'Moderate', 'High', 'Very High', 'Total Area'],
            columns=['Area (m\u00b2)']).style.set_caption(
    "Pixel Representing Mangrove in sqMeter").set_table_styles(
    [{'selector': 'caption','props':[('font-weight','bold')]}]))

with col2:
    st.header("Pie Charts Visualization")

    df = pd.DataFrame({'mangrove': [round(value1,6), round(value2,6), round(value3,6), round(value4,6), round(value5,6), round(value,6)]},
                    index =['Very Low','Low', 'Moderate', 'High', 'Very High', 'Total Area'])

    fig = px.pie(df, values='mangrove', names=df.index, title='Pixel Representing Mangrove in sqMeter')

    st.plotly_chart(fig)

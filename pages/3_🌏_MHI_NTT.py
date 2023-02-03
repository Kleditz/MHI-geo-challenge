# from src.mhi import Map
# from src.mhi import mask_mhiVlow, mask_mhilow, mask_mhimod, mask_mhihigh, mask_mhiVhigh, maskedmvi, pd
import geemap.foliumap as geemap
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

st.sidebar.title("More About us")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/dIBPfvb.png"
st.sidebar.image(logo)

st.title("`Mangrove Health Index` - `NTT`")

st.markdown(
    """
    Aplikasi ini dibuat menggunakan Google Earth Engine API dan data citra **LANDSAT/LC08/C01/T1_SR**, selain itu anda juga dapat melihat luas area 
    setiap kelas MHI pada bagian bawah. Untuk mengetahui threshold dari setiap level MHI, cukup aktifkan layer pada layout Map yang ditampilkan.
    """
)

service_account = "hehehe@hehehe-375811.iam.gserviceaccount.com" # email addres here/ID
credentials = ee.ServiceAccountCredentials(service_account, 'hehehe-375811-d734f3320f7d.json')
ee.Initialize(credentials)

Map = geemap.Map()

# Import aoi vector
aoi = (ee.FeatureCollection('projects/ee-kadekpremaswara/assets/ntt_mw'))

#=================================================================

# Construct start and end dates:
start = ee.Date('2020-01-01')
finish = ee.Date('2020-12-31')

#=================================================================

# Load Landsat 8 surface reflectance data
l8sr = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR') \
            .filterBounds(aoi) \
            .filterDate(start, finish)


def maskL8sr(image):
  cloudShadowBitMask = ee.Number(2).pow(3).int()
  cloudsBitMask = ee.Number(2).pow(5).int()
  qa = image.select('pixel_qa')
  mask = qa.bitwiseAnd(cloudShadowBitMask).eq(0) \
      .And(qa.bitwiseAnd(cloudsBitMask).eq(0))
  return image.updateMask(mask).divide(10000)

composite = l8sr.map(maskL8sr) \
                    .reduce(ee.Reducer.median())

# Masking for pixel above 50 m
srtm = ee.Image('USGS/SRTMGL1_003')
elevation = srtm.select('elevation')
masksrtm = srtm.lt(50)
maskedsrtm = composite.updateMask(masksrtm)

# Water masking
hansenImage = ee.Image('UMD/hansen/global_forest_change_2015')
datamask = hansenImage.select('datamask')
maskland = datamask.eq(1)
maskedcomposite = maskedsrtm.updateMask(maskland)
lcomposite = maskedcomposite.clip(aoi)

mvi = lcomposite.expression(
    '(NIR - GREEN)/(SWIR - GREEN)', {
      'NIR': lcomposite.select('B5_median'),
      'GREEN': lcomposite.select('B3_median'),
      'SWIR': lcomposite.select('B6_median')
}).rename('mvi')

# Tweak these values accordingly
# Lower threshold
lower = 4
# Upper threshold
upper = 20

mviina = mvi.lt(upper).add(mvi.gt(lower))
mask = mviina.eq(2)
maskedmvi = mviina.updateMask(mask).rename('mangrove')

mvimaskedcomposite = lcomposite.updateMask(mask)

#=================================================================

#NBR
nbr = mvimaskedcomposite.expression(
    '((NIR - SWIR) / (NIR + SWIR))', {
      'NIR': mvimaskedcomposite.select('B5_median'),
      'SWIR': mvimaskedcomposite.select('B6_median')
}).rename('NBR')
# GCI
gci = mvimaskedcomposite.expression(
    'NIR / GREEN - 1', {
      'NIR': mvimaskedcomposite.select('B5_median'),
      'GREEN': mvimaskedcomposite.select('B3_median')
}).rename('GCI')
# SIPI
sipi = mvimaskedcomposite.expression(
    '((NIR - BLUE) / (NIR - RED))', {
      'NIR': mvimaskedcomposite.select('B5_median'),
      'RED': mvimaskedcomposite.select('B4_median'),
      'BLUE': mvimaskedcomposite.select('B2_median')
}).rename('SIPI')
# ARVI
arvi = mvimaskedcomposite.expression(
    '((NIR - 2*RED + BLUE) / (NIR + 2*RED + BLUE))', {
      'NIR': mvimaskedcomposite.select('B5_median'),
      'RED': mvimaskedcomposite.select('B4_median'),
      'BLUE': mvimaskedcomposite.select('B2_median')
}).rename('ARVI')

# MHI
mhi = mvimaskedcomposite.expression(
    '102.12*NBR - 4.64*GCI + 178.15*SIPI + 159.53*ARVI - 252.39', {
      'NBR': nbr.select('NBR'),
      'GCI': gci.select('GCI'),
      'SIPI': sipi.select('SIPI'),
      'ARVI': arvi.select('ARVI')
}).rename('MHI')

# Define color pallete for MHI in 4 (four) order class
mhiVis = {
  'min': 0,
  'max': 100,
  'palette': ['000000', 'ff0000', 'ffff00', '00ff00','0070ff']
}

#palette for visualization
palette = '000000' #Black

# Class: Very Low
mhiVlow = mhi.lte(20)
mask_mhiVlow = mhiVlow.updateMask(mhiVlow).rename('vlow mangrove')

# Class: Low
mhilow = mhi.gt(20).And(mhi.lte(40))
mask_mhilow = mhilow.updateMask(mhilow).rename('low mangrove')

# Class: Moderate
mhimod = mhi.gt(40).And(mhi.lte(60))
mask_mhimod = mhimod.updateMask(mhimod).rename('mod mangrove')

# Class: High
mhihigh = mhi.gt(60).And(mhi.lte(80))
mask_mhihigh = mhihigh.updateMask(mhihigh).rename('high mangrove')

# Class: Very High
mhiVhigh = mhi.gt(80)
mask_mhiVhigh = mhiVhigh.updateMask(mhiVhigh).rename('vhigh mangrove')

# Display MHI
Map.centerObject(aoi,16)
Map.addLayer(mhi, mhiVis, 'MHI')
colors = mhiVis['palette']
vmin = mhiVis['min']
vmax = mhiVis['max']
Map.add_colorbar(mhiVis, width=5.0, height=0.4, 
                label="Mangrove Health Index", layer_name="MHI")
Map.addLayer(mask_mhiVlow,{'palette':palette},'Very Low',shown=0)
Map.addLayer(mask_mhilow,{'palette':palette},'Low',shown=0)
Map.addLayer(mask_mhimod,{'palette':palette},'Moderate',shown=0)
Map.addLayer(mask_mhihigh,{'palette':palette},'High',shown=0)
Map.addLayer(mask_mhiVhigh,{'palette':palette},'Very High',shown=0)

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

    fig = px.pie(df, values='mangrove', names=df.index)

    st.plotly_chart(fig)

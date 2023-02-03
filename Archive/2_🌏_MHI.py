import ee
import geemap
import numpy as np
import pandas as pd
# import pygal
import streamlit as st
# import folium as fl

#
# """
# To be able run the python script into streamlit framework, we need to login via service accounts that provided by Google Cloud Computing Service.
# about google cloud computing services:
# user : kadekpremaswara@student.unud.ac.id
# further more, follow our documentation .pptx
# """


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

service_account = "hehehe@hehehe-375811.iam.gserviceaccount.com" # email addres here/ID
credentials = ee.ServiceAccountCredentials(service_account, 'hehehe-375811-d734f3320f7d.json')
ee.Initialize(credentials)

Map = geemap.Map()

# Import aoi vector
aoi = ee.FeatureCollection('projects/ee-kadekpremaswara/assets/b_mw')

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
# Display MHI
Map.addLayer(mhi, mhiVis, 'MHI')
Map.centerObject(aoi,8)

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

Map.addLayer(mask_mhiVhigh,{'palette':palette},'Very High')
Map.to_streamlit()
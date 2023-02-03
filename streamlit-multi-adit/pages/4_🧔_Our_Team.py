import streamlit as st

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

st.title("Meet our team!")

st.markdown(
    """
    In order to accomplish the goals of this project, we're currently Final Year Student at Marine Science Udayana University, Bali.
    """
)

#Ubah aja jadi perpoint issue yang ada dan jawaban kita gimana terhadap itu
markdown = """
Note : Nanti bakal ada foto berlima
1. Mas Aan
2. Tera
3. Ilham
4. Adit dan Manan
"""

st.markdown(markdown)
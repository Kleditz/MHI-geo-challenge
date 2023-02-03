# utf-8-coding
# Author: https://github.com/Kleditz

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

st.title("Tentang Aplikasi Kami")

st.markdown(
    """
    Aplikasi ini kami buat untuk menjawab isu global terkait **`Blue Carbon`**.
    """
)

st.header("Overview Pipeline pada Aplikasi kami:")

#Ubah aja jadi perpoint issue yang ada dan jawaban kita gimana terhadap itu
markdown = """
1. API Google Earth Engine yang digunakan untuk membantu proses komputasi dari data satelit suatu daerah menjadi ...
2. Framework Streamlit yang digunakan untuk deployment project kami dalam bentuk website ...
3. Penggunaan bahasa pemrograman Python yang tergolong open-source dan memiliki banyak community, sehingga digunakan dalam pengembangan aplikasi ini.
4. Mas Aan dan Tera pencinta GIS
5. Ilham yang ngasih ide streamlit
6. Manan yang suka buat paper
7. Adit anak bawang yang ikut aja
"""

st.markdown(markdown)

st.header("Tutorial menggunakan Aplikasi kami:")

markdown = """
1. Untuk memahami overview lebih detail dari project ini, user dapat mengakses [paper official kami disini](https://github.com/Kleditz/MHI-geo-challenge).
2. Untuk memulai silahkan klik `>` untuk menampilkan side-bar aplikasi ini.
3. Untuk membaca Pipeline/Proses pada Google Earth Engine dapat memilih `Google Earth Pipeline` pada side-bar.
4. Untuk menggunakan fitur `MHI` kami, dapat memilih `MHI` pada side-bar.
5. Untuk mengetahui luas area pada setiap kelas `MHI`, dapat memilih `Luas` pada side-bar.
6. Terakhir, untuk melihat halaman manusia tanpa tanda jasa cek `Our Team`.
"""

st.markdown(markdown)

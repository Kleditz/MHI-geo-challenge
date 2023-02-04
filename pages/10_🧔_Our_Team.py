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

st.title("Meet our team!")

st.markdown(
    """
    In order to accomplish the goals of this project, we're currently Final Year Student at Marine Science Udayana University,
    in the frame there is also Dr. Abd. Rahman As-syakur, S.P., M.Si. as our supervisor at URGis Udayana.
    """
)

foto_tim = 'https://i.imgur.com/u7XtVpN.jpg'
st.image(foto_tim)

markdown = """
Inframe :
- `Developer Team` Abdul Manan | [GitHub](https://github.com/abdmanan30) | [LinkedIn](https://www.linkedin.com/in/abdulmanan30)
- `Developer Team` Kadek Aditya Premaswara | [GitHub](https://github.com/kleditz) | [LinkedIn](https://www.linkedin.com/in/kadek-aditya-premaswara)
- `Developer Team` Rinaldy Terra | [GitHub](https://github.com/rtp07) | [LinkedIn](https://www.linkedin.com/in/rinaldyterra-16)
- `Developer Team` Ilham Habibullah | [GitHub](https://github.com/IlhamHabibullah)
- `URGis Supervisor` Abd. Rahman As-syakur | assyakur@unud.ac.id 
"""

st.markdown(markdown)
import streamlit as st

tittle1 = "MHI by URGis"
logo = "https://i.imgur.com/dIBPfvb.png"
st.set_page_config(page_title=tittle1, page_icon=logo, layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

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


st.title("Send Mail")

st.markdown(
    """
    You can also send us a Feedback, or send a Question about our Web-Apps. `Developer Team` will answer your e-mail later on.
    """
)

with st.container():
    st.write("---")
    st.header("Get in Touch with us!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/kadekpremaswara@student.unud.ac.id" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="Sender name" placeholder ="Input your Name here" required>
        <input type="mail" name="Sender e-mail" placeholder ="Input your E-mail here" required>
        <textarea name="Message" placeholder ="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
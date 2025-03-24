import streamlit as st

st.set_page_config(page_title="Mise en place d'un ecosysteme IA", page_icon=":package:")

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "Requester", "Streamlit", "Admin"]


def login():

    st.header("Log in")
    name = st.text_input('Login')
    password = st.text_input('Mot de passe', type='password')
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()


role = st.session_state.role

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("settings.py", title="Settings", icon=":material/settings:")
home = st.Page(
    "home/home.py",
    title="Home",
    icon=":material/help:",
    default=(role == "Requester"),
)

streamlit_pratique_01 = st.Page(
    "streamlit/pratique01.py",
    title="Pratique 01",
    icon=":material/help:",
    default=(role == "Streamlit"),
)

streamlit_pratique_02 = st.Page(
    "streamlit/pratique02.py",
    title="Pratique 02",
    icon=":material/help:",
    default=False,
)

streamlit_pratique_03 = st.Page(
    "streamlit/pratique03.py",
    title="Pratique 03",
    icon=":material/help:",
    default=False,
)


account_pages = [logout_page, settings]
home_pages = [home]
streamlit_pages = [streamlit_pratique_01, streamlit_pratique_02, streamlit_pratique_03]


st.logo("fichiers/images.png")
st.title("Mise en place d'un ecosysteme IA")

page_dict = {}
if st.session_state.role in ["Requester", "Admin"]:
    page_dict["Request"] = home_pages
elif st.session_state.role in ["Streamlit", "Admin"]:
    page_dict["Streamlit"] = streamlit_pages

if len(page_dict) > 0:
    pg = st.navigation({"Menu": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()
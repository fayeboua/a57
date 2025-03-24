import streamlit as st

st.title('Application de recommandation de films')

# Formater du texte
st.write('Bienvenue sur notre application de recommandation de '
'films. Vous pouvez utiliser cette application pour obtenir des'
'recommandations de films en fonction de l\'algorithme de'
'filtrage collaboratif.')

# Utiliser Markdown
st.subheader('Markdown')
st.markdown("""
# This is title
## This header
### subheader -1
#### subheader -2

simple plain text

for *italic* use asterisk
for **bold** format use two asterisk
""")

# Afficher des Messages de Statut
st.subheader("Afficher des Messages de Statut")
st.info("this message display text in blue background")
st.success("this message display text in green background")
st.warning("this message display text in yellow background")
st.error("this message display text in red background")

# Afficher des Images
st.subheader("Display Image")
st.image('./fichiers/mountains.webp', caption='mountains', width=300)

# Afficher des Vidéos
st.subheader('Display Video')
video_file = open('./fichiers/star.mp4',mode='rb').read()
st.video(video_file)

# Optionnel: Barre latérale et formulaire
option = st.sidebar.selectbox('Menu', ['Accueil', 'Recommandation de films'])

st.sidebar.title("Sidebar Title")
with st.sidebar.form(key='my_form'):
    name = st.text_input('Enter your name')
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        st.write(f'Hello {name}')
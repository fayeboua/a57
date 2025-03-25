import streamlit as st

st.title("Pratique 01 - Hello World")

# Afficher du texte simple
st.write("Hello World")

# Formater du texte
st.header("This is Header")
st.subheader("This is subheader")
st.caption('This is caption')
st.text('This is plain text')

# Utiliser Markdown
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
st.success("this message display text in green background")
st.warning("this message display text in yellow background")
st.error("this message display text in red background")

# Afficher des Images
st.subheader("Display Image")
st.image('../fichiers/mountains.webp', caption='mountains', width=300)

# Afficher des Vidéos
st.subheader('Display Video')
video_file = open('../fichiers/star.mp4',mode='rb').read()
st.video(video_file)
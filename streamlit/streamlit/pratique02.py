import streamlit as st

# st.set_page_config(page_title="Layouts", layout='wide')
# st.title('Streamlit Layout')  # display title format
st.title("Pratique 02 - Layouts")

# sidebar
sidebar = st.sidebar
sidebar.write('This is my sidebar')
sidebar.header('Header in sidebar')

# columns
col1, col2, col3 = st.columns(3)
with col1:
    st.write('This is column -1')
    st.image('./fichiers/cat.jpg')
    
with col2:
    st.write('This is column -2')
    st.image('./fichiers/dog.jpg')
    
with col3:
    st.write('This is column -3')
    st.image('./fichiers/owl.jpg')
    
# tabs
st.header('Display in Tabs')
tab1, tab2, tab3 = st.tabs(['Cat', 'Dog', 'Owl'])

with tab1:
    st.write('You are in Cat Tab')
    st.image('./fichiers/cat.jpg')
with tab2:
    st.write('You are in Dog Tab')
    st.image('./fichiers/dog.jpg')
with tab3:
    st.write('You are in Owl Tab')
    st.image('./fichiers/owl.jpg')
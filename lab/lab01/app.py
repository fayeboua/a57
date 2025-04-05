import streamlit as st
import os
import pandas as pd

st.title("Application de visualisation de données")

uploaded_file_sidebar = st.sidebar.file_uploader('Choissisez un fichier CSV', type='csv', key='sidebar')
uploaded_file_main = st.file_uploader('Choissisez un fichier CSV', type='csv', key='main')


uploaded_file = uploaded_file_sidebar if uploaded_file_sidebar is not None else uploaded_file_main


df = None
if uploaded_file is not None:
    st.success('Fichier CSV chargé avec succès')

    with st.expander("Fichier téléchargé"):
        st.write(uploaded_file.name)
        path = os.path.join('./upload', uploaded_file.name)
        with open(path, mode='wb') as f:
            f.write(uploaded_file.getbuffer())

        try:
            if df is None:
                df = pd.read_csv(path)
            else:
                df = pd.concat([df, pd.read_csv(path)], ignore_index=True)
            st.dataframe(df)
        except pd.errors.EmptyDataError:
            st.error("Le fichier CSV est vide ou ne contient pas de colonnes valides.")
        except pd.errors.ParserError:
            st.error("Erreur de parsing du fichier CSV.")
        except Exception as e:
            st.error(f"Une erreur est survenue lors de la lecture du fichier CSV: {e}")


    if df is not None:
        with st.expander("Visualisation des données"):
            try:
                columns = [col for col in df.columns if col.lower() != 'date']
                col = st.selectbox('Choisir une colonne', columns)
                st.line_chart(df[col])
            except KeyError:
                st.error("La colonne sélectionnée n'existe pas dans le fichier CSV.")
            except Exception as e:
                st.error(f"Une erreur est survenue lors de la visualisation des données: {e}")

else:
    st.warning('Veuillez charger un fichier CSV pour commencer.')

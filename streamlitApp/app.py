import streamlit as st
from visualisationsMap import show_maps
from visualisationsGraphs import plot_population, plot_pprst_percentage, plot_sr_nb_category
from data_access import fetch_data
from folium.plugins import MarkerCluster, HeatMap
from data_processing import process_data

def show_homepage():
    st.header("Bienvenue dans l'application")
    st.markdown("Cette application présente des graphiques et des cartes basés sur des données épidémiologiques.")
    st.markdown("Sélectionnez une option dans la barre latérale pour afficher les graphiques ou les cartes.")

def main():
    # Personnalisation de l'apparence
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-color: green;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Titre de l'application
    st.title("********")

    # Sidebar pour la navigation
    st.sidebar.title("Menu")
    page = st.sidebar.selectbox("Sélectionnez une page", ["Accueil", "Graphiques", "Cartes"])

    if page == "Accueil":
        # Afficher la page d'accueil
        show_homepage()

    elif page == "Graphiques":
        # Afficher les graphiques
        st.header("Graphiques")
        data = fetch_data()
        if data is not None:
            plot_pprst_percentage(data)
            plot_sr_nb_category(data)
            plot_population(data)

    elif page == "Cartes":
        # Afficher les cartes
        data = fetch_data()
        show_maps(data)

if __name__ == "__main__":
    main()

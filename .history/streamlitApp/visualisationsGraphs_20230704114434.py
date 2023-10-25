from data_processing import process_data
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go





def plot_pprst_percentage(data):
    # Exemple de visualisation du pourcentage des villages positifs et négatifs à la PPR
    st.subheader('Le pourcentage des villages par statut PPR (Peste des petits ruminants)')
    
    # Calculer le nombre de villages positifs et négatifs
    positive_count = (data['pprst'] == 'positive').sum()
    negative_count = (data['pprst'] == 'negative').sum()
    
    # Calculer les pourcentages
    total_villages = len(data)
    positive_percentage = (positive_count / total_villages) * 100
    negative_percentage = (negative_count / total_villages) * 100
    
    # Créer les labels et les valeurs pour le diagramme circulaire
    labels = ['Positive', 'Negative']
    values = [positive_percentage, negative_percentage]
    
    # Créer la figure du diagramme circulaire
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    
    # Afficher la figure dans Streamlit
    st.plotly_chart(fig)



def plot_sr_nb_category(data):
    st.subheader('Taille des petits ruminants')
    # Définir les intervalles et les labels des catégories
    sr_nb_intervals = [0, 500, 800, float('inf')]
    sr_nb_labels = ['small', 'medium', 'large']

    # Appliquer la catégorisation à la colonne 'sr_nb'
    data['sr_nb_category'] = pd.cut(data['sr_nb'], bins=sr_nb_intervals, labels=sr_nb_labels)

    # Compter le nombre de villages dans chaque catégorie
    sr_nb_category_counts = data['sr_nb_category'].value_counts().reset_index()

    # Renommer les colonnes
    sr_nb_category_counts.columns = ['Category', 'Count']

    # Créer le diagramme à barres
    fig = px.bar(sr_nb_category_counts, x='Category', y='Count', color='Category')

    # Afficher le diagramme à barres
    st.plotly_chart(fig)

def plot_population(data):
    # Exemple de visualisation de la population humaine
    st.subheader('Population Distribution')
    population_counts = data['human_pop'].value_counts()
    st.bar_chart(population_counts)

def main():
    # Récupérer les données traitées
    data = process_data()

    # Afficher les graphiques
    plot_population(data)
    plot_pprst_percentage(data)
    plot_sr_nb_category(data)

if __name__ == '__main__':
    main()

import streamlit as st
import folium
from streamlit_folium import folium_static

from data_processing import process_data

def show_maps(data):
    if data is not None:
        # Créer une carte Folium vide centrée sur la première position
        initial_lat = data['latitude'].iloc[0]
        initial_lon = data['longitude'].iloc[0]
        initial_zoom = 10

       
        # Carte de la PPRST avec légende
       


        

        # Affichage de la légende avec les carrés colorés et le CSS
        st.markdown("""
        <style>
        .legend {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            margin-left: 20px;
        }

        .square {
            width: 15px;
            height: 15px;
            margin-right: 5px;
            display: inline-block;
        }

        .positive {
            background-color: red;
        }

        .negative {
            background-color: green;
        }
        </style>

        **Légende - PPRST Map**
        - Marqueur: Village
        - Couleur:
        <div class='legend'><div class='square negative'></div> Vert (Negative)</div>
        <div class='legend'><div class='square positive'></div> Rouge (Positive)</div>
        """, unsafe_allow_html=True)



        map_pprst = folium.Map(location=[initial_lat, initial_lon], zoom_start=initial_zoom)
        for _, row in data.iterrows():
            pprst_value = row['pprst']
            if pprst_value == 'positive':
                pprst_numeric = 1
                color = 'red'
            elif pprst_value == 'negative':
                pprst_numeric = -1
                color = 'green'
            else:
                pprst_numeric = float(pprst_value)
                color = 'green' if pprst_numeric < 0 else 'red'
            
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=5,
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.7,
                popup=f"Village ID: {row['village_id']}\nPPRST: {pprst_value}",
                tooltip="Cliquez pour plus d'informations"
            ).add_to(map_pprst)

        folium_static(map_pprst)



        # Carte des petits ruminants avec légende
        st.markdown("**Légende - SR_NB Map**")
        st.markdown("- Marqueur: Village")
        st.markdown("- Taille: Proportionnelle au nombre de petits ruminants")

        map_sr_nb = folium.Map(location=[initial_lat, initial_lon], zoom_start=initial_zoom)
        for _, row in data.iterrows():
            sr_nb = row['sr_nb']
            radius = sr_nb / 10  # Ajuster le rayon pour une meilleure visualisation
            folium.Circle(
                location=[row['latitude'], row['longitude']],
                radius=radius,
                color='blue',
                fill=True,
                fill_color='blue',
                fill_opacity=0.7,
                popup=f"Village ID: {row['village_id']}\nSR_NB: {row['sr_nb']}",
                tooltip="Cliquez pour plus d'informations"
            ).add_to(map_sr_nb)

        folium_static(map_sr_nb)

       

    else:
        st.write("Erreur lors du traitement des données.")

# Exemple d'utilisation


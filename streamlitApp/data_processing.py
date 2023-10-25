import pandas as pd
from datetime import datetime
from data_access import fetch_data

def process_data():
    # Récupérer les données depuis la base de données
    data = fetch_data()

    if data is not None:
        # Convertir la colonne 'date_visite' en format date
        #data['date_visite'] = pd.to_datetime(data['date_visite'], format='%Y-%m-%d')

        # Convertir la colonne 'pprst' en valeurs binaires (0 et 1)
        

        # Traiter la colonne 'sr_nb' pour la catégorisation
        sr_nb_intervals = [(0, 100), (101, 500), (501, float('inf'))]
        sr_nb_labels = ['small', 'medium', 'large']
        data['sr_nb_category'] = pd.cut(data['sr_nb'], bins=[interval[0] for interval in sr_nb_intervals] + [float('inf')], labels=sr_nb_labels)
        
        data['pprst'] = data['pprst'].map({'negative': 0, 'positive': 1})
        # Traiter la colonne 'pprst' pour calculer le pourcentage des villages positifs et négatifs
        pprst_counts = data['pprst'].value_counts()
        total_villages = pprst_counts.sum()
        data['pprst_percentage'] = (data['pprst'].map(pprst_counts) / total_villages) * 100
        

        return data
    else:
        return None

import pandas as pd
from database import connect_to_database

def fetch_data():
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT village_id, date_visite, latitude, longitude, human_pop, sr_size, sr_nb, pprst FROM villagesdata"
            cursor.execute(query)
            data = pd.DataFrame(cursor.fetchall(), columns=['village_id', 'date_visite', 'latitude', 'longitude', 'human_pop', 'sr_size', 'sr_nb', 'pprst'])
            cursor.close()
            conn.close()
            return data
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Erreur lors de la récupération des données depuis la base de données : {error}")
            return None
    else:
        return None

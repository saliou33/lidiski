import psycopg2

def connect_to_database():
    conn = None
    try:
        # Paramètres de connexion à la base de données
        params = {
            'host': 'localhost',
            'port': '5432',
            'database': 'lidiski_project',
            'user': 'postgres',
            'password': 'passer'
        }

        # Établir la connexion
        conn = psycopg2.connect(**params)
        print("Connexion à la base de données PostgreSQL réussie")

        # Retourner la connexion
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erreur lors de la connexion à la base de données PostgreSQL: {error}")
        # En cas d'erreur, gérer l'exception selon vos besoins
        # Par exemple, vous pouvez lever une exception personnalisée ou retourner None
        return None

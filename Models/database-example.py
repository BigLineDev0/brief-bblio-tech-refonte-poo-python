import mysql.connector

maconnexion = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)

if maconnexion.is_connected():
    print(f"connexion a la base de donnee {maconnexion.database}")
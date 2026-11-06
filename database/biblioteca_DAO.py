from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteca(self):
        connessione = DBConnect()
        cnx = connessione.get_connection()
        cursore = cnx.cursor(dictionary=True)
        query = """SELECT nome, indirizzo
                   FROM biblioteca
                   ORDER BY nome"""
        cursore.execute(query)
        risultato = cursore.fetchall()
        cursore.close()
        cnx.close()
        return risultato
    # TODO

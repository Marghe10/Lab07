from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_libri(self):
        connessione=DBConnect()
        cnx=connessione.get_connection()
        cursore = cnx.cursor(dictionary=True)
        query="""SELECT * FROM libro"""
        cursore.execute(query)
        risultato = cursore.fetchall()
        cursore.close()
        cnx.close()
        return risultato
    # TODO

    #deve restituirmi una lista coi libri presenti nel database

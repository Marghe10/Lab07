from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        connessione=DBConnect()
        cnx=connessione.get_connection()
        query="""SELECT * FROM Libro"""
        cursore=cnx.cursor()
        cursore.execute(query)
        for libro in cursore:
            print(libro)
        cursore.close()
        cnx.close()
    # TODO

    #deve restituirmi una lista coi libri presenti nel database
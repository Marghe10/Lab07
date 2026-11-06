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
        query = """SELECT * FROM Libro"""
        cursore=cnx.cursor()
        cursore.execute(query)
        for libro in cursore:
            print(libro)
        cursore.close()
        cnx.close()

    # TODO

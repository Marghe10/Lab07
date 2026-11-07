from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self):
        cnx = DBConnect.get_connection()
        try:
            cursore = cnx.cursor(dictionary=True)
            query = """SELECT id, nome, indirizzo
                       FROM biblioteca
                       ORDER BY nome"""
            cursore.execute(query)

            biblioteche=[]
            for row in cursore:
                biblioteca=Biblioteca(id=row['id'], nome=row['nome'], indirizzo=row['indirizzo'])
                #uso la classe biblioteca e la popolo con gli elementi della mia row che posso chiamare
                # [id, nome, cognome] perchè con il dictionary=true ho creato una lista di dizionari con ogni riga
                # corrispondente a un dizionario e ogni dizionario corrispondente a un libro
                biblioteche.append(biblioteca)
            return biblioteche
            cursore.close()
            cnx.close()
        except ConnectionError:
            print("c'è stato un problema con la connessione")

    # TODO

from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_libri(self): # aggiunta io
        cnx = DBConnect.get_connection()
        try:
            cursore = cnx.cursor(dictionary=True)
            query = """SELECT id,titolo,autore,genere,anno_pubblicazione,id_biblioteca FROM libro
                       ORDERD BY id"""
            cursore.execute(query)

            libri = []
            for row in cursore:
                libro = Libro(id=row["id"],titolo=row["titolo"], autore=row["autore"],
                              genere=row["genere"],anno_pubblicazione=row["anno_pubblicazione"],
                              id_biblioteca=row["id_biblioteca"])
                libri.append(libro)
            return libri
            cursore.close()
            cnx.close()
        except ConnectionError:
            print("c'è stato un problema con la connessione")

    def get_generi(self): # aggiunta io
        cnx = DBConnect.get_connection()
        try:
            cursore = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT genere
                       FROM libro 
                       WHERE genere IS NOT NULL
                       ORDER BY genere """
            cursore.execute(query)

            generi = []
            for row in cursore:
                generi.append(row)
            return generi
            cursore.close()
            cnx.close()
        except ConnectionError:
            print("c'è stato un problema con la connessione")

    def get_libri_filtrati(self, biblioteca, genere): # aggiunta io
        cnx = DBConnect.get_connection()

        if cnx is None:
            raise RuntimeError("Impossibile connettersi al database.")

        try:
            print(f"biblioteca: {biblioteca} \n genere: {genere}")
            # print(f"nome biblioteca: {biblioteca["nome"]} \n nome genere: {genere["genere"]}")

            cursor = cnx.cursor(dictionary=True)
            query = """
                    SELECT l.*
                    FROM libro AS l
                    JOIN biblioteca AS b ON l.id_biblioteca = b.id
                    WHERE b.nome = COALESCE(%s, b.nome)
                    AND l.genere = COALESCE(%s, l.genere)
                    ORDER BY l.titolo"""

            cursor.execute(query, (biblioteca, genere))

            libri_filtrati = []

            for row in cursor:
                libro = Libro(
                id=row["id"],
                titolo=row["titolo"],
                autore=row["autore"],
                genere=row["genere"],
                anno_pubblicazione=row["anno_pubblicazione"],
                id_biblioteca=row["id_biblioteca"])
                libri_filtrati.append(libro)

            print(f"Ci sono {len(libri_filtrati)} libri filtrati")
            return libri_filtrati
        finally:
            if cursor is not None:
                cursor.close()
                cnx.close()







        #TODO
    #deve restituirmi una lista coi libri presenti nel database

import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_biblioteche(self, biblioteche):
        # Svuoto le vecchie opzioni, per evitare duplicati.
        dropdown = self._view.biblioteca_dropdown
        dropdown= dropdown.options.clear()

        # Inserisco l'opzione iniziale.
        self._view.biblioteca_dropdown.options.append(ft.dropdown.Option(key="nessun_filtro",text="Nessun filtro"))

        # Inserisco le biblioteche ricevute.
        for nome in biblioteche:
            dropdown.options.append(ft.dropdown.Option(key=nome, text=nome))

        dropdown.value = "nessun_filtro"
        dropdown.update()


        def carica_biblioteche(self):
            biblioteche_complete = self._model.get_biblioteche()
            self.popola_biblioteche(biblioteche_complete)


    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA LIBRI
    # TODO

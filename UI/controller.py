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
    def handler_dropdown(self):
        biblioteche=self._model.get_biblioteche()
        self._view.biblioteca_dropdown.options.clear()
        self._view.biblioteca_dropdown.value = None

        for biblioteca in biblioteche:
            opzione = ft.DropdownOption(
                key=str(biblioteca.id),
                text=f"{biblioteca.nome} - {biblioteca.indirizzo}")

            self._view.biblioteca_dropdown.options.append(opzione)

        self._view.biblioteca_dropdown.update()


    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA LIBRI
    # TODO



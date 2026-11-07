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

    # POPOLA DROPDOWN (TODO)
    def popola_dropdown(self):
        biblioteche = self._model.get_biblioteche()
        for biblioteca in biblioteche:
            self._view.dropdown_biblioteca.options.append(ft.dropdown.Option(biblioteca.nome)) #biblioteca.nome

        generi = self._model.get_generi()
        for genere in generi:
            #print("il genere è: "+str(genere["genere"]))
            genere_stringa = str(genere["genere"])
            self._view.dropdown_genere.options.append(ft.dropdown.Option(genere_stringa))


    # CALLBACKS DROPDOW (TODO)
    def seleziona_biblioteca(self,e):
        scelta = self._view.dropdown_biblioteca.value

        if scelta == "Nessun filtro":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = scelta

    def seleziona_genere(self,e):
        scelta = self._view.dropdown_genere.value

        if scelta == "Nessun filtro":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = scelta


    # AZIONE: MOSTRA LIBRI (TODO)

    def mostra_libri(self, e):
        libri = self._model.get_libri_filtrati(
            self.biblioteca_selezionata,
            self.genere_selezionato)

        self._view.lista_libri.controls.clear()

        if not libri:
            self._view.update()
            self._view.show_alert("Nessun libro trovato con i filtri selezionati.")
            return

        for libro in libri:
            self._view.lista_libri.controls.append(ft.Text(str(libro)))
        self._view.update()
import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        self._view.dd_album.options.clear()
        self._view.lista_visualizzazione_1.controls.clear()

        self._model.popola_grafo(float(self._view.txt_durata.value))
        for nodo in self._model.g.nodes():
            self._view.dd_album.options.append(ft.DropdownOption(key=nodo.id,content=ft.Text(nodo.title)))

        num_nodi = self._model.g.number_of_nodes()
        num_archi = self._model.g.number_of_edges()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Grafo creato, {num_nodi} nodi e {num_archi} archi"))


        self._view.page.update()



    def get_selected_album(self, e):
        """ Handler per gestire la selezione dell'album dal dropdown """""
        self.album_selezionato = self._view.dd_album.value
        print(self.album_selezionato)

    def handle_analisi_comp(self, e):
        """ Handler per gestire l'analisi della componente connessa """""
        self._view.lista_visualizzazione_2.controls.clear()
        self._model.get_comp_connessa(self.album_selezionato)

        dim_comp_connessa = self._model.counter
        durata_comp_connessa = self._model.durata_cc
        self._view.lista_visualizzazione_2.controls.append(
            ft.Text(f"Componente connessa: {dim_comp_connessa} album, {durata_comp_connessa} minuti"))

        self._view.page.update()

    def handle_get_set_album(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del set di album """""
        # TODO
import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO
        grafo=self._model.costruisci_grafo()
        print(grafo)
        minimo,massimo=self._model.get_estremi()
        self._view.lista_visualizzazione_1.clean()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(grafo))
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Peso min: {minimo:.2f}, Peso max: {massimo:.2f}"))
        self._view.page.update()


    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        # TODO
        try:
            soglia = float(self._view.txt_name.value)
        except:
            self._view.show_alert("Inserisci un numero valido per la soglia.")
            return

        min_p, max_p = self._model.get_estremi()
        if soglia < min_p or soglia > max_p:
            self._view.show_alert(f"Soglia fuori range ({min_p:.2f}-{max_p:.2f})")
            return
        minori, maggiori = self._model.count_edges_by_threshold(soglia)
        self._view.lista_visualizzazione_2.controls.clear()
        self._view.lista_visualizzazione_2.controls.append(
            ft.Text(f"Archi < {soglia}: {minori}, Archi > {soglia}: {maggiori}"))
        self._view.page.update()


    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        # TODO
        def handle_cammino_minimo(self, e):
            if not self._model.G:
                self._view.show_alert("Inserisci prima un numero valido per la soglia")
            else:
                soglia = float(self._view.txt_soglia.value)
                percorso_migliore = self._model.calcola_percorso_massimo()  # ritorna una lista
                print(percorso_migliore)
                # for i in percorso_migliore:
                #    print(i)

                self._view.lista_visualizzazione_3.controls.clean()
                if percorso_migliore == []:
                    self._view.lista_visualizzazione_3.controls.append(
                        ft.Text(f'Nessun percorso trovato , inserire una soglia più bassa'))

                else:
                    for i in range(len(percorso_migliore) - 1):
                        u = percorso_migliore[i]
                        v = percorso_migliore[i + 1]

                        if self._model.G.has_edge(u, v):
                            nodo_partenza = self._model.dizionario_rifugi[u]
                            nodo_arrivo = self._model.dizionario_rifugi[v]
                            peso_arco = self._model.G[u][v]['weight']
                            print(nodo_partenza)
                            print(nodo_arrivo)

                            self._view.lista_visualizzazione_3.controls.append(
                                ft.Text(f'{nodo_partenza}   ----->   {nodo_arrivo}'
                                        f':   {peso_arco}'))
            self.page.update()
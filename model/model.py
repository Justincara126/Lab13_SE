import networkx as nx
from copy import deepcopy

from jupyter_server.auth import passwd
from networkx.classes import neighbors

from database.dao import DAO
class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self.dizionario_geni=self.get_geni()
        self.dizionario_localizzazioni=self.get_localizzazioni()
        self.percorso_migliore=[]
        #self.interazioni=self.costruisci_grafo()
    def get_geni(self):
        return DAO.search_all_gene()
    def get_localizzazioni(self):
        return DAO.search_all_localization()
    def costruisci_grafo(self):
        dizionario_connessioni_pesate=DAO.search_connessioni(self.dizionario_geni)
        #ritorna un dizionario in cui la chiave è la coppia di geni e come attributo ha il peso dell'arco
        #print(dizionario_connessioni_pesate)
        for coppia_geni in dizionario_connessioni_pesate:
            #print(coppia_geni,dizionario_connessioni_pesate[coppia_geni])
            nodo1=coppia_geni[0]
            nodo2=coppia_geni[1]
            #print(nodo1,nodo2)
            if dizionario_connessioni_pesate[coppia_geni]==0:
                pass
            else:
                self.G.add_edge(nodo1,nodo2,weight=dizionario_connessioni_pesate[coppia_geni])
        for u,v,peso in self.G.edges(data=True):
            print(u,v,peso)
        return self.G
    def get_estremi(self):
        min=1000000
        max=0
        for u, v, data in self.G.edges(data=True):
            if data["weight"]<min:
                min=data["weight"]
            elif data["weight"]>max:
                max=data["weight"]
        return min,max
    def count_edges_by_threshold(self,soglia):
        minori = 0
        maggiori = 0
        uguali = 0
        for u, v, data in self.G.edges(data=True):
            if data["weight"] < soglia:
                minori += 1
                # posso eliminare qui le connessioni di quelle che non rispettano la soglia, oppure nella ricorsine?...

            elif data["weight"] > soglia:
                maggiori += 1
            else:
                uguali += 1
        # print(minori,maggiori,uguali)
        return minori, maggiori
    def calcola_percorso_massimo(self):

        percorso_migliore = None
        massima_distanza = 0
        nodi = list(self.G.nodes())

        # MODO 1 ALGORITMO DIJKSTRA

        for i in range(len(nodi)):
            for j in range(i + 1, len(nodi)):
                u = nodi[i]
                v = nodi[j]
                print(1)
                try:
                    distanza = nx.dijkstra_path_length(self.G, u, v, weight='weight')
                    percorso_migliore = nx.dijkstra_path(self.G, u, v, weight='weight')

                    if (distanza > massima_distanza or massima_distanza == 0):
                        self.percorso_migliore = percorso_migliore
                        massima_distanza = distanza

                except nx.NetworkXNoPath:
                    continue
        print(self.percorso_migliore)
        return self.percorso_migliore





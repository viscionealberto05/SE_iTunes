import networkx as nx
from networkx import connected_components

from database.dao import DAO

class Model:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.g = nx.Graph()

        self.dizionario_album = {} #key: album_id #value = durata

    def get_tracks(self):
        self.tracks = DAO.get_tracce()

    def get_albums(self):
        self.albums = DAO.get_albums()

    def get_collegamenti(self):
        self.collegamenti = DAO.recupera_archi()

    def load_durate(self):
        for track in self.tracks:
            for album in self.albums:
                if track.album_id == album.id:
                    if album.id not in self.dizionario_album.keys():
                        self.dizionario_album[album.id] = float(track.milliseconds/(1000*60)) #salvo la durata in minuti
                    else:
                        self.dizionario_album[album.id] += float(track.milliseconds /(1000*60))
                    break


    def popola_grafo(self,soglia):

        self.nodes = []
        self.edges = []
        self.dizionario_album = {}

        self.g.clear()
        self.get_tracks()
        self.get_albums()
        self.load_durate()
        self.get_collegamenti()

        print(self.g)

        print(len(self.nodes))
        for album in self.albums:
            if self.dizionario_album[album.id] > float(soglia):
                self.nodes.append(album)

        self.g.add_nodes_from(self.nodes)
        print(f"{len(self.nodes)} nodi")

        #Aggiunta degli archi secondo le playlist
        for tupla in self.collegamenti:

            for album in self.albums:
                if tupla[0] == album.id:
                    nodo1 = album

                elif tupla[1] == album.id:
                    nodo2 = album
                    break


            if nodo1 in self.nodes and nodo2 in self.nodes:
                if (nodo1,nodo2) in self.g.edges.keys():
                    pass
                else:
                    self.g.add_edge(nodo1, nodo2)

        return self.g

    def get_comp_connessa(self, album_id):

        print("MODEL riceve:")
        print(album_id)

        for node in self.g.nodes():
            if int(album_id) == node.id:
                print("trovato")
                album = node
                break


        set_comp_connessa = nx.node_connected_component(self.g,album)

        self.counter = 0
        self.durata_cc = 0.0
        for node in set_comp_connessa:
            self.counter += 1
            self.durata_cc += self.dizionario_album[node.id]


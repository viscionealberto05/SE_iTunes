from model.model import Model
model = Model()
model.get_albums()
model.get_tracks()
model.get_collegamenti()
g = model.popola_grafo(4)
print(g)
from grafo import Grafo
from aestrela import AEstrela

meuGrafo = Grafo()

busca_gulosa = AEstrela(meuGrafo.bucharest)
busca_gulosa.buscar(meuGrafo.arad)

print(busca_gulosa.encontrado)
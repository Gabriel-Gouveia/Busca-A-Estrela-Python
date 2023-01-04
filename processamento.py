from grafo import Grafo
from aestrela import AEstrela

meuGrafo = Grafo()

busca_aestrela = AEstrela(meuGrafo.bucharest)
busca_aestrela.buscar(meuGrafo.arad)

print(busca_aestrela.encontrado)

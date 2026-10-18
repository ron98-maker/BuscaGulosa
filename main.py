from Grafo import Grafo
from Gulosa import Gulosa
from Aestrela import Aestrela
from Largura import Largura

print("BUSCA GULOSA")
gulosa = Gulosa()
gulosa.buscar(Grafo().arad)

print("\nBUSCA A*")
aestrela = Aestrela()
aestrela.buscar(Grafo().arad)

print("\nBUSCA EM LARGURA")
largura = Largura()
largura.buscar(Grafo().arad)
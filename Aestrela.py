from Vertice import Vertice
from Adjacente import Adjacente
class Aestrela:
    def __init__(self):
        self.objetivo = "Bucareste"
        self.status = False
        self.caminho = []
        self.custo_total = 0

    def buscar(self, vertice):

        print(f"Vertice atual: {vertice.rotulo} Distância: {vertice.distancia}")
        vertice.visitado = True
        self.caminho.append(vertice)
        if vertice.rotulo == self.objetivo:
            self.status = True
            print("")
            print(f"Objetivo {self.objetivo} encontrado!")
            print("Caminho percorrido:")
            print(f"Custo total: {self.custo_total}")
            for v in self.caminho:
                print(f"Vértice: {v.rotulo}")
            return True
        else:
            vetor_adjacentes = []
            for adj in vertice.adjacentes:
                if adj.vertice.visitado == False:
                    vetor_adjacentes.append(adj)

            vetor_adjacentes.sort(key=lambda x: x.custo + x.vertice.distancia)
            

            #print("Adjacentes ordenados por distância:")
            #vertice.exibir_adjacentes()

            
            if len(vetor_adjacentes) > 0:
                self.custo_total += vetor_adjacentes[0].custo
                self.buscar(vetor_adjacentes[0].vertice)


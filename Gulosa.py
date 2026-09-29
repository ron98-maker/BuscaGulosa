from Vertice import Vertice
from Adjacente import Adjacente
class Gulosa:
    def __init__(self):
        self.objetivo = "Bucareste"
        self.status = False

    def buscar(self, vertice):

        print(f"Vertice atual: {vertice.rotulo} Distância: {vertice.distancia}")
        vertice.visitado = True
        if vertice.rotulo == self.objetivo:
            self.status = True
            print("")
            print(f"Objetivo {self.objetivo} encontrado!")
            return True
        else:
            vetor_adjacentes = []
            for adj in vertice.adjacentes:
                if adj.vertice.visitado == False:
                    adj.vertice.visitado = True
                    vetor_adjacentes.append(adj.vertice)

            vetor_adjacentes.sort(key=lambda x: x.distancia)
            
            print("")
            print("")
            print("Adjacentes ordenados por distância:")
            for adj in vetor_adjacentes:
                print(f"Vértice: {adj.rotulo} Distância: {adj.distancia}")

            print("")
            print("")
            
            if len(vetor_adjacentes) > 0:
                self.buscar(vetor_adjacentes[0])

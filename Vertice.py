
class Vertice:
    def __init__(self, rotulo, distancia):
        self.rotulo = rotulo
        self.distancia = distancia
        self.visitado = False
        self.adjacentes = []

    @property
    def rotulo(self):
        return self._rotulo

    @rotulo.setter
    def rotulo(self, valor):
        self._rotulo = valor

    @property
    def distancia(self):
        return self._distancia

    @distancia.setter
    def distancia(self, valor):
        self._distancia = valor

    @property
    def visitado(self):
        return self._visitado

    @visitado.setter
    def visitado(self, valor):
        self._visitado = valor

    @property
    def adjacentes(self):   
        return self._adjacentes

    @adjacentes.setter
    def adjacentes(self, valor):
        self._adjacentes = valor

    def adicionar_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def exibir_adjacentes(self):
        if not self.adjacentes:
            print(f"O vértice {self.rotulo} não possui adjacentes")
        else:
            print(f"Adjacentes do vértice {self.rotulo}")
            for adjacente in self.adjacentes:
                print(f"Vértice: {adjacente.vertice.rotulo} Distância: {adjacente.vertice.distancia}")

    

    
    
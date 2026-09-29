
class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo

    @property
    def vertice(self):
        return self._vertice

    @vertice.setter
    def vertice(self, valor):
        self._vertice = valor

    @property
    def custo(self):
        return self._custo

    @custo.setter
    def custo(self, valor):
        self._custo = valor
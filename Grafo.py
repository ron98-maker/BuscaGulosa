from Vertice import Vertice
from Adjacente import Adjacente
class Grafo:
    def __init__(self):
        self.arad = Vertice("Arad", 366)
        self.bucareste = Vertice("Bucareste", 0)
        self.craiova = Vertice("Craiova", 160)
        self.dobreta = Vertice("Dobreta", 242)
        self.eforie = Vertice("Eforie", 161)
        self.fagaras = Vertice("Fagaras", 178)
        self.giurgiu = Vertice("Giurgiu", 77)
        self.hirsova = Vertice("Hirsova", 151)
        self.iasi = Vertice("Iasi", 226)
        self.lugoj = Vertice("Lugoj", 244)
        self.mehadia = Vertice("Mehadia", 241)
        self.neamt = Vertice("Neamt", 234)
        self.oradea = Vertice("Oradea", 380)
        self.pitesti = Vertice("Pitesti", 98)
        self.rimnicu = Vertice("Rimnicu Vilcea", 193)
        self.sibiu = Vertice("Sibiu", 253)
        self.timisoara = Vertice("Timisoara", 329)
        self.urziceni = Vertice("Urziceni", 80)
        self.vaslui = Vertice("Vaslui", 199)
        self.zerind = Vertice("Zerind", 374)

        self.arad.adicionar_adjacente(Adjacente(self.zerind, 75))
        self.arad.adicionar_adjacente(Adjacente(self.sibiu, 140))
        self.arad.adicionar_adjacente(Adjacente(self.timisoara, 118))

        self.zerind.adicionar_adjacente(Adjacente(self.arad, 75))
        self.zerind.adicionar_adjacente(Adjacente(self.oradea, 71))

        self.oradea.adicionar_adjacente(Adjacente(self.zerind, 71))
        self.oradea.adicionar_adjacente(Adjacente(self.sibiu, 151))

        self.sibiu.adicionar_adjacente(Adjacente(self.oradea, 151))
        self.sibiu.adicionar_adjacente(Adjacente(self.arad, 140))
        self.sibiu.adicionar_adjacente(Adjacente(self.fagaras, 99))
        self.sibiu.adicionar_adjacente(Adjacente(self.rimnicu, 80))

        self.fagaras.adicionar_adjacente(Adjacente(self.sibiu, 99))
        self.fagaras.adicionar_adjacente(Adjacente(self.bucareste, 211))

        self.rimnicu.adicionar_adjacente(Adjacente(self.sibiu, 80))
        self.rimnicu.adicionar_adjacente(Adjacente(self.pitesti, 97))
        self.rimnicu.adicionar_adjacente(Adjacente(self.craiova, 146))

        self.pitesti.adicionar_adjacente(Adjacente(self.rimnicu, 97))
        self.pitesti.adicionar_adjacente(Adjacente(self.craiova, 138))
        self.pitesti.adicionar_adjacente(Adjacente(self.bucareste, 101))

        self.craiova.adicionar_adjacente(Adjacente(self.dobreta, 120))
        self.craiova.adicionar_adjacente(Adjacente(self.rimnicu, 146))
        self.craiova.adicionar_adjacente(Adjacente(self.pitesti, 138))

        self.dobreta.adicionar_adjacente(Adjacente(self.craiova, 120))
        self.dobreta.adicionar_adjacente(Adjacente(self.mehadia, 75))

        self.mehadia.adicionar_adjacente(Adjacente(self.dobreta, 75))
        self.mehadia.adicionar_adjacente(Adjacente(self.lugoj, 70))

        self.lugoj.adicionar_adjacente(Adjacente(self.mehadia, 70))
        self.lugoj.adicionar_adjacente(Adjacente(self.timisoara, 111))

        self.timisoara.adicionar_adjacente(Adjacente(self.lugoj, 111))
        self.timisoara.adicionar_adjacente(Adjacente(self.arad, 118))

        self.bucareste.adicionar_adjacente(Adjacente(self.fagaras, 211))
        self.bucareste.adicionar_adjacente(Adjacente(self.pitesti, 101))
        self.bucareste.adicionar_adjacente(Adjacente(self.giurgiu, 90))
        self.bucareste.adicionar_adjacente(Adjacente(self.urziceni, 85))

        self.giurgiu.adicionar_adjacente(Adjacente(self.bucareste, 90))

        self.urziceni.adicionar_adjacente(Adjacente(self.bucareste, 85))
        self.urziceni.adicionar_adjacente(Adjacente(self.hirsova, 98))
        self.urziceni.adicionar_adjacente(Adjacente(self.vaslui, 142))

        self.hirsova.adicionar_adjacente(Adjacente(self.urziceni, 98))
        self.hirsova.adicionar_adjacente(Adjacente(self.eforie, 86))

        self.eforie.adicionar_adjacente(Adjacente(self.hirsova, 86))

        self.vaslui.adicionar_adjacente(Adjacente(self.urziceni, 142))
        self.vaslui.adicionar_adjacente(Adjacente(self.iasi, 92))

        self.iasi.adicionar_adjacente(Adjacente(self.vaslui, 92))
        self.iasi.adicionar_adjacente(Adjacente(self.neamt, 87))

        self.neamt.adicionar_adjacente(Adjacente(self.iasi, 87))
        

        
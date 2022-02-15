from Unico import Unico
from Doble import Doble

class InventarioCursos:
    def __init__(self):
        self.lista = []

    def getLista(self):
        return self.lista

    def agregarCurso(self,*args):
        if len(args)==6:
            curso = Unico(*args)
        elif len(args)==9:
            curso = Doble(*args)
        self.lista.append(curso)

    def eliminarCurso(self,indice):
        self.lista.pop(indice)

    def toString(self):
        for i in self.lista:
            i.toString()

    def extraerCodigos(self):
        codigos = dict()
        lista = self.getLista()
        for curso in lista:
            key = curso.getCodigo()
            if codigos.get(key):
                codigos[key]+=1
            else:
                codigos[key] = 1
        return codigos.keys()
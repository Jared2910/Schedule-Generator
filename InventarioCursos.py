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

                



if __name__ == '__main__':
    inventario = InventarioCursos()

    inventario.agregarCurso("Programacion 4","41737","EIF209","Lunes","10:00","11:40","Jueves","10:00","11:40")
    inventario.agregarCurso("Ingenieria en sistemas 1","41744","EIF210","Martes","13:00","16:40")
    inventario.agregarCurso("Bases de datos","41752","EIF211","Lunes","15:00","16:40","Jueves","15:00","16:40")
    inventario.agregarCurso("Ingles 4","41095","LIX400","Miercoles","13:00","16:40","Viernes","13:00","16:00")

    inventario.toString()



        
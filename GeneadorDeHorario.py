from InventarioCursos import InventarioCursos
import itertools


class GeneradorDeHorario:
    def __init__(self,inventario):
        self.inventario = inventario

    def getInventario(self):
        return self.inventario

    def generarLista(self):
        lista = []
        inventario = self.getInventario()
        inventario = inventario.getLista()

        for i in inventario:
            lista.append((i, i.getCodigo()))
        return lista

    def buscarRepetidos(self,cursos, lista):
        for curso in cursos:
            contador = 0
            for i in lista:
                contador += i[1].count(curso)
            if contador > 1:
                return False
        return True

    def BuscarCombinaciones(self):
        inventario = self.getInventario()
        lista = self.generarLista()
        codigos = inventario.extraerCodigos()
        combinaciones = list(itertools.combinations(lista, len(codigos)))
        resultado = []

        for i in combinaciones:
            if self.buscarRepetidos(codigos, i):
                resultado.append(list(i))

        return resultado

if __name__ == "__main__":
    inventario = InventarioCursos()
    inventario.agregarCurso("Programacion 4","41737","EIF209","Lunes","10:00","11:40","Jueves","10:00","11:40")
    inventario.agregarCurso("Programacion 4","41736","EIF209","Lunes","8:00","9:40","Jueves","8:00","9:40")

    inventario.agregarCurso("Ingenieria en sistemas 1","41744","EIF210","Martes","13:00","16:40")
    inventario.agregarCurso("Ingenieria en sistemas 1","41742","EIF210","Martes","8:00","11:40")

    inventario.agregarCurso("Bases de datos","41752","EIF211","Lunes","15:00","16:40","Jueves","15:00","16:40")

    inventario.agregarCurso("Ingles 4","41095","LIX400","Miercoles","13:00","16:40","Viernes","13:00","16:00")

    inventario.agregarCurso("Metodos de investigacion","41787","EIF413","Martes","6:00","7:40","Viernes","6:00","7:40")



    generador = GeneradorDeHorario(inventario)
    
    result = generador.BuscarCombinaciones()
    print(result)
        


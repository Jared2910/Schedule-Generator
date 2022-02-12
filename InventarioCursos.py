from Curso import Curso

class InventarioCursos:
    def __init__(self):
        self.lista = []

    def agregarCurso(self,*args):
        self.lista.append(Curso(*args))

    def eliminarCurso(self,indice):
        self.lista.pop(indice)

    def toString(self):
        for i in range(len(self.lista)):
            self.lista[i].toString()



if __name__ == '__main__':
    prueba = InventarioCursos()

    prueba.agregarCurso("Programacion 4","41737","EIF209","Lunes","10:00","11:40","Jueves","10:00","11:40")
    prueba.agregarCurso("Ingenieria en sistemas 1","41744","EIF210","Martes","13:00","16:40")
    prueba.agregarCurso("Bases de datos","41752","EIF211","Lunes","15:00","16:40","Jueves","15:00","16:40")
    prueba.agregarCurso("Ingles 4","41095","LIX400","Miercoles","13:00","16:40","Viernes","13:00","16:00")

    prueba.toString()



        
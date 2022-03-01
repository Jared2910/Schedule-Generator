import datetime
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

    def simplificar(self,horarios):
        lista = []
        for i in horarios:
            temp = []
            for j in i:
                temp.append(j[0])
            lista.append(temp)
        return lista

    def buscarChoqueDeHorario(self,horario,lista):
        margen = datetime.timedelta(minutes=20)
        for i in lista:
            if not(i[0]<horario[0] and i[1]<horario[0] or i[0]-horario[1]>= margen):
                return False
        return True
        


    def verificarHora(self,cursos):
        verified = {'Lunes':[],'Martes':[],'Miercoles':[],'Jueves':[],'Viernes':[],'Sabado':[],'Domingo':[]}
        for curso in cursos:
            horario = curso.getHorario()
            for key in horario:
                if verified[key] == []:
                    verified[key].append(horario[key])
                elif self.buscarChoqueDeHorario(horario[key],verified[key]):
                    verified[key].append(horario[key])
                else:
                    return False
        return True
                    
        
    def filtrarHorario(self,listaHorarios):
        lista = []
        for i in listaHorarios:
            if self.verificarHora(i):
                lista.append(i)
        return lista

    def imprimirHorarios(self,horarios):
        num = 1
        for i in horarios:
            print(f'Horario || {num} ||\n')
            for j in i:
                j.toString()
            print('---------------------------------------------------------')
            num+=1
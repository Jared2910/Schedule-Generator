import datetime
from FormatoHoras import separadorHoraMinuto


class Curso:
    nombre = ""
    nrc = ""
    codigo = ""
    horario = dict()

    def __init__(self,nombre,nrc,codigo,dia1,entrada1,salida1,dia2,entrada2,salida2):
        self.nombre = nombre
        self.nrc = nrc
        self.codigo = codigo

        horaE1,minutoE1 = separadorHoraMinuto(entrada1)
        horaS1,minutoS1 = separadorHoraMinuto(salida1)

        horaE2,minutoE2 = separadorHoraMinuto(entrada2)
        horaS2,minutoS2 = separadorHoraMinuto(salida2)

        self.horario[dia1]=(datetime.timedelta(hours=horaE1,minutes=minutoE1),datetime.timedelta(hours=horaS1,minutes=minutoS1))
        self.horario[dia2]=(datetime.timedelta(hours=horaE2,minutes=minutoE2),datetime.timedelta(hours=horaS2,minutes=minutoS2))

    def getNombre(self):
        return self.nombre
    def getNrc(self):
        return self.nrc
    def getCodigo(self):
        return self.codigo
    def getHorario(self):
        return self.horario

    def mostrarHorario(self):
        dictionario = self.getHorario()
        for key in dictionario:
            print(key,':',dictionario[key][0],'-',dictionario[key][1])
    
    def toString(self):
        print(f"Curso: {self.getNombre()}")
        print(f"NRC: {self.getNrc()}")
        print(f"Codigo: {self.getCodigo()}")
        print(f"---Hora del curso---")
        self.mostrarHorario()
        print()
    

curso1 = Curso("Programacion 4","41741","EIF209","Lunes","8:00","9:40","Jueves","8:00","9:00")

curso1.toString()

        
from Curso import Curso
import datetime
from FormatoHoras import separadorHoraMinuto


class Unico(Curso):
    
    def __init__(self, nombre, nrc, codigo, dia, entrada, salida):
        self.nombre = nombre
        self.nrc = nrc
        self.codigo = codigo

        horaE1, minutoE1 = separadorHoraMinuto(entrada)
        horaS1, minutoS1 = separadorHoraMinuto(salida)

        self.horario = dict()
        self.horario[dia] = (datetime.timedelta(
            hours=horaE1, minutes=minutoE1), datetime.timedelta(hours=horaS1, minutes=minutoS1))

    

    def mostrarHorario(self):
        super().mostrarHorario()

    def toString(self):
        super().toString()


	

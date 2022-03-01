from Curso import Curso
from FormatoHoras import separadorHoraMinuto
import datetime


class Doble(Curso):
    def __init__(self, nombre, nrc, codigo,profesor, dia_1, entrada_1, salida_1, dia_2, entrada_2, salida_2):
        self.nombre = nombre
        self.nrc = nrc
        self.codigo = codigo
        self.profesor = profesor

        horaE1, minutoE1 = separadorHoraMinuto(entrada_1)
        horaS1, minutoS1 = separadorHoraMinuto(salida_1)
        horaE2, minutoE2 = separadorHoraMinuto(entrada_2)
        horaS2, minutoS2 = separadorHoraMinuto(salida_2)

        self.horario = dict()
        self.horario[dia_1] = (datetime.timedelta(
            hours=horaE1, minutes=minutoE1), datetime.timedelta(hours=horaS1, minutes=minutoS1))
        self.horario[dia_2] = (datetime.timedelta(
            hours=horaE2, minutes=minutoE2), datetime.timedelta(hours=horaS2, minutes=minutoS2))

    def mostrarHorario(self):
        super().mostrarHorario()

    def toString(self):
        super().toString()

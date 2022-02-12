from Curso import Curso
from FormatoHoras import separadorHoraMinuto
import datetime


class Doble(Curso):
    horario = dict()

    def __init__(self, nombre, nrc, codigo, dia_1, entrada_1, salida_1, dia_2, entrada_2, salida_2):
        self.nombre = nombre
        self.nrc = nrc
        self.codigo = codigo

        horaE1, minutoE1 = separadorHoraMinuto(entrada_1)
        horaS1, minutoS1 = separadorHoraMinuto(salida_1)

        horaE2, minutoE2 = separadorHoraMinuto(entrada_2)
        horaS2, minutoS2 = separadorHoraMinuto(salida_2)

        self.horario[dia_1] = (datetime.timedelta(
            hours=horaE1, minutes=minutoE1), datetime.timedelta(hours=horaS1, minutes=minutoS1))

        self.horario[dia_2] = (datetime.timedelta(
            hours=horaE2, minutes=minutoE2), datetime.timedelta(hours=horaS2, minutes=minutoS2))

    def getNombre(self):
        return self.nombre
    def getNrc(self):
        return self.nrc
    def getCodigo(self):
        return self.codigo
    def getHorario(self):
        return self.horario

    def mostrarHorario(self):
        super().mostrarHorario()

    def toString(self):
        super().toString()
    
if __name__ == "__main__":
    a = Doble("Ingenieria en sistemas 1", "41744","EIF210", "Martes", "13:00", "16:40","Viernes","8:00","9:40")
    a.toString()

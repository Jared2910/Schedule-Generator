from Curso import Curso
import datetime
from FormatoHoras import separadorHoraMinuto


class Unico(Curso):
    horario = dict()
    def __init__(self, nombre, nrc, codigo, dia, entrada, salida):
        self.nombre = nombre
        self.nrc = nrc
        self.codigo = codigo

        horaE1, minutoE1 = separadorHoraMinuto(entrada)
        horaS1, minutoS1 = separadorHoraMinuto(salida)

        self.horario[dia] = (datetime.timedelta(
            hours=horaE1, minutes=minutoE1), datetime.timedelta(hours=horaS1, minutes=minutoS1))

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
    a = Unico("Ingenieria en sistemas 1", "41744","EIF210", "Martes", "13:00", "16:40")
    a.toString()



	

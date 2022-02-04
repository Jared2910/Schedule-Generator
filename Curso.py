import string


class Curso:
    nombre = ""
    nrc = ""
    escuela = ""
    numeroDeCurso = ""
    horario = {"dia0":"00:00 AM - 00:00 AM","dia1":"00:00 AM - 00:00 AM"}

    def __init__(self,nombre,nrc,escuela,numeroDeCurso,horario):
        self.nombre = nombre
        self.nrc = nrc
        self.escuela = escuela
        self.numeroDeCurso = numeroDeCurso
        self.horario = horario

    def getNombre(self):
        return self.nombre
    def getNrc(self):
        return self.nrc
    def getEscuela(self):
        return self.escuela
    def getNumeroDeCurso(self):
        return self.numeroDeCurso
    def getHorario(self):
        return self.horario
    
curso1 = Curso("Programacion 4","41741","EIF","209",dict(Lunes="8:00 AM - 9:40 AM",Jueves="8:00 AM - 9:40 AM"))

h = curso1.getHorario()

print(h["Lunes"])

        
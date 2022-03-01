from abc import ABC,abstractmethod

class Curso(ABC):

    @abstractmethod
    def __init__(self, nombre, nrc, codigo,profesor):
        self.nombre = nombre
        self.nrc = nrc
        self.codigo = codigo
        self.profesor = profesor


    @abstractmethod
    def toString(self):
        print(f"Curso: {self.getNombre()}")
        print(f"NRC: {self.getNrc()}")
        print(f"Codigo: {self.getCodigo()}")
        print(f"Profesor(a): {self.getProfesor()}")
        print(f"---Hora del curso---")
        self.mostrarHorario()

    @abstractmethod
    def mostrarHorario(self):
        horario = self.getHorario()
        for key in horario:
            print(key,':', horario[key][0], '-', horario[key][1])

    def mostrarHorario_String(self):
        string = ''
        horario = self.getHorario()
        for key in horario:
            string += (key+': '+str(horario[key][0])+' - '+str(horario[key][1])+'\n')
        return string


    def getNombre(self):
        return self.nombre
    def getNrc(self):
        return self.nrc
    def getCodigo(self):
        return self.codigo
    def getProfesor(self):
        return self.profesor
    def getHorario(self):
        return self.horario

        
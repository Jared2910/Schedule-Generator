from abc import ABC,abstractmethod

class Curso(ABC):
    @abstractmethod
    def toString(self):
        print(f"Curso: {self.getNombre()}")
        print(f"NRC: {self.getNrc()}")
        print(f"Codigo: {self.getCodigo()}")
        print(f"---Hora del curso---")
        self.mostrarHorario()

    @abstractmethod
    def mostrarHorario(self):
        horario = self.getHorario()
        for key in horario:
            print(key, ':', horario[key][0], '-', horario[key][1])

        
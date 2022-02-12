from abc import ABC,abstractmethod


class Curso(ABC):
    @abstractmethod
    def toString(self):
        pass

    @abstractmethod
    def __mostrarHorario(self):
        pass

    def __CursoDeDosDias(self,*args):
        self.nombre = args[0]
        self.nrc = args[1]
        self.codigo = args[2]

        horaE1,minutoE1 = separadorHoraMinuto(args[4])
        horaS1,minutoS1 = separadorHoraMinuto(args[5])

        horaE2,minutoE2 = separadorHoraMinuto(args[7])
        horaS2,minutoS2 = separadorHoraMinuto(args[8])

        self.horario[args[3]]=(datetime.timedelta(hours=horaE1,minutes=minutoE1),datetime.timedelta(hours=horaS1,minutes=minutoS1))
        self.horario[args[6]]=(datetime.timedelta(hours=horaE2,minutes=minutoE2),datetime.timedelta(hours=horaS2,minutes=minutoS2))

        
from Empleados import Empleado
class EContratado(Empleado):
    __fecha_inicio:str
    __fecha_fin:str
    __cant_horas:int
    # Variable de Clase:
    __valor_x_hora = 10000

    def __init__(self, dni, nombre, direccion, telefono,fechai,ff,ch) -> None:
        super().__init__(dni, nombre, direccion, telefono)
        self.__fecha_inicio = fechai
        self.__fecha_fin = ff
        self.__cant_horas = ch

    @classmethod
    def getvalorh(cls):
        return cls.__valor_x_hora
    
    @classmethod
    def setvalorh(cls,valor):
        cls.__valor_x_hora = valor

    def getcanth(self):
        return self.__cant_horas
    
    def sethoras(self,valor):
        self.__cant_horas += valor

    def calcularsueldo(self):
        sueldo = self.__cant_horas * self.__valor_x_hora
        return sueldo

    def mostrar(self):
        print('Empleado Contratado:')
        print(f'{super().mostrar()}')
        print('Fecha de inicio: {}, Fecha de Finalizacion: {}, Cantidad de horas: {}, Valor por hora: {}' .format(self.__fecha_inicio,self.__fecha_fin,self.__cant_horas,self.getvalorh()))

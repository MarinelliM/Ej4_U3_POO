from Empleados import Empleado
class EPlanta(Empleado):
    __sueldo_basico: int
    __antiguedad: str

    def __init__(self,dni,nombre,direccion,telefono,sueldo,antiguedad) -> None:
        super().__init__(dni,nombre,direccion,telefono)
        self.__sueldo_basico = sueldo
        self.__antiguedad = antiguedad

    def calcularsueldo(self):
        div = self.__sueldo_basico/100
        sueldo = self.__sueldo_basico+ (div * self.__antiguedad)
        return sueldo
    
    def mostrar(self):
        print('Empleado de Planta:')
        print(f'{super().mostrar()}')
        print('Sueldo Basico: {}, Antiguedad: {}' .format(self.__sueldo_basico,self.__antiguedad))

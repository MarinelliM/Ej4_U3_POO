from Empleados import Empleado
class EExterno(Empleado):
    __tarea:str
    __fecha_i:str
    __fecha_f:str
    __monto_viático:int
    __costo_obra:int
    __monto_segurovida:int
    __sueldo = 0
    
    def __init__(self, dni, nombre, direccion, telefono,tarea,fi,ff,mv,costo,ms) -> None:
        super().__init__(dni, nombre, direccion, telefono)
        self.__tarea = tarea
        self.__fecha_i = fi
        self.__fecha_f = ff
        self.__monto_viático = mv
        self.__costo_obra = costo
        self.__monto_segurovida = ms

    def mostrar(self):
        print('Empleado Externo:')
        print(f'{super().mostrar()}')
        print('Fecha inicio: {}, Fecha fin: {}, Monto del Viatico: {}, Costo de la obra: {}, Monto del seguro de vida: {}'.format(self.__fecha_i,self.__fecha_f,self.__monto_viático,self.__costo_obra,self.__monto_segurovida))

    def calcularsueldo(self):
        sueldo = (self.__costo_obra-self.__monto_viático-self.__monto_segurovida)
        return sueldo
class Empleado:
    __dni: int
    __nombre:str
    __direccion:str
    __telefono: int

    def __init__(self,dni,nombre,direccion,telefono) -> None:
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
    
    def calcularsueldo(self):
        pass 

    def getdni(self):
        return self.__dni
    
    def getnombre(self):
        return self.__nombre
    
    def getdireccion(self):
        return self.__direccion
    
    def getdni(self):
        return self.__dni
    
    #def mostrar(self):
    #    print('Nombre del empleado: {}, Dni: {}, Direccion: {}, Telefono: {}' .format(self.__nombre,self.__dni,self.__direccion,self.__telefono))
    def mostrar(self):
        return f'Nombre del empleado: {self.__nombre}, Dni: {self.__dni}, Direccion: {self.__direccion}, Telefono: {self.__telefono}'    
    

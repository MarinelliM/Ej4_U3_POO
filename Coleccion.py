import numpy as np
from Empleados import Empleado
from EContratados import EContratado
from EExternos import EExterno
from EPlanta import EPlanta
import csv
class Coleccion:
    __dimension: int
    __cantidad: int
    __incremento = 5

    def __init__(self,dimension) -> None:
        self.__empleados = np.empty(dimension,dtype=Empleado)
        self.__dimension = dimension
        self.__cantidad = 0

    def agregarempleado(self,empleado):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__empleados.resize(self.__dimension)
        self.__empleados[self.__cantidad] = empleado
        self.__cantidad+=1

    def setdimension(self,dimension):
        self.__dimension = dimension

    def mostrar(self):
        i = 0
        for e in self.__empleados:
            if isinstance(e,Empleado):
                e.mostrar()
                print('\n')
            else: 
                i+=1
                pass
        print('Casillas vacias: {}' .format(i))
        print('\n')

    def mostrarsueldo(self):
        for e in self.__empleados:
            if isinstance(e,Empleado):
                a = e.calcularsueldo()
                print('Sueldo: {}' .format(a))
                print('\n')
            else: pass
    
    def mostrarcontratados(self):
        print('Datos de los empleados Contratados unicamente:')
        for e in self.__empleados:
            if isinstance(e,EContratado):
                e.mostrar()
                print('\n')
            else: 
                pass

    def Registrarhoras(self,dni,ch):
        i = 0
        while i < len(self.__empleados):
            if isinstance(self.__empleados[i],EContratado):
                if dni == self.__empleados[i].getdni() and ch == self.__empleados[i].getcanth():
                    canthoras = int(input('Ingrese las horas que quiere agregar:'))
                    self.__empleados[i].sethoras(canthoras)
                    print('\n')
                    print('Horas actualizadas, nuevos datos del empleado:')
                    self.__empleados[i].mostrar()
                    i=len(self.__empleados)
                else: i+=1
            else: i+=1
        print('\n')

    def ayudaeconomica(self):
        i = 0
        print('Le corresponde una ayuda economica a los siguientes empleados:')
        while i < len(self.__empleados):
            if self.__empleados[i] != None:
                if self.__empleados[i].calcularsueldo() < 150000:
                    print('Nombre: {}, Direccion: {}, Dni: {}' .format(self.__empleados[i].getnombre(),self.__empleados[i].getdireccion(),self.__empleados[i].getdni()))
                    print('\n')
                    i+=1
                else: i+=1
            else: i+=1

    def agregaree(self):
        with open('externos.csv','r',encoding='utf8') as archivo:
            reader = csv.reader(archivo,delimiter=',')
            next(reader)
            for fila in reader:
                dni = int(fila[0])
                nombre = str(fila[1])
                direccion = str(fila[2])
                telefono = int(fila[3])
                tarea = str(fila[4])
                fecha_i = str(fila[5])
                fecha_f = str(fila[6])
                monto_v = int(fila[7])
                costo_o = int(fila[8])
                monto_s = int(fila[9])
                empleado = EExterno(dni,nombre,direccion,telefono,tarea,fecha_i,fecha_f,monto_v,costo_o,monto_s)
                self.agregarempleado(empleado)
    
    def agregarec(self):
        with open('contratados.csv','r',encoding='utf8') as archivo:
            reader = csv.reader(archivo,delimiter=',')
            next(reader)
            for fila in reader:
                dni = int(fila[0])
                nombre = str(fila[1])
                direccion = str(fila[2])
                telefono = int(fila[3])
                fecha_i = str(fila[4])
                fecha_f = str(fila[5])
                canth = int(fila[6])
                empleado = EContratado(dni,nombre,direccion,telefono,fecha_i,fecha_f,canth)
                self.agregarempleado(empleado)
    
    def agregarep(self):
        with open('planta.csv','r',encoding='utf8') as archivo:
            reader = csv.reader(archivo,delimiter=',')
            next(reader)
            for fila in reader:
                dni = int(fila[0])
                nombre = str(fila[1])
                direccion = str(fila[2])
                telefono = int(fila[3])
                sueldob = int(fila[4])
                antiguedad = int(fila[5])
                empleado = EPlanta(dni,nombre,direccion,telefono,sueldob,antiguedad)
                self.agregarempleado(empleado)
    
    def initc(self,dimension):
        self.setdimension(dimension)
        self.agregarec()
        self.agregaree()
        self.agregarep()
        
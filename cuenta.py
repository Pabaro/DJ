from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.edad = edad
        self.dni = dni
    
    #getter
    @property
    def nombre(self):
        return self.__nombre
    
    #setter
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    #getter
    @property
    def edad(self):
        return self.edad
    
    #setter
    @edad.setter
    def edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("La edad debe ser un número positivo.")
    
   
    #getter
    @property
    def dni(self):
        return self.dni
    
    #setter
    @dni.setter
    def dni(self, dni):
        if len(dni) == 9:
            self.dni = dni
        else:
            print("El DNI debe tener 9 caracteres.")
    
    
    
    def mostrar(self):
        print("Nombre:", self.__nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)
    
    def es_mayor_de_edad(self):
        return self.edad >= 18

class Cuenta(Persona):
    def __init__(self, titular="", cantidad=0.0):
        self.titular = titular
        self.__cantidad = cantidad
        
    #getter
    @property
    def titular(self):
        return self.titular
        
    #setter
    @titular.setter
    def titular(self, titular):
        self.titular = titular
    
    #getter
    @property
    def get_cantidad(self):
        return self.__cantidad
    
    #setter
    def __cantidad(self, cantidad):
        self.__cantidad = cantidad
    
    
    
    def mostrar(self):
        print("Titular:", self.titular)
        print("Cantidad:", self.__cantidad)
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        self.__cantidad -= cantidad



class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.05):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    
    #getter
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    #setter
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion
    
    
    
    def es_titular_valido(self):
        edad = self.titular().edad()
        return edad >= 18 and edad < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
    
    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print("Bonificación:", self.__bonificacion)

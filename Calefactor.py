import abc
from abc import ABC
class Calefactor(ABC):
    __marca=''
    __modelo=''
    __costo=0
    def __init__(self,marca='',modelo=''):
        self.__marca=marca
        self.__modelo=modelo
        self.__costo=0
    def setCosto(self,costo):
        self.__costo=costo
    def getModelo(self):
        return self.__modelo
    def getMarca(self):
        return self.__marca
    def getCosto(self):
        return self.__costo
    def __lt__(self,otroCalefactor):
        resultado=False
        if isinstance(otroCalefactor,Calefactor):
            resultado=self.__costo<otroCalefactor.getCosto()
        return resultado
    def __str__(self):
        return 'Marca:{} Modelo:{}'.format(self.__marca, self.__modelo)
    @abc.abstractclassmethod
    def calcularCosto():
        pass
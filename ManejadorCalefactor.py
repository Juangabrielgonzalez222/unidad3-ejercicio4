import csv,numpy as np
from Calefactor import Calefactor
from CalefactorElectrico import CalefactorElectrico
from CalefactorGas import CalefactorGas
class ManejadorCalefactor:
    __arregloCalefactores=None
    __cantidad=0
    __dimension=0
    __incremento=0
    def __init__(self,dimension=3,incremento=5):
        self.__arregloCalefactores=np.empty(dimension,dtype=Calefactor)
        self.__dimension=dimension
        self.__incremento=incremento
        self.__cantidad=0
    def agregarCalefactor(self,equipo):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.redimensionarArreglo()
        self.__arregloCalefactores[self.__cantidad]=equipo
        self.__cantidad+=1
    def redimensionarArreglo(self):
        self.__arregloCalefactores.resize(self.__dimension)
    def verificarDimension(self):
        if self.__cantidad!=self.__dimension:
            self.__dimension=self.__cantidad
            self.redimensionarArreglo()
    def cargarDesdeArchivo(self):
        nombreArchivo='calefactor-electrico.csv'
        archivo=open(nombreArchivo,encoding='utf-8')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                self.agregarCalefactor(CalefactorElectrico(fila[0],fila[1],int(fila[2])))
        print('Fin de la carga desde: ',nombreArchivo)
        archivo.close()
        nombreArchivo='calefactor-a-gas.csv'
        archivo=open(nombreArchivo,encoding='utf-8')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                self.agregarCalefactor(CalefactorGas(fila[0],fila[1],fila[2],int(fila[3])))
        print('Fin de la carga desde: ',nombreArchivo)
        archivo.close()
        self.verificarDimension()
    def calcularCostoGas(self,costoGas,cantidad):
        for i in range(self.__cantidad):
            if type(self.__arregloCalefactores[i])==CalefactorGas:
                self.__arregloCalefactores[i].calcularCosto(costoGas,cantidad)
    def calcularCostoElectrico(self,costoEnergia,cantidad):
        for i in range(self.__cantidad):
            if type(self.__arregloCalefactores[i])==CalefactorElectrico:
                self.__arregloCalefactores[i].calcularCosto(costoEnergia,cantidad)
    def buscarCalefactorGas(self,costoGas,cantidad):
        self.calcularCostoGas(costoGas,cantidad)
        iMenor=None
        bandera=True
        for i in range(self.__cantidad):
            if type(self.__arregloCalefactores[i])==CalefactorGas:
                if bandera:
                    iMenor=i
                    bandera=not bandera
                else:
                    if self.__arregloCalefactores[i]<self.__arregloCalefactores[iMenor]:
                        iMenor=i
        if iMenor!=None:
            print(self.__arregloCalefactores[iMenor])
    def buscarCalefactorElectrico(self,costoEnergia,cantidad):
        self.calcularCostoElectrico(costoEnergia,cantidad)
        iMenor=None
        bandera=True
        for i in range(self.__cantidad):
            if type(self.__arregloCalefactores[i])==CalefactorElectrico:
                if bandera:
                    iMenor=i
                    bandera=not bandera
                else:
                    if self.__arregloCalefactores[i]<self.__arregloCalefactores[iMenor]:
                        iMenor=i
        if iMenor!=None:
            print(self.__arregloCalefactores[iMenor])
    def buscarCalefactorMenorConsumo(self):
        iMenor=0
        for i in range(1,self.__cantidad):
            if self.__arregloCalefactores[i]<self.__arregloCalefactores[iMenor]:
                iMenor=i
        self.__arregloCalefactores[iMenor].mostrarDatos()
from Calefactor import Calefactor
class CalefactorGas(Calefactor):
    __matricula=''
    __calorias=0
    def __init__(self,marca='',modelo='',matricula='',calorias=0):
        super().__init__(marca,modelo)
        self.__matricula=matricula
        self.__calorias=calorias
    def calcularCosto(self,costo,cantidadConsumida):
        self.setCosto((self.__calorias/1000)*cantidadConsumida*costo)
    def mostrarDatos(self):
        print('Tipo:{} Marca:{} Modelo:{} Matricula:{} Calorias:{} kilocalorias'.format('Calefactor A Gas',self.getMarca(),self.getModelo(),self.__matricula,self.__calorias))
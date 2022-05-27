from Calefactor import Calefactor
class CalefactorElectrico(Calefactor):
    __potencia=0
    def __init__(self,marca='',modelo='',potencia=0):
        super().__init__(marca,modelo)
        self.__potencia=potencia
    def calcularCosto(self,costoEnergia,cantidad):
        self.setCosto((self.__potencia/1000) *cantidad*costoEnergia)
    def mostrarDatos(self):
        print('Tipo:{} Marca:{} Modelo:{} Potencia Maxima:{} watts '.format('Calefactor Electrico',self.getMarca(),self.getModelo(),self.__potencia))
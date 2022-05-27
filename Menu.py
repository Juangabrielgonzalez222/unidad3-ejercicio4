class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.salir
        }
    def lanzarMenu(self,manejadorCalefactor):
        #Menu opciones
        i=len(self.__opciones)
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1 para ingresar por teclado el  costo por m3 y cantidad que se estima consumir en m3 y mostrar marca y modelo del calefactor a gas natural de menor costo de consumo.')
            print('-Ingrese 2 para ingresar por teclado el costo de el kilowatt/h, la cantidad que se estima consumir por hora y mostrar  marca  y modelo del calefactor eléctrico de menor consumo.')
            print('-Ingrese 3 para mostrar tipo de calefactor y todos los datos del calefactor de menor consumo.')
            print('-Ingrese 4 para salir.')
            opcion=self.cargarNumeroEntero('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion>0 and opcion<4:
                ejecutar(manejadorCalefactor)
            else:
                ejecutar()
    def opcion1(self,manejadorCalefactor):
        costoGas=self.cargarFlotante('Ingrese costo por m3:\n')
        cantidad=self.cargarNumeroEntero('Ingrese cantidad a consumir:\n')
        manejadorCalefactor.buscarCalefactorGas(costoGas,cantidad)
    def opcion2(self,manejadorCalefactor):
        costoEnergia=self.cargarFlotante('Ingrese costo del kilowatt/h:\n')
        cantidad=self.cargarNumeroEntero('Ingrese cantidad a consumir por hora:\n')
        manejadorCalefactor.buscarCalefactorElectrico(costoEnergia,cantidad)
    def opcion3(self,manejadorCalefactor):
        costoGas=self.cargarFlotante('Ingrese costo por m3:\n')
        cantidad=self.cargarNumeroEntero('Ingrese cantidad a consumir m3:\n')
        manejadorCalefactor.calcularCostoGas(costoGas,cantidad)
        costoEnergia=self.cargarFlotante('Ingrese costo del kilowatt/h:\n')
        cantidad=self.cargarNumeroEntero('Ingrese cantidad a consumir por hora:\n')
        manejadorCalefactor.calcularCostoElectrico(costoEnergia,cantidad)
        manejadorCalefactor.buscarCalefactorMenorConsumo()
    def cargarNumeroEntero(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se debe ingresar un numero entero.')
            else:
                bandera=False
        return numero
    def cargarFlotante(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se admiten numeros enteros y punto ,por ejemplo:500 o 500.50')
            else:
                bandera=False
        return numero
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')
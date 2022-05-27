from ManejadorCalefactor import ManejadorCalefactor
from Menu import Menu

if __name__== '__main__':
	bandera=True
	cantidadCalefactores=0
	while bandera:
		try:
			cantidadCalefactores=int(input('Ingrese la cantidad total de calefactores:\n'))
		except ValueError:
			print('Solo se aceptan numeros enteros.')
		else:
			bandera=not bandera
	manejadorCalefactor=ManejadorCalefactor(cantidadCalefactores,5)
	manejadorCalefactor.cargarDesdeArchivo()
	menu=Menu()
	menu.lanzarMenu(manejadorCalefactor)
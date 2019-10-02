"""                 GESTOR DE MULTIMEDIA

Juan Pablo Delgado.
Elkin Quiñones Mosquera.
Brayan Daniel Romero Ardila.
Daniel Felipe Quiroga Parra.

Este es el archivo principal del código del programa. Aquí se encuentra las
funciones que mantienen abierta la aplicación. La librería importada corresponde
al archivo de código de los menús.

ARCHIVOS DE CÓDIGO:
    - MenuFile.py
    - files.py
    - Miscellaneous.py """

import MenuFile

def main():

	"""Mantiene el programa abierto hasta que el usuario confirma que desea
	cerrarlo.
	- No utiliza argumentos.
	- No devuelve nada.
    - Llama al menú principal de MenuFile.py
	- Es la función principal."""

	programOn = True
	while programOn == True:
		MenuFile.MainMenu()
		programOn = LogOut()

def LogOut():

	"""Esta función de encarga de confirmar si el usuario desea cerrar el
	programa.
	- No utiliza argumentos.
	- Retorna un valor booleano que rompe el bucle de la función main()
	según la entrada del usuario.
	- Si la entrada no es válida se llama a sí misma hasta retornar True
	o False."""

	print("¿Desea salir de la aplicación? (SI \ NO)")
	logOutConfirmation = input("su respuesta: ")
	if logOutConfirmation.lower() == "si":
		return False
	elif logOutConfirmation.lower() == "no":
		return True
	else:
		return LogOut()

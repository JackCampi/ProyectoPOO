import Miscellaneous

def main():
	"""Mantiene el programa abierto hasta que el usuario confirma que desea
	cerrarlo."""
	programOn = True
	while programOn == True:
		MainMenu()
		programOn = LogOut()

def LogOut():

	"""Esta función de encarga de confirmar si el usuario desea cerrar el
	programa. Devuelve un valor booleano que según la respuesta del usuario
	rompe o no el bucle de la función main()."""

	print("¿Desea salir de la aplicación? (SI \ NO)")
	logOutConfirmation = input("su respuesta: ")
	if logOutConfirmation.lower() == "si":
		return False
	elif logOutConfirmation.lower() == "no":
		return True
	else:
		return LogOut()

def MainMenu():

	"""Esta función corresponde al menú principal en el cual el usuario
	tiene la opción de seleccionar el formato al que quiere acceder (Música,
	Fotos o Videos). Este menú llama al segundo menú pasándole como argumento
	lo que el usuario elija."""

	print("\n===================0===================\n")
	print("\tMENÚ PRINCIPAL\n\n1. Música.\n2. Fotos.\n3. Videos.\n\n0. Salir.\n")
	answer1 = Answer(["0","1","2","3"])
	if answer1 == "0":
		return
	elif answer1 == "1":
		SecondMenu("music")
		MainMenu()
	elif answer1 == "2":
		SecondMenu("pictures")
		MainMenu()
	elif answer1 == "3":
		SecondMenu("videos")
		MainMenu()

def Answer(options):

	"""Esta función pide la entrada del usuario y la evalúa de manera que
	esta corresponda a las opciones disponibles en cada menú. Recibe como
	parámetro una lista de las opciones que el usuario tiene disponibles y
	a partir de esta compara si la entrada corresponde a alguna de ellas, de
	lo contrario, la función se encarga de pedirle al usuario una respuesta
	válida. Retorna la opción final del usuario como un string."""

	validAnswer = False
	answer = "x"
	while validAnswer == False:
		answer = input("Seleccione el número de la opción: ")
		if answer in options:
			validAnswer = True
		else:
			print("Respuesta inválida, por favor intente de nuevo.")
	return answer

def SecondMenu(_format):

	"""Esta función se encarga de mostrar el segundo menú y las opciones para
	que el usuario pueda ver sus archivos multimedia o las listas de reproducción.
	La primera opción hace un llamado al tercer menú, mientras que la segunda
	llama a un quinto menú donde puede visualizar las demás opciones."""

	print("\n===================0===================\n")
	print("\t"+ MenuFormat(_format).upper()+"\n")
	print("1. Mi"+ MenuFormat(_format,False) +".\n2. Listas de reproducción.\n\n0. Atrás.\n")
	answer2 = Answer(["0","1","2"])
	if answer2 == "0":
		return
	elif answer2 == "1":
		ThirdMenu(_format)
		SecondMenu(_format)
	elif answer2 == "2":
		FifthMenu(_format)
		SecondMenu(_format)

def ThirdMenu(_format):

	"""Esta función corresponde al tecer menú, en el cual el usuario puede
	escoger entre ver de manera ordenada todas sus canciones fotos o videos,
	buscar un elemento o añadir uno nuevo."""

	print("\n===================0===================\n")
	print("\tMI"+ MenuFormat(_format, False).upper()+"\n")
	print("1. Ver mi"+ MenuFormat(_format, False) +".\n2. Buscar.\n3. Añadir.\n\n0. Atrás.\n")
	answer3 = Answer(["0","1","2","3"])
	if answer3 == "0":
		return
	elif answer3 == "1":
		FourthMenu(_format)
		ThirdMenu(_format)
	elif answer3 == "2":
		SearchMenu(_format)
		ThirdMenu(_format)
	elif answer3 == "3":
		#Función de añadir de Juan
		ThirdMenu(_format)

def SearchMenu(_format):

	"""Esta función corresponde al menú de busqueda, en el cual el usuario
	introduce una información sobre un elemento, ya sea el nombre, el álbum, el
	año, etc. y se imprimen las posibles opciones para dicha búsqueda. Desde
	este menú es posible eliminar un elemento, modificar su información o
	añadirlo a una lista de reproducción."""

	print("\n===================0===================\n")
	print("\tBUSCAR EN MI" + MenuFormat(_format,False).upper()+ "\n")
	toSearch = input("¿Qué desea buscar? ")
	searchResults = Miscellaneous.SearchMainList(_format,toSearch)

	#PARTE DE CODIGO FALTANTE: La función SearchMainList retorna una lista.

	print("¿Qué desea hacer con este elemento?\n1. Añadir a lista de reproducción.\n2. Eliminar.\n3. Modificar información.\n\n0. Atrás.")
	answer = Answer(["0","1","2","3"])
	if answer == "0":
		return
	elif answer == "1":
		#función de añadir a lista de Juan
		print()
		return
	elif answer == "2":
		#función de eliminar de Juan
		print()
		return
	elif answer == "3":
		#Menú de modificación
		print()
		return


def FourthMenu(_format):

	"""Esta función corresponde al cuarto menú, el cual le da al usuario las
	opciones de vizualizar sus canciones, fotos o videos según el orden que
	escoja."""

	print("\n===================0===================\n")
	print("\tVER MI"+ MenuFormat(_format,False).upper() +"\n")
	print(FourthMenuOptions(_format))
	answer4 = Answer(["0","1","2","3","4","5"])
	if answer4 == "0":
		return
	elif answer4 == "1":
		sortedList = Miscellaneous.SortMainList(_format,"name")
		FourthMenu(_format)
	elif answer4 == "2":
		sortedList = Miscellaneous.SortMainList(_format,"author")
		FourthMenu(_format)
	elif answer4 == "3":
		sortedList = Miscellaneous.SortMainList(_format,"album")
		FourthMenu(_format)
	elif answer4 == "4":
		sortedList = Miscellaneous.SortMainList(_format,"year")
		FourthMenu(_format)
	elif answer4 == "5":
		sortedList = Miscellaneous.SortMainList(_format,"type")
		FourthMenu(_format)

def FourthMenuOptions(_format):

	"""Esta función devuelve las opciones para el cuarto menú según el formato
	que se esté usando."""

	if _format == "music":
		return "1. Por nombre.\n2. Por artista.\n3. Por álbum.\n4. Por año.\n5. Por género.\n\n0. Atrás.\n"
	else:
		return "1. Por nombre.\n2. Por protagonista.\n3. Por álbum.\n4. Por año.\n5. Por tipo.\n\n0. Atrás.\n"

def MenuFormat(_format, onlyFormat = True):

	"""Esta función devuelve strings que son utilizados en los menús para
	completar los textos de los títulos o las opciones. De manera general,
	devuelve una traducción del formato. El segundo argumento de esta función
	hace que el string que se devuelve tenga los caracteres para completar
	frases como "mi música" o "mis videos" (la letra s y un espacio)."""

	if _format == "music":
		if onlyFormat != True:
			return " música"
		return "música"
	elif _format == "pictures":
		if onlyFormat != True:
			return "s fotos"
		return "fotos"
	else:
		if onlyFormat != True:
			return "s videos"
		return "videos"

main()

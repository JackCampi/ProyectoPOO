"""En este módulo se encuentran los menús que se imprimen en la consola. Toma
funciones de Miscellaneous.py y files.py, los cuales corresponden al manejo de
los archivos y la información."""

import Miscellaneous
import files
import os

def main():

	"""Mantiene el programa abierto hasta que el usuario confirma que desea
	cerrarlo.
	- No utiliza argumentos.
	- No devuelve nada.
	- Es la función principal."""

	programOn = True
	while programOn == True:
		MainMenu()
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

"""A partir de esta linea se declaran las funciones de los menús"""

def MainMenu():

	"""Esta función corresponde al menú principal en el cual el usuario
	tiene la opción de seleccionar el formato al que quiere acceder (Música,
	Fotos o Videos).
	- Este menú llama al segundo menú pasándole como argumento el formato que
	el usuario elija.
	- Se llama a sí misma una vez la función llamada termine."""

	print("\n===================0===================\n")
	print("\tMENÚ PRINCIPAL\n\n1. Música.\n2. Fotos.\n3. Videos.\n\n0. Salir.\n")
	answer1 = Answer(["0","1","2","3"])
	if answer1 == "0":
		return
	elif answer1 == "1":
		SecondMenu("music")
	elif answer1 == "2":
		SecondMenu("pictures")
	elif answer1 == "3":
		SecondMenu("videos")
	MainMenu()

def SecondMenu(_format):

	"""Esta función se encarga de mostrar el segundo menú y las opciones para
	que el usuario pueda ver sus archivos multimedia o las listas de reproducción.
	- Recibe como argumento el formato sobre el que se está trabajando.
	- La primera opción hace un llamado al tercer menú.
	- La segunda opción llama al quinto menú.
	- Se llama a sí misma cuando las funciones llamadas se acaban."""

	print("\n===================0===================\n")
	print("\t"+ MenuFormat(_format).upper()+"\n")
	print("1. Mi"+ MenuFormat(_format,False) +".\n2. Listas de reproducción.\n\n0. Atrás.\n")
	answer2 = Answer(["0","1","2"])
	if answer2 == "0":
		return
	elif answer2 == "1":
		ThirdMenu(_format)
	elif answer2 == "2":
		FourthMenu(_format)
	SecondMenu(_format)

def ThirdMenu(_format):

	"""Esta función corresponde al tecer menú, en el cual el usuario puede
	escoger entre ver de manera ordenada todas sus canciones fotos o videos,
	buscar un elemento o añadir uno nuevo.
	- La primera opción llama al cuarto menú.
	- La segunda opción llama al menú de búsqueda.
	- La tercera opción llama al menú de añadir elemento.
	- Se llama a sí misma cuando las funciones llamadas se acaban."""

	print("\n===================0===================\n")
	print("\tMI"+ MenuFormat(_format, False).upper()+"\n")
	print("1. Ver mi"+ MenuFormat(_format, False) +".\n2. Buscar.\n3. Añadir.\n\n0. Atrás.\n")
	answer3 = Answer(["0","1","2","3"])
	if answer3 == "0":
		return
	elif answer3 == "1":
		SortListMenu(_format, "mi"+ MenuFormat(_format,False))
	elif answer3 == "2":
		SearchMenu(_format)
	elif answer3 == "3":
		AddElementMenu(_format)
	ThirdMenu(_format)

def AddElementMenu(_format):

	""" Esta función corresponde al menú donde el usuario ingresa los datos de
	un nuevo elemento para añadirlo a la lista principal del formato.
	-Recibe como argumento el formato sobre el cual se está trabajando, con
	el fin de modificar el archivo principal.
	- Llama a la función TakeElementInfo, que devuelve el diccionario de la
	nueva entrada.
	- Hace un llamado a la función AddEntry de la librería files.
	- No retorna ningún valor, pero imprime un mensaje que indica que la acción
	se realizó."""

	print("\n===================0===================\n")
	print("\tAÑADIR A MI"+MenuFormat(_format, False).upper()+"\n")
	newElementDic = TakeElementInfo()
	files.AddEntry(newElementDic,_format)
	print("\nEl elemento se ha añadido a \"mi{0}\".".format(MenuFormat(_format, False)))

def TakeElementInfo():

	"""Esta función corresponde al menú donde se toman los datos de un elemento
	(nombre, autor, album, etc.) y devuelve un diccionario que puede ser utilizado
	para añadir un nuevo elemento o modificar uno existente.
	Devuelve diccionario con datos introducidos por el usuario."""

	ElementDic = {"name": "" ,"author" : "" , "album" : "" , "year" : "", "type" : "" , "path" : ""}
	ElementDic["name"] = input("Nombre: ")
	ElementDic["author"] = input("Autor: ")
	ElementDic["album"] = input("Álbum: ")
	ElementDic["year"] = input("Año: ")
	ElementDic["type"] = input("Género: ")
	ElementDic["path"] = input("Archivo: ")
	return ElementDic #Pasar para abajo

def SearchMenu(_format):

	"""Esta función corresponde al menú de búsqueda, en el cual el usuario
	introduce una información sobre un elemento, ya sea el nombre, el álbum, el
	año, etc. y se imprimen las posibles opciones para dicha búsqueda.
	- En el caso de no haber resultados llama a NotFoundMenu y le pregunta al
	usuario si desea realizar la búsqueda de nuevo o salir al tercer menú.
	- En el caso de haber más de un resultado, le pide al usuario seleccionar
	algún elemento.
	- Con el elemento encontrado llama a FoundElementMenu, donde el usuario
	dispone de más opciones.
	- Al terminar, vuelve al tercer menú."""

	print("\n===================0===================\n")
	print("\tBUSCAR EN MI" + MenuFormat(_format,False).upper()+ "\n")
	toSearch = input("¿Qué desea buscar? ")
	searchResults = Miscellaneous.SearchMainList(_format,toSearch)
	if len(searchResults) == 0 :
		answer = NotFoundMenu(_format, "mi" + MenuFormat(_format, False))
		if answer == "0":
			return
		else:
			SearchMenu(_format)
			return
	elif len(searchResults) == 1:
		searchElement = searchResults[0]
	else:
		PrintList(_format,searchResults)
		searchElement = searchResults[SelectListElement(len(searchResults))]
	FoundElementMenu(_format, searchElement)

def FoundElementMenu(_format, foundElement):
	#FALTA CÓDIGO

	"""Esta función corresponde al menú que el usuario dispone cuando encuentra
	un elemento. Desde este menú puede añadir dicho elemento a una lista de
	reproducción, eliminarlo o modificar su información.
	- La primera opción .......
	- La segunda opción elimina el elemento mediante la función DeleteEntry de
	la librería files.
	- La tercera opción lleva al menú de modificación, donde se ingresa la nueva
	información del elemento.
	- Al terminar, vuelve al tercer menú."""

	print("\n===================0===================\n")
	PrintListHead(_format)
	print("1.\t|\t{0}\t|\t{1}\t|\t{2}\t|\t{3}\t|\t{4}\n".format(foundElement["name"],foundElement["author"],foundElement["album"],foundElement["year"],foundElement["type"]))
	print("¿Qué desea hacer con este elemento?\n1. Añadir a lista de reproducción.\n2. Eliminar.\n3. Modificar información.\n\n0. Atrás.")
	answer = Answer(["0","1","2","3"])
	if answer == "0":
		return
	elif answer == "1":
		#menu de añadir a lista de reproducción
		#función de añadir a lista de Juan
		print()
		return
	elif answer == "2":
		files.DeleteEntry(foundElement, _format)
		print("Se ha eliminado el elemento. Volviendo a \"MI" + MenuFormat(_format,False).upper()+"\".")
		return
	elif answer == "3":
		ModifyElementMenu(_format,foundElement)
		return

def AddToPlaylistMenu(_format, toAddElement):
	#FALTA CÓDIGO
	#mostrar las playlist
	playlistName = input("¿A cuál lista desea agregar este elemento? ")

def ModifyElementMenu(_format, oldElementDic):

	"""Esta función corresponde al menú donde el usuario ingresa la nueva
	información de un elemento para modificarlo.
	- Llama a TakeElementInfo para tomar la nueva información, y a ModifyList
	de la librería files para reemplazar el archivo principal.
	- Al terminar, vuelve al tercer menú."""

	print("\nIngrese la nueva información del elemento.")
	newElementDic = TakeElementInfo()
	files.ModifyList(newElementDic,oldElementDic,_format)
	print("Se ha modificado la información del elemento. Volviendo a \"MI" + MenuFormat(_format,False).upper()+"\".")

def NotFoundMenu(_format, listName ):

	"""Esta función corresponde al menú donde el usuario escoge si desea volver
	a buscar o salir al menú anterior en el caso de que no se hayan encontrado
	elementos.
	- Toma como argumentos el formato sobre el que se está trabajando y el string
	del nombre de la lista en la que se estaba buscando.
	- Retorna la opción que el usuario ingrese para que esta pueda ser utilizada
	en la función donde fue llamada."""

	print("No se encontró ningún elemento en " + listName +".\n")
	print("1. Volver a buscar.\n\n0. Atrás.\n")
	answer = Answer(["0","1"])
	return answer

def SortListMenu(_format, listName , listPath = "Main_list.txt"): #Modificando...

	"""CORREGIR... Esta función corresponde al menú de listas ordenadas, el cual le da al
	usuario las opciones de vizualizar la lista según el orden que
	escoja.
	- Recibe como argumento el formato sobre el cual se está trabajando.
	- Desde la primera opción a la quinta imprime una lista de elementos
	ordenados según la característica seleccionada por el usuario.
	- Al imprimir las listas se llama a sí misma hasta que el usuario desea salir.
	- Al salir, vuelve al tercer menú."""

	print("\n===================0===================\n")
	print("\tVER "+ listName.upper() +"\n")
	print(SortListMenuOptions(_format))
	answer4 = Answer(["0","1","2","3","4","5"])
	if answer4 == "0":
		return
	elif answer4 == "1":
		listToPrint = files.ReadFormat(_format,listPath)
		sortedList = Miscellaneous.SortList(listToPrint,"name")
		if len(sortedList) == 0:
			print("No hay elementos en "+listName+".")
		else:
			PrintList(_format,sortedList)
	elif answer4 == "2":
		listToPrint = files.ReadFormat(_format,listPath)
		sortedList = Miscellaneous.SortList(listToPrint,"author")
		if len(sortedList) == 0:
			print("No hay elementos en "+listName+".")
		else:
			PrintList(_format,sortedList)
	elif answer4 == "3":
		listToPrint = files.ReadFormat(_format,listPath)
		sortedList = Miscellaneous.SortList(listToPrint,"album")
		if len(sortedList) == 0:
			print("No hay elementos en "+listName+".")
		else:
			PrintList(_format,sortedList)
	elif answer4 == "4":
		listToPrint = files.ReadFormat(_format,listPath)
		sortedList = Miscellaneous.SortList(listToPrint,"year")
		if len(sortedList) == 0:
			print("No hay elementos en "+listName+".")
		else:
			PrintList(_format,sortedList)
	elif answer4 == "5":
		listToPrint = files.ReadFormat(_format,listPath)
		sortedList = Miscellaneous.SortList(listToPrint,"type")
		if len(sortedList) == 0:
			print("No hay elementos en "+listName+".")
		else:
			PrintList(_format,sortedList)
	SortListMenu(_format)
	
def FourthMenu(_format):
	#FALTA CODIGO
	print("\n===================0===================\n")
	print("\tLISTAS DE REPRODUCCIÓN DE " + MenuFormat(_format).upper() + "\n")
	print("1. Mis listas.\n2. Crear lista.\n3. Buscar lista.\n4. Eliminar lista.\n\n0. Salir.\n")
	answer = Answer(["0","1","2","3","4"])
	if answer == "0":
		return
	elif answer == "1":
		playlists = files.GetPlaylists(_format)
		if len(playlist) == 0:
			print("No hay listas de reproducción en " + MenuFormat(_format) + ".")
		else:
			for playlistIndex in range(len(playlists)):
				print(str(playlistIndex+1)+"\t|\t"+playlists[playlistIndex] + ".\n")
			print("1. Seleccionar una lista de reproducción.\n\n0. Atrás.\n")
			answer1 = Answer(["0","1"])
			if answer1 == "1":
				playlistName = playlists[SelectListElement(len(playlists))]
				PlaylistMenu(_format, playlistName)
	elif answer == "2":
		NewPlaylistMenu(_format)
	elif answer == "3":
		#función de buscar una lista.
		print()
	elif answer == "4":
		#función de eliminar una lista.
		print()
	FourthMenu(_format)

def PlaylistMenu(_format, playlistName):
	print("\n" + playlistName.upper() + "\n")
	print("1. Ver contenido de la lista.\n2. Añadir un elemento.\n3. Eliminar un elemento.\n4. Eliminar lista.\n\n0. Atrás.\n")
	answer = Answer(["0","1","2","3","4"])
	if answer == "0":
		return
	elif answer == "1":
		PrintPlaylist(_format,playlistName)
	elif answer == "2":
		AddPlaylistElement(_format,playlistName)
	elif answer == "3":
		DeletePlaylistElement(_format, playlistName)
	elif answer == "4":
		files.DeletePlaylist(_format,playlistName)
		print("La lista fue eliminada.")
	PlaylistMenu(_format, playlistName)

def PrintPlaylist(_format,playlistName):
	playlistPath = "playlist"+ os.sep + playlistName + ".txt"
	SortListMenu(_format,playlistName,playlistPath)

def AddPlaylistElement(_format, playlistName):
	element = input("¿Qué elemento desea agregar a la lista? ") ## Cambios
	results = Miscellaneous.SearchMainList(_format,element)
	if len(results) == 0:
		option = NotFoundMenu(_format, "mi"+MenuFormat(_format,False))
		if option == "0":
			return
		else:
			AddPlaylistElement(_format, playlistName)
	elif len(results) == 1:
		finalElement = results[0]
	else:
		finalElement = results[SelectListElement(len(results))]
	PrintListHead(_format)
	print("1.\t|\t{0}\t|\t{1}\t|\t{2}\t|\t{3}\t|\t{4}\n".format(finalElement["name"],finalElement["author"],finalElement["album"],finalElement["year"],finalElement["type"]))
	print("¿Desea añadir este elemento a " + playlistName + "?\n1. Confirmar.\n0. Cancelar.")
	answer = Answer(["0","1"])
	if answer == 0:
		print("No se añadió el elemento.\n")
		return
	else:
		playlistPath = "playlist"+ os.sep + playlistName + ".txt"
		files.AddEntry(finalElement ,_format , playlistPath)
		print("Se añadió \""+finalElement["name"]+ "\" a " + playlistName + ". Volviendo al menú de la lista de reproducción.")

def DeletePlaylistElement(_format, playlistName):
	playlistPath = "playlist"+ os.sep + playlistName + ".txt"
	playlistList = file.ReadFormat(_format, playlistPath)
	element = input("¿Qué elemento desea eliminar? ")
	results = Miscellaneous.BinarySearch(playlistList,element)
	if len(results) == 0:
		option = NotFoundMenu(_format, playlistName)
		if option == "0":
			return
		else:
			DeletePlaylistElement(_format, playlistName)
	elif len(results) == 1:
		finalElement = results[0]
	else:
		finalElement = results[SelectListElement(len(results))]
	PrintListHead(_format)
	print("1.\t|\t{0}\t|\t{1}\t|\t{2}\t|\t{3}\t|\t{4}\n".format(finalElement["name"],finalElement["author"],finalElement["album"],finalElement["year"],finalElement["type"]))
	print("¿Desea eliminar este elemento de " + playlistName + "?\n1. Confirmar.\n0. Cancelar.")
	answer = Answer(["0","1"])
	if answer == 0:
		print("El elemento no se eliminó.\n")
		return
	else:
		files.DeleteEntry(finalElement,_format,playlistPath)
		print("Se eliminó el elemento de " + playlistName + ". Volviendo al menú de la lista de reproducción.")


def NewPlaylistMenu(_format):
	print("\n===================0===================\n")
	print("\tCREAR LISTA DE REPRODUCCIÓN\n")
	playlistName = input("Nombre de la lista de reproducción: ")
	files.MakePlaylist(_format,playlistName)
	print("La lista de reproducción ha sido creada.\n\n¿Desea añadir elementos a la lista?\n1. Aceptar.\n0. Cancelar.\n")
	answer = Answer(["0","1"])
	if answer == "0":
		return
	else:
		adding = True
		while adding == True:
			AddPlaylistElement(_format, playlistName)
			print("¿Desea añadir otro elemento a la lista?\n1. Aceptar.\n0. Cancelar.\n")
			answer1 = Answer(["0","1"])
			if answer1 == "0":
				adding == False

"""Desde aqui se declaran las funciones secundarias que son utilizadas dentro de
las funciones de menús."""

def Answer(options):

	"""Esta función pide la entrada del usuario y la evalúa de manera que
	esta corresponda a las opciones disponibles en cada menú.
	- Recibe como argumento una lista de las opciones que el usuario tiene
	disponibles.
	- Compara la entrada del usuario con la lista de opciones. Si la Respuesta
	no es válida, la función se encarga de pedir una nueva entrada.
	- Retorna la opción final del usuario como un string."""

	validAnswer = False
	answer = "x"
	while validAnswer == False:
		answer = input("Seleccione el número de la opción: ")
		if answer in options:
			validAnswer = True
		else:
			print("Respuesta inválida, por favor intente de nuevo.")
	return answer

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

def PrintList(_format,_list):
	"""Esta función se encarga de imprimir las listas con la cabecera de manera
	ordenada"""
	PrintListHead(_format)
	for dicIndex in range(len(_list)):
		PrintListElement(_list , dicIndex)

def PrintListElement(_list,dicIndex = 0):

	"""Imprime la información de una canción/foto/video de manera ordenada. Al
	principio añade un índice que se utiliza para enumerar los elementos en el
	caso de que estos sean varios."""

	toPrint = "{0}.\t|\t{1}\t|\t{2}\t|\t{3}\t|\t{4}\t|\t{5}\n"
	print(toPrint.format(dicIndex+1,_list[dicIndex]["name"],_list[dicIndex]["author"],_list[dicIndex]["album"],_list[dicIndex]["year"],_list[dicIndex]["type"]))

def PrintListHead(_format):
	"""Imprime la cabecera de la lista cuando se muestran los elementos."""
	if _format == "music":
		print("No.\t|\tNombre\t|\tArtista\t|\tÁlbum\t|\tAño\t|\tGénero\n")
	else:
		print("No.\t|\tNombre\t|\tProtagonista\t|\tÁlbum\t|\tAño\t|\tTipo\n")
	return

def SelectListElement(listLength):

	"""Esta función recibe el largo de una lista y devuelve el indice del
	elemento que el usuario escoga."""

	print("¿Cuál desea seleccionar? ")
	selectElement = Answer([str(x) for x in range(1,listLength+1)])
	return int(selectElement) - 1

def SortListMenuOptions(_format):

	"""Esta función devuelve las opciones para el menú de ordenar listas
	según el formato que se esté usando.
	- Devuelve un strings con las opciones que el usuario puede escoger en el
	menú de ordenar listas (Varían para música)."""

	if _format == "music":
		return "1. Por nombre.\n2. Por artista.\n3. Por álbum.\n4. Por año.\n5. Por género.\n\n0. Atrás.\n"
	else:
		return "1. Por nombre.\n2. Por protagonista.\n3. Por álbum.\n4. Por año.\n5. Por tipo.\n\n0. Atrás.\n"

"""Aquí se ejecuta el programa"""

main()

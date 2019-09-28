'''Módulo files, maneja todo lo relacionado con los archivos y a representación
    interna de los elementos'''
import os


def MakeEntry(string):
    """Recibe una cadena que contiene la información de la canción/foto/video
    y lo devuelve como un diccionario.

    parámetros de entrada:
    string -- La cadena que contiene la información de la nueva entrada,
              tiene que estar en el siguiente orden "nombre, autor, album,
              año, género, directorio."

    salida:
    Un diccionario que contiene la información ingresada.
    """
    order = ("name", "author", "album", "year", "genre", "path")
    elements = string.strip("\n").split("¬")
    entry = {}
    for i in range(len(order)):
        if order[i] == "year":
            entry[order[i]] = int(elements[i])
        else:
            entry[order[i]] = elements[i]
    return entry


def ToString(entry):
    """Recibe un diccionario que contiene la información de una entrada y
    devuelve una cadena.

    parámetros de entrada:
    entry -- Un diccionario (ver MakeEntry).

    salida:
    Una lista separada por el caracter ¬, que contiene la información de una
    entrada en el siguiente orden "nombre, autor, album, año, género,
    directorio."
    """
    ans = ""
    for i in entry:
        ans += str(entry[i])
        ans += "¬"
    return ans[:-1]


def ReadFormat(_format, name="Main_list.txt"):
    """Recibe el formato y el nombre del archivo de una lista, y devuelve
    una lista de python, donde cada elemento es un diccionario (ver MakeEntry).

    parámetros de entrada:
    _format -- El formato de la lista, puede ser "music", "pictures", o
    "videos."
    name -- El nombre del archivo de la lista, por defecto es "Main_list.txt,
    si se desea cambiar la lista predetermina debe escribir
    "pictures\nombre.txt."

    salida:
    Una lista de python en donde cada elemento es un diccionario representando
    una entrada.
    """
    root = _format
    path = root + os.sep + name
    fileHandler = open(path, "r")
    bigList = []
    try:
        for line in fileHandler:
            entry = MakeEntry(line)
            bigList.append(entry)

    finally:
        fileHandler.close()
        return bigList


def GetOrderedValue(entry):
    """Recibe un diccionario y devuelve un entero que representa el ranking
    del elemento "name" en la entrada-diccionario.

    parámetros de entrada:
    entry -- Un diccionario que contiene la información de una entrada.

    salida:
    Un entero que trata de cuantificar el orden que debería tener el elemento
    en una lista.
    """
    ans = 0
    letters = "abcdefghijklmnñopqrstuvwxyz"
    numbers = "0123456789"
    for i in entry["name"]:
        if i in letters:
            ans += letters.index(i)
        elif i in numbers:
            ans += numbers.index(i)

    return ans


def GetNewPosition(entry, entries):
    """Recibe un diccionario y una lista de entradas, devuelve la posición en
    donde debería estar la entrada en la lista de entradas, teniendo en cuenta
    su puntaje de la función GetOrderedValue.

    parámetros de entrada:
    entry -- Un diccionario que contiene la información de una entrada.
    entries -- Una lista de entradas.

    salida:
    Un entero que representa la posición en donde debería ir la nueva entrada.
    """
    k = GetOrderedValue(entry)
    n = 0
    for i in entries:
        if GetOrderedValue(i) >= k:
            break
        else:
            n += 1
    return n


def AddEntry(newEntry, _format, name="Main_list.txt"):
    """Recibe una entrada, un formato y el nombre de archivo de una lista y
    añade la nueva entrada a la lista.

    parámetros de entrada:
    newEntry -- Entrada que será agregada.
    _format -- El formato de la lista, puede ser "music", "pictures", o
    "videos."
    name -- El nombre del archivo de la lista, por defecto es "Main_list.txt,
    si se desea cambiar la lista predetermina debe escribir
    "playlists\nombre.txt."

    salida:
    No hay salida, solo modifica el archivo.
    """
    entries = ReadFormat(_format)
    root = _format
    path = root + os.sep + name
    fileHandler = open(path, "w")
    n = GetNewPosition(newEntry, entries)
    if n == 0:
        fileHandler.write(ToString(newEntry) + "\n")
        for i in entries:
            fileHandler.write(ToString(i) + "\n")
    elif n >= len(entries):
        for i in entries:
            fileHandler.write(ToString(i) + "\n")
        fileHandler.write(ToString(newEntry) + "\n")
    else:
        for i in range(0, n):
            fileHandler.write(ToString(entries[i]) + "\n")
        fileHandler.write(ToString(newEntry) + "\n")
        for i in range(n, len(entries)):
            fileHandler.write(ToString(entries[i]) + "\n")

    fileHandler.close()


def DeleteEntry(entry, _format, name="Main_list.txt"):
    """Recibe una entrada, un formato y el nombre de archivo de una lista y
    elimina la entrada a la lista.

    parámetros de entrada:
    newEntry -- Entrada que será agregada.
    _format -- El formato de la lista, puede ser "music", "pictures", o
    "videos."
    name -- El nombre del archivo de la lista, por defecto es "Main_list.txt,
    si se desea cambiar la lista predetermina debe escribir
    "playlists\nombre.txt."

    salida:
    No hay salida, solo modifica el archivo.
    """
    entries = ReadFormat(_format)
    root = _format
    path = root + os.sep + name
    fileHandler = open(path, "w")
    for i in entries:
        if i != entry:
            fileHandler.write(ToString(i) + "\n")
    fileHandler.close()

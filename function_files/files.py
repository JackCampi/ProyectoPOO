"""Módulo files, maneja todo lo relacionado con los archivos y la
    representación interna de los elementos"""
import os


def MakeEntry(string):
    """Recibe una cadena que contiene la información de la canción/foto/video
    y lo devuelve como un diccionario.

    parámetros de entrada:
    string -- La cadena que contiene la información de la nueva entrada,
              tiene que estar en el siguiente orden "nombre, autor, album,
              año, género."

    salida:
    Un diccionario que contiene la información ingresada.
    """
    order = ("name", "author", "album", "year", "type", "path")
    elements = string.strip("\n").split("¬")
    entry = {}
    assert len(elements) == len(order), "Entrada inválida"
    for i in range(len(order)):
        entry[order[i]] = elements[i]
    return entry


def ToString(entry):
    """Recibe un diccionario que contiene la información de una entrada y
    devuelve una cadena.

    parámetros de entrada:
    entry -- Un diccionario (ver MakeEntry).

    salida:
    Una lista separada por el caracter ¬, que contiene la información de una
    entrada en el siguiente orden "nombre, autor, album, año, género."
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
    "playlists\nombre.txt."

    salida:
    Una lista de python en donde cada elemento es un diccionario representando
    una entrada.
    """
    root = _format
    path = root + os.sep + name
    fileHandler = open(path, "r")
    bigList = []
    for line in fileHandler:
        entry = MakeEntry(line)
        bigList.append(entry)
    fileHandler.close()
    return bigList


def WriteList(_list, _format, name="Main_list.txt"):
    """
    Recibe una lista de diccionarios, el formato, y el nombre de archivo de una lista.
    No devuelve nada, solo sobrescribe la información de la lista de diccionarios en el archivo.
    :param _list: lista de diccionarios (ver ReadFormat).
    :param _format: Tipo de archivo (ver ReadFormat).
    :param name: Nombre del archivo.
    :return: None
    """
    root = _format
    path = root + os.sep + name
    fileHandler = open(path, "w")
    for i in _list:
        fileHandler.write(ToString(i) + "\n")
    fileHandler.close()


def AddEntry(newEntry, _format, name="Main_list.txt"):
    """Recibe una entrada, un formato y el nombre de archivo de una lista y
    añade la nueva entrada a la lista.

    parámetros de entrada:
    newEntry -- Entrada que será agregada (dict, ver ReadFormat).
    _format -- El formato de la lista, puede ser "music", "pictures", o
    "videos."
    name -- El nombre del archivo de la lista, por defecto es "Main_list.txt,
    si se desea cambiar la lista predetermina debe escribir
    "playlists\nombre.txt".

    salida:
    No hay salida, solo modifica el archivo.
    """
    entries = ReadFormat(_format, name)
    entries.append(newEntry)
    sorted(entries, key=lambda entries: entries["name"])
    WriteList(entries, _format, name)


def DeleteEntry(entry, _format, name="Main_list.txt"):
    """Recibe una entrada, un formato y el nombre de archivo de una lista y
    elimina la entrada a la lista.

    parámetros de entrada:
    entry -- Entrada que será agregada (dict, ver ReadFormat).
    _format -- El formato de la lista, puede ser "music", "pictures", o
    "videos."
    name -- El nombre del archivo de la lista, por defecto es "Main_list.txt,
    si se desea cambiar la lista predetermina debe escribir
    "playlists\nombre.txt".

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


def ModifyList(newEntry, oldEntry, _format, name="Main_list.txt"):
    """Recibe un nuevo diccionario, un viejo diccionario, el formato, y el nombre de archivo de una lista.
    No devuelve nada, pero sobrescribe la información de la nueva entrada en la vieja entrada.

    parámetros de entrada:
    newEntry: Nueva entrada (dict, ver ReadFormat).
    oldEntry: Vieja entrada (dict, ver ReadFormat).
    _format -- El formato de la lista, puede ser "music", "pictures", o "videos."
    name -- El nombre del archivo de la lista, por defecto es "Main_list.txt,
    si se desea cambiar la lista predetermina debe escribir
    "playlists\nombre.txt."

    salida:
    No hay salida.
    """
    DeleteEntry(oldEntry, _format, name)
    AddEntry(newEntry, _format, name)


def MakePlaylist(_format, name):
    """
    Recibe el formato y el nombre de una lista de reproducción, para crear su archivo asociado.

    parámetros de entrada:
    :param _format: Formato de la lista
    :param name: Nombre del archivo, sin el txt
    :return: None
    """
    path = _format + os.sep + "playlists" + os.sep + name + ".txt"
    fileHandler = open(path, "w")
    fileHandler.close()


def DeletePlaylist(_format, name):
    """
    Recibe el formato y el nombre de una lista de reproducción, y elimina su archivo asociado.

    :param _format: Formato de la lista
    :param name: Nombre del archivo, sin el txt
    :return: None
    """
    path = _format + os.sep + "playlists" + os.sep + name + ".txt"
    os.remove(path)


def GetPlaylists(_format):
    """Recibe un formato y devuelve una lista con cadenas indicando el nombre de archivo de todas
    las playlist del formato.
    :param _format: Formato, ver ReadFormat.
    """
    path = _format + os.sep + "playlists"
    ans = []
    for root, directory, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                ans.append(file[:-4])
    return ans

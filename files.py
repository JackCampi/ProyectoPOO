"""Módulo files, maneja todo lo relacionado con los archivos y a
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
    order = ("name", "author", "album", "year", "type")
    elements = string.strip("\n").split("¬")
    entry = {}
    assert len(elements) == len(order), "Entrada inválida"
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
    "pictures\nombre.txt."

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
    :param _list: lista de diccionarios.
    :param _format: Tipo de archivo
    :param name: Nombre de archivo.
    :return: None
    """
    root = _format
    path = root + os.sep + name
    fileHandler = open(path, "w")
    for i in _list:
        fileHandler.write(ToString(i) + "\n")
    fileHandler.close()


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
    newEntry -- Entrada que será agregada (dict).
    _format -- El formato de la lista, puede ser "music", "pictures", o
    "videos."
    name -- El nombre del archivo de la lista, por defecto es "Main_list.txt,
    si se desea cambiar la lista predetermina debe escribir
    "playlists\nombre.txt."

    salida:
    No hay salida, solo modifica el archivo.
    """
    entries = ReadFormat(_format, name)
    n = GetNewPosition(newEntry, entries)
    entries.insert(n, newEntry)
    WriteList(entries, _format, name)


def DeleteEntry(entry, _format, name="Main_list.txt"):
    """Recibe una entrada, un formato y el nombre de archivo de una lista y
    elimina la entrada a la lista.

    parámetros de entrada:
    entry -- Entrada que será agregada (dict).
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


def ModifyList(newEntry, oldEntry, _format, name="Main_list.txt"):
    """Recibe un nuevo diccionario, un viejo diccionario, el formato, y el nombre de archivo de una lista.
    No devuelve nada, pero sobrescribe la información de la nueva entrada en la vieja entrada.

    parámetros de entrada:
    newEntry: Nueva entrada (dict).
    oldEntry: Vieja entrada (dict).
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
    :type _format: str
    """
    path = _format + os.sep + "playlists"
    ans = []
    for root, directory, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                ans.append(file)
    return ans


#### Tests


print(GetPlaylists("pictures"))
"""
import MainListTest

music = MainListTest.GetList()

for i in music:
    AddEntry(i, "music")

new_song = MakeEntry("all you need is love¬the beatles¬magical mystery tour¬1967¬rock")
old_song = {"name":"waiting for love","author":"avicii","album":"stories","year":2015,"type":"electronica"}
to_delete = {"name":"ajena","author":"eddy herrera","album":"atrevido","year":2001,"type":"merengue"}
ModifyList(new_song, old_song, "music")
DeleteEntry(to_delete, "music")


MakePlaylist("pictures", "musica_en_fotosxd")
for i in music:
    AddEntry(i, "pictures", "playlists\musica_en_fotosxd.txt")


for i in ReadFormat("music"):
    print(GetOrderedValue(i))

print("------------------------")
for i in ReadFormat("music"):
    print(GetNewPosition(i, ReadFormat("music")))



DeletePlaylist("pictures", "musica_en_fotosxd")
"""
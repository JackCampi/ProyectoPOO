'''Este es el módulo misceláneo, donde se encuentran diversas funciones
   referentes a la filtración de datos.'''

import MainListTest #importación de la Main_list para hacer pruebas
                    #se modificará cuando se tengan los archivos de texto
from function_files import files # importación del módulo de Juan

def SortMainList(_format, key):

    '''función que llama al método ReadFormat para obtener la Main_list
       de un formato en específico y luego se las pasa a la función
       SortList para ser ordenadas de acuerdo a una llave o criterio.
       RETURN: lista de diccionarios de toda la Main_list ordenados
       por la clave.'''

    #mainList = MainListTest.GetList() # llamada a la Main_list de prueba
    mainList = files.ReadFormat(_format) # función creada por Juan
    return SortList(mainList, key)

def SortList(_list, key):

    '''función que recibe una lista, bien sea la Main_list o una playlist
       y la filtra por una clave elegida en el menú.
       RETURN: lista de diccionarios de los elementos en Main_list
       organizados por clave.'''

    try:
        return sorted(_list, key = lambda _dict : _dict[key])
    except:
        raise NameError("Invalid key, please check if the key is correct")
        #si la clave dada es erronea se levanta un error

def SearchMainList(_format, item):

    '''función que llama al método ReadFormat para obtener la Main_list
       de algún formato y un item para llamar a la función SearchItemInDict
       y buscar el elemento.
       RETURN: lista de diccionarios que coincidan con la búsqueda.
       NOTA: busca tanto en nombre como en álbum, autor, año, etc...'''

    #mainList = SortMainList("music","name") # esto llama a la Main_list de prueba
    mainList = files.ReadFormat(_format) # función creada por Juan
    return SearchItemInDict(mainList, item)

def SearchItemInDict(_list, item):

    '''item: string que se quiere buscar en el diccionario.
       esta función que buca elemento por elemento en todas las llaves de un
       diccionario si un item coincide con lo guardado en los diccionarios.
       la función va guardando todas las coincidencias que encuentre y luego
       llama a la función CleanList para deshacerse de los elementos repetidos.
       RETURN: devuelve una lista de diccionarios ordenados por nombre, donde
       en alguna de sus llaves coincida el item buscado.'''

    elementsFound = []
    if len(_list) == 0: #primero checkea que la lista no este vacia
        return elementsFound
    for key in _list[0].keys(): #recorre todas las llaves del diccionario
        for i in range(len(_list)):
            if item in _list[i][key]:
                elementsFound.append(_list[i])
    cleanedList = CleanList(elementsFound) #elimina elementos repetidos
    cleanedSoartedList = SortList(cleanedList, "name") #organiza el resultado por nombres
    return cleanedSoartedList

def CleanList(_list):

    '''función que recibe una lista y elimina todos los elementos repetidos.
       RETURN: lista sin elementos repetidos.'''

    cleanedList = []
    for i in range(len(_list)):
        if _list[i] not in cleanedList:
            cleanedList.append(_list[i])
    return cleanedList

def SearchItemInList(_list, item):

    '''función que recibe una lista de strings y un item (string) que desea
       buscar dentro de la lista. recorre elemento por elemento y guarda los
       elementos donde coincida el item.
       RETURN: lista de todas las coincidencias.'''

    soartedList = sorted(_list)
    elementsFound = []
    for i in range(len(soartedList)):
        if item in soartedList[i]:
            elementsFound.append(soartedList[i])
    return elementsFound


'''-------------------------------------BETA---------------------------------------------------------
                    Aquí encontrarás funciones en fase beta que por el momento
                    no son utilizadas en el fucionamiento del programa pero que
                    en un futuro pueden servir.
                    NOTA: algunas no son del todo funcionales. Se retomará
                    cuando sean requeridas.'''

def BinarySearchInList(_list, item):

    '''FASE BETA: función que recibe una lista de elemntos y realiza
       una búsqueda binaria hasta encontrar la primera coincidencias
       FALTA: que revise si a los lados tambien se encuentran elementos
       que coincidan con la búsqueda'''

    _list.sort()
    first = 0
    last = len(_list)-1
    elementsFound = []
    found = False
    while first <= last and not found:
        middle = (first + last) // 2
        if _list[middle] == item:
            elementsFound.append(_list[middle])
            found = True
        else:
            if item < _list[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return elementsFound

def BinarySearch(_list, item):

    '''función que recibe una lista y un item para buscar en dicha lista
       se realiza una búsqueda binaria en cada una de las llaves
       y cuando se encuentre la primera coincidencia se llama dos
       métodos para comprobar si hay más elementos que coincidan
       RETURN: lista de diccionarios que coincidan con la búsqueda
       NOTA: busca tanto en nombre como en álbum, autor, año, etc...
       NOTA2: se descontinuó la función porque solo funciona si el item
       coincide al 100% con los elementos de los diccionario y no
       funciona si solo se pone un pedazo. Se cambió por la función
       SearchItemInDict.'''

    elementsFound = []
    for key in _list[0].keys(): # recorre la lista mirando cada una de las llaves
        soartedList = SortList(_list, key) #organiza la lista de acuerdo a la llaves
        first = 0                          #para realizar la búsqueda bien
        last = len(soartedList)-1
        found = False
        while first <= last and not found:
            middle = (first + last) // 2
            if soartedList[middle][key] == item: #entra cuando se encontro la primera coincidencia
                sameItemRight = CheckRight(soartedList, middle, item, key)
                                #revisa cuantos elementos a la derecha de _lista también coinciden
                sameItemLeft = CheckLeft(soartedList, middle, item, key)-1
                                #revisa cuantos elementos a la derecha de _lista tambien coinciden
                elementsFound = soartedList[middle-sameItemLeft:middle+sameItemRight]
                                #solo toma el intervalo de _list donde coincide la búsqueda
                found = True #rompe con el bucle y se va a la siguiente clave
            else: # acorta el intervalo de búsqueda
                if item < soartedList[middle][key]:
                    last = middle - 1
                else:
                    first = middle + 1
    return elementsFound

def CheckRight(_list, index, item, key):

    '''función que revisa índice por índice si los elementos
       a la derecha de la primera coincidencia también coinciden.
       RETURN: int del numero de elementos a la derecha
       que coinciden con la búsqueda.
       NOTA: función exclusiva para el fucionamiento de BinarySearch.'''

    if _list[index][key] != item:
        return 0
    else:
        if index == len(_list)-1:
            return 1
        else:
            return 1 + CheckRight(_list, index + 1, item, key)

def CheckLeft(_list, index, item, key):

    '''función que revisa índice por índice si los elementos
       a la izquierda de la primera coincidencia también coinciden
       RETURN: int del número de elementos a la izquierda.
       que coinciden con la búsqueda.
       NOTA: función exclusiva para el fucionamiento de BinarySearch.'''

    if _list[index][key] != item:
        return 0
    else:
        if index == 0:
            return 1
        else:
            return 1 + CheckLeft(_list, index - 1, item, key)

'''---------------------------ZONA DE PRUEBAS----------------------------------------------------------
    aquí se realizan pruebas para ver si todo funciona correctamente,
    se borrará cuando todo este listo'''

#playlists = ["playlist", "playlist2", "main", "salsa", "rumba"]

#print(SortMainList("music","name"))
'''for i in SortMainList("music", "type"):
    print(i)'''
#print(SearchMainList("music", "pop"))
'''for i in SearchMainList("music", "19"):
    print(i)'''
#print(SearchItemInList(playlists, "p"))

'''Este es el módulo miselaneo donde se encuentran diversas funciones
   referentes a la filtración de datos'''

#import MainListTest #importación de la Main_list para hacer pruebas
                    #se modificará cuando se tengan los archivos de texto
import files # importación del módulo de Juan

def SortMainList(_format, key):

    '''fución que llama al método ReadFormat para obtener la Main_list
       de un formato en específico y luego se las pasa a la función
       SortList para ser ordenadas de acuerdo a una llave o criterio.
       RETURN: lista de diccionarios de toda la Main_list ordenados
       por la clave.'''

    #mainList = MainListTest.GetList() # llamada a la Main_list de prueba
    mainList = files.ReadFormat(_format) # fución creada por Juan
    return SortList(mainList, key)

def SortList(_list, key):

    '''fución que recibe una lista, bien sea la Main_list o una playlist
       y la filtra por una clave elegida en el menú.
       RETURN: lista de diccionarios de los elementos en Main_list
       organizados por clave'''

    try:
        return sorted(_list, key = lambda _dict : _dict[key])
    except:
        raise NameError("Invalid key, please check if the key is correct")
        #si la clave dada es erronea se levanta un error

def SearchMainList(_format, item):

    '''fución que llama al método ReadFormat para obtener la Main_list
       de algún formato y un item para llamar a la fución BinarySearch
       y buscar el elemento
       RETURN: lista de diccionarios que coincidan con la busqueda
       NOTA: busca tanto en nombre como en álbum, autor, año, etc...'''

    #mainList = SortMainList("music","name") # esto llama a la Main_list de prueba
    mainList = files.ReadFormat(_format) # fución creada por Juan
    return BinarySearch(mainList, item)

def BinarySearchInList(_list, item):
    _list.sort()
    first = 0
    last = len(_list)-1
    elementsFound = []
    found = False
    while first <= last and not found:
        middle = (first + last) // 2
        if _list[middle] == item:
            elementsFound.append(_list[middle])
        else:
            if item < _list[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return elementsFound

def BinarySearch(_list, item):

    '''fución que recibe una lista y un item para buscar en dicha lista
       se realiza una busqueda binaria en cada una de las llaves
       y cuando se encuentre la primera coincidencia se llama dos
       métodos para comprobar si hay más elementos que coincidan
       RETURN: lista de diccionarios que coincidan con la busqueda
       NOTA: busca tanto en nombre como en álbum, autor, año, etc...'''

    elementsFound = []
    for key in _list[0].keys(): # recorre la lista mirando cada una de las llaves
        soartedList = SortList(_list, key) #organiza la lista de acuerdo a la llaves
        first = 0                          #para realizar la busqueda bien
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
                                #solo toma el intervalo de _list donde coincide la busqueda
                found = True #rompe con el bucle y se va a la siguiente clave
            else: # acorta el intervalo de busqueda
                if item < soartedList[middle][key]:
                    last = middle - 1
                else:
                    first = middle + 1
    return elementsFound

def CheckRight(_list, index, item, key):

    '''fución que revisa índice por índice si los elementos
       a la derecha de la primera coincidencia también coinciden
       RETURN: int del numero de elementos a la derecha
       que coinciden con la busqueda
       NOTA: fución exclusiva para el fucionamiento de BinarySearch'''

    if _list[index][key] != item:
        return 0
    else:
        if index == len(_list)-1:
            return 1
        else:
            return 1 + CheckRight(_list, index + 1, item, key)

def CheckLeft(_list, index, item, key):

    '''fución que revisa índice por índice si los elementos
       a la izquierda de la primera coincidencia también coinciden
       RETURN: int del numero de elementos a la izquierda
       que coinciden con la busqueda
       NOTA: fución exclusiva para el fucionamiento de BinarySearch'''

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

#print(SortMainList("music","name"))
'''for i in SortMainList("music", "type"):
    print(i)'''
#print(SearchMainList("music", "pop"))
'''for i in SearchMainList("music", "pop"):
    print(i)'''

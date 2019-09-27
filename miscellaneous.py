'''Este es el módulo moselaneo donde se encuentran diversas funciones
   referentes a la filtración de datos'''
import prueba

def SortMainList(_format, key):

    mainList = prueba.GetList()
    #mainList = readFortmat(_format)
    return SortList(mainList, key)

def SortList(_list, key):

    try:
        return sorted(_list, key = lambda _dict : _dict[key])
    except:
        raise NameError("Invalid key, please check if the key is correct")

def SearchMainList(_format, name):

    mainList = SortMainList("music","name")
    #mainList = readFortmat(_format)
    return BinarySearch(mainList, name)

'''def BinarySearch(_list, name):
    first = 0
    last = len(_list)-1
    elementsFound = []
    #return 34
    while first <= last:
        middle = (first + last) // 2
        if _list[middle]["name"] == name:
            elementsFound.append(_list[middle])
            first = middle + 1
        else:
            if name < _list[middle]["name"]:
                last = middle - 1
            else:
                first = middle + 1
    return elementsFound'''
def BinarySearch(_list, item):
    elementsFound = []
    for key in _list[0].keys():
        first = 0
        last = len(_list)-1
        while first <= last:
            middle = (first + last) // 2
            if _list[middle][key] == item:
                elementsFound.append(_list[middle])
                first = middle + 1
            else:
                if item < _list[middle][key]:
                    last = middle - 1
                else:
                    first = middle + 1
    return elementsFound

#print(SortMainList("music","type"))
print(SearchMainList("music", "thriller"))

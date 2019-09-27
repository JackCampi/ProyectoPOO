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

def Search(_format, name):

    mainList = SortMainList("music","name")
    #mainList = readFortmat(_format)
    item = BinarySearch(mainList, name)
    return item

def BinarySearch(_list, name):
    first = 0
    last = len(_list)-1
    found = False
    #return 34
    while first <= last and not found:
        middle = (first + last) // 2
        if _list[middle]["name"] == name:
            found = True
        else:
            if name < _list[middle]["name"]:
                last = middle - 1
            else:
                first = middle + 1
    return found

#print(SortMainList("music","name"))
print(Search("music", "demons"))

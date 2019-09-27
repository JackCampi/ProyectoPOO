'''Este es el módulo moselaneo donde se encuentran diversas funciones
   referentes a la filtración de datos'''
import prueba

def SortList(_format, key):

    mainList = prueba.GetList()
    #mainList = readFortmat(_format)
    try:
        return sorted(mainList, key = lambda _dict : _dict[key])
    except:
        raise NameError("Invalid key, please check if the key is correct")

def Search(_format, name):

    mainList = SortList("music","name")
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

print(SortList("music","name"))
print(Search("music", "demons3"))

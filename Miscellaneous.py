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

def BinarySearch(_list, item):
    elementsFound = []
    for key in _list[0].keys():
        soartedList = SortList(_list, key)
        first = 0
        last = len(soartedList)-1
        found = False
        while first <= last and not found:
            middle = (first + last) // 2
            if soartedList[middle][key] == item:
                sameItemRight = CheckRight(soartedList, middle, item, key)
                sameItemLeft = CheckLeft(soartedList, middle, item, key)-1
                elementsFound = soartedList[middle-sameItemLeft:middle+sameItemRight]
                found = True
            else:
                if item < soartedList[middle][key]:
                    last = middle - 1
                else:
                    first = middle + 1
    return elementsFound

def CheckRight(_list, index, item, key):
    if _list[index][key] != item:
        return 0
    else:
        if index == len(_list)-1:
            return 1
        else:
            return 1 + CheckRight(_list, index + 1, item, key)

def CheckLeft(_list, index, item, key):
    if _list[index][key] != item:
        return 0
    else:
        if index == 0:
            return 1
        else:
            return 1 + CheckLeft(_list, index - 1, item, key)

#print(SortMainList("music","type"))
'''for i in SortMainList("music", "type"):
    print(i)'''
#print(SearchMainList("music", "pop"))
for i in SearchMainList("music", "beat it"):
    print(i)

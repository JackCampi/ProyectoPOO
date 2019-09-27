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
                #Clean(elementsFound)
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
        #answer.append(_list[index])
        #answer.append(CheckSides(_list, index + 1, item, key, answer))

        #return list(_list[index]) + list(CheckSides(_list, index + 1, item, key)) + list(CheckSides(_list, index - 1, item, key))
        #return list(_list[index]).append(CheckSides(_list, index + 1, item, key)) #+ list(CheckSides(_list, index - 1, item, key))
        #print(key, item, index)
        #print(_list)
        if index == len(_list)-1:
            return 1
        else:
            return 1 + CheckRight(_list, index + 1, item, key) #+ CheckSides(_list, index - 1, item, key)

def CheckLeft(_list, index, item, key):
    if _list[index][key] != item:
        return 0
    else:
        #answer.append(_list[index])
        #answer.append(CheckSides(_list, index + 1, item, key, answer))

        #return list(_list[index]) + list(CheckSides(_list, index + 1, item, key)) + list(CheckSides(_list, index - 1, item, key))
        #return list(_list[index]).append(CheckSides(_list, index + 1, item, key)) #+ list(CheckSides(_list, index - 1, item, key))
        #print(key, item, index)
        #print(_list)
        if index == 0:
            return 1
        else:
            return 1 + CheckLeft(_list, index - 1, item, key) #+ CheckSides(_list, index - 1, item, key)

def Clean(_list):
    for i in range(len(_list)-1):
        if type(_list[i]) != type({}) or _list[i] == {}:
            #.remove(_list[i])
            _list.pop(i)
#print(SortMainList("music","type"))
'''for i in SortMainList("music", "type"):
    print(i)'''
#print(SearchMainList("music", "pop"))
for i in SearchMainList("music", "no 6 collaborations project"):
    print(i)

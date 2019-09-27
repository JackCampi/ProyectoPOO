'''Este es el módulo moselaneo donde se encuentran diversas funciones
   referentes a la filtración de datos'''
import prueba

def SortList(_format, key):
    print("hola")
    mainList = prueba.GetList()
    #mainList = readFortmat(_format)
    return sorted(mainList, key = lambda _dict : _dict[key])

print(SortList("music","name2"))

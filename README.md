# ProyectoPOO

### Fantastic bugs and where to find them

Si no se puede eliminar bugs cuando se descubren inmediatamente es
recomendable escribirlos aquí para eliminarlos después, importantísimo
escribir los pasos y lo que dice el python para poder reproducir el 
error correctamente.

1. la opción mis listas del menú listas de reproduccion me lleva la mismo menú en buble
 Pasos: (1, 2, 1, 1)
 
 
1. Falta código
    
    Pasos: (1, 1, 1, 1)
    
	*TypeError: SortListMenu() missing 1 required positional argument: 'listName'*


2. No hace nada al buscar una lista existente 

    Pasos: (1, 2, 3, NOMBRE_EXISTENTE)
	
	**Se queda colgado**

3. No elimina listas si no son seleccionadas antes 

    Pasos: (1, 2, 4, NOMBRE)
	
	**Se queda colgado**

4. Directorio equivocado al añadir playlists 

    Pasos: (1, 2, 1, 1, 1, 3)
    
	*FileNotFoundError: [Errno 2] No such file or directory: 'music\\playlist\\1.txt'*

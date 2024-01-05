#Buscamos el valor x en una lista llamada my_list:
def search(x, my_list):
    for k in range(len(my_list)):
        if my_list[k] == x:
            return k
    return -1

nums = [6, 7, 3, 42, 9]
print(search(42, nums))#  indice(posicion)= 3

#Aquí iteramos a través de la lista usando un bucle for y buscamos una
#coincidencia. Si el elemento actual es igual a x, se devuelve el
#índice de ese elemento.

#Se devuelve -1 si no se encuentra ninguna coincidencia.
#Implementemos una clase Cola con sus correspondientes métodos
#enqueue, dequeue, is_empty y print.

#Usaremos una lista para almacenar los elementos.
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def print_queue(self):
        print(self.items)

q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('42')
q.print_queue()

q.dequeue()
q.print_queue()

#El método enqueue añade un elemento al principio de la lista,
#mientras que el método dequeue elimina el último elemento.

print("------------------------")

cola = ["Mike","Dave","Mary","Alex"]
#         0      1      2      3

#Agregando elementos al final de la cola:
cola.append("Bruno")
cola.append("Charles")
print(cola)

#Quitando elementos por el principio de la cola:
n = cola.pop(0)
print(f"{n} salio de la cola")
n = cola.pop(0)
print(f"{n} salio de la cola")

print(cola)

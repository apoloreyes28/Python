#Cada elemento (lo llamaremos nodo) de una lista enlazada consta
#de dos elementos: los datos y una referencia al siguiente nodo.

#El último nodo tiene una referencia a nulo(NULL). El punto de entrada
#a una lista enlazada se denomina encabezado(head) de la lista.

#Comencemos creando la clase de nodo:
class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next

#Ahora podemos crear la clase LinkedList con los métodos correspondientes:
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

# función para agregar un nodo al frente
    def add_at_front(self, data):
        self.head = Node(data, self.head)

# función para agregar nodo al final
    def add_at_end(self, data):
        if not self.head:
            self.head = Node(data, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)

# función para eliminar cualquier nodo
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

# función para obtener el último nodo
    def get_last_node(self):
        n = self.head
        while (n.next != None):
            n = n.next
        return n.data

# función para comprobar si la lista está vacía
    def is_empty(self):
        return self.head == None

# función para imprimir los nodos de la lista
    def print_list(self):
        n = self.head
        while n != None:
            print(n.data, end=" => ")
            n = n.next
        print()

s = LinkedList()
s.add_at_front(5)
s.add_at_end(8)
s.add_at_front(9)

s.print_list()
print(s.get_last_node())

#El método add_at_front() añade un nuevo nodo como cabeza de la lista
#y enlaza la cabeza anterior con él.
#El método add_at_end() itera hasta el final de la lista usando un
#bucle while y añade el nuevo nodo como enlace del último nodo.
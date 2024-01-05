#Vamos a definir e implementar la clase Stack con sus
#correspondientes métodos: push, pop, is_empty and print_stack .

#Usaremos una lista para almacenar los datos.
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def print_stack(self):
        print(self.items)

s = Stack()
s.push('a')
s.push('b')
s.push('c')
s.print_stack()

s.pop()
s.print_stack()

print("------------------------")

pila = [1,2,3]

#Agregamos elementos por el final de la pila:
pila.append(4)
pila.append(5)
print(pila)

#Quitando elementos por el final de la pila:
n = pila.pop()
print(f"Sacando el elemento: {n}")# 5
n = pila.pop()
print(f"Sacando el elemento: {n}")# 4

print(pila)

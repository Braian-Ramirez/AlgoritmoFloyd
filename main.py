# Definimos la clase Nodo para representar nodos de una lista enlazada
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def __repr__(self) -> str:
        return f"<Nodo{self.valor}>"

# Creamos cinco nodos (Complejidad: O(1))
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)

# Crear una lista enlazada con ciclo (Complejidad: O(1))
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5
nodo5.siguiente = nodo2

# Crear una lista enlazada sin ciclo (Complejidad: O(1))
nodo1_no_ciclo = Nodo(1)
nodo2_no_ciclo = Nodo(2)
nodo3_no_ciclo = Nodo(3)
nodo4_no_ciclo = Nodo(4)
nodo5_no_ciclo = Nodo(5)

nodo1_no_ciclo.siguiente = nodo2_no_ciclo
nodo2_no_ciclo.siguiente = nodo3_no_ciclo
nodo3_no_ciclo.siguiente = nodo4_no_ciclo
nodo4_no_ciclo.siguiente = nodo5_no_ciclo

# Función para buscar un ciclo en una lista enlazada (Complejidad: O(n), donde 'n' es el número de nodos)
def buscar_ciclo(lista):
    liebre = lista
    tortuga = lista

    while liebre and tortuga and liebre.siguiente:
        liebre = liebre.siguiente.siguiente
        tortuga = tortuga.siguiente

        if liebre == tortuga:
            print("Ciclo detectado:", liebre, tortuga)
            return True

    return False

# Comprobamos si hay un ciclo en la lista enlazada con ciclo
print("Lista con ciclo:")
ciclo_detectado = buscar_ciclo(nodo1)
if not ciclo_detectado:
    print("No se encontró ciclo en la lista.")

# Comprobamos si hay un ciclo en la lista enlazada sin ciclo
print("\nLista sin ciclo:")
ciclo_detectado = buscar_ciclo(nodo1_no_ciclo)
if not ciclo_detectado:
    print("No se encontró ciclo en la lista sin ciclo.")

# Función para buscar un número repetido en una lista (Complejidad: O(k), donde 'k' es la longitud de la lista 'nums')
def buscar_numero_repetido(nums):
    numeros_vistos = set()

    for num in nums:
        if num in numeros_vistos:
            return num
        numeros_vistos.add(num)

# Llamamos a la función para buscar un número repetido en la lista 'nums'
nums = [1, 3, 4, 2, 0, 7, 8, 8]
numero_repetido = buscar_numero_repetido(nums)

# Imprimimos el número repetido y su posición si se encuentra
if numero_repetido is not None:
    print(f"El número que se repite es: {numero_repetido}")
    posicion = nums.index(numero_repetido)  # (Complejidad: O(k))
    print(f"La posición del valor que se repite es: {posicion}")
else:
    print("No se encontró ningún número repetido en la lista.")


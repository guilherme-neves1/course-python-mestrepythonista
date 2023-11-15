# SET => Valores únicos na lista

'''
numeros = [2, 2, 5, 8]
frutas = ['maça', 'uva', 'banana', 'maça', 'morango']

# Convertendo para SET e removendo a repetição
set_numeros = set(numeros)
set_frutas = set(frutas)

print(set_numeros)
print(set_frutas)

# Adicionando novos valores
set_numeros.add(10)
print(set_numeros)
'''

# Conjuntos
numeros1 = [2, 2, 5, 8]
numeros2 = [2, 2, 3, 9]

a = set(numeros1)
b = set(numeros2)

# Excluir os iguais entre as listas
print(a.symmetric_difference(b))

# Mostrar o valor igual entre elas
print(a.intersection(b))

# Unir as listas removendo os itens duplicados
print(a.union(b))

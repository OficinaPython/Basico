#adicionando elementos na lista
listamercado = ["ovos","leite","frango","chocolate"]
listamercado.append('carne') #append adiciona elementos no final lista
print('Adicionando elementos na lista: ',listamercado)

print('\n')

#O metodo extend adiciona elementos na lista porem ele se comporta diferente do append
listamercado = ["ovos","leite","frango","chocolate"]
listamercado.extend('ameixa')
listamercado.append('uvapassa')
print(listamercado)

print('\n')

#O metodo insert adiciona elementos em uma lista em uma posição especifica
listamercado = ["ovos","leite","frango","chocolate"]
listamercado.insert(1,800)#na posição 1 vai aparecer o numero '800'
print(listamercado)

print('\n')

'''#Deletando elementos de uma lista
del listamercado[1]
print(listamercado)'''

print('\n')

#usando o metodo pop, ele apaga o ultimo elemento da lista, mas tambem é possivel definir umelemento

listamercado = ["ovos","leite","frango","chocolate"]
listamercado.pop()
print('Apagando elementos da lista usando o metodo pop: ',listamercado)

print('\n')

#metodo remove:remove elementos da lista, voce indica o valor aser eliminado e nao o indice

listamercado = ["ovos","leite","frango","chocolate"]
listamercado.remove('frango')
print('Removendo elementros usando o remove: ',listamercado)

print('\n')

#trocando elementos de uma lista
listamercado = ["ovos","leite","frango","chocolate"]
listamercado[2] = 'PAO'#aqui a palavra frango foi trocada pela palavra PAO
print('Trocando elementos da lista: ',listamercado)

print('\n')

#listas aninhadas
lista = [1,5,7,8],[5,8,9],[9,6,3,0]
print(lista)
a = lista
print('Listas aninhadas: ',a)

print('\n')

#somando listas
lista1= [5,8,9]
lista2 = [8,6,9]
listatotal = lista1 + lista2#houve uma concatenação das listas 1 e 2
print('Somando listas: ',listatotal)

print('\n')

#Metodo index localiza e informa a posição de determinado elemento na lista
listamercado = ["ovos","leite","frango","uva"]
print(listamercado.index('uva'))#a palavra uva esta na posição 3

print('\n')

#Metodo reverse: inverte elementos da lista

lista_exemplo1 = ['chocolate','pera','uva']
lista_exemplo1.reverse()#inverteu a ordem da lista
print(lista_exemplo1)

print('\n')

#Metodo sort ordena a lista em ordem numerica
lista_num = [4,8,3,6,9,7]
lista_num.sort()
print(lista_num)

#para fazer a ordem inversa dos elementos da lista, basta usarmos o parametro 'reverse=True'

lista_num = [1,2,3,4,5,6,7,8,9]
lista_num.sort(reverse=True)
print(lista_num)


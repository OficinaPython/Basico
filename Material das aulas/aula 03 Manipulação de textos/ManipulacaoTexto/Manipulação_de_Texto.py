'''
MATERIAL DE APOIO: Manipúlação de textos
'''

                                    #Analise

teste = 'Programar em Python é Muito Legal e Divertido! ' #definindo uma string

print(len(teste)) #a função len é derivada da palavra lenght que significa comprimento
                  #ela mede o tamanho da string, ou seja, quantos caracteres a mesma possui

#a função count conta quantas vezes uma determinada letra aparece na farse
exemplo2 = teste.count('a')
print(exemplo2)

#find informa posição em que a letra ou palavra especificada se encontra
exemplo3 = teste.find('Muito')
print(exemplo3) #neste exemplo a palavra 'muito' aparece primeiro na posição 22

#o In verifica se a palavra 'legal' está dentro da String 'teste'
exemplo4 = 'legal' in teste
print(exemplo4)

                                #Transformação

#a função replace troca uma string por outra
exemplo1 = teste.replace('Legal','BOMMM')
print(exemplo1)

#A função Upper transforma todas as letras da String em maiusculas
exemplo5 = teste.upper()
print(exemplo5)

#A função Lower faz justamente o contrario, coloca todas as letras em minusculas
exemplo6 = teste.lower()
print(exemplo6)

#A função capitaliza deixa todas as letras da frase em minusculas menos a primeira letra
exemplo7 = teste.capitalize()
print(exemplo7)

#A função Tittle analiza quantas palavras tem na frase com base nos espaços
#logo em seguida ele deixa as palavras que foram separadas com a primeira letra em maiusculas
print('tittle aki',teste.title())

#A função Strip tira os espaços antes e depois da string
string = '     Casa Amarela      '
print('A palavra tem um tamanho de {} '.format(len(string.strip())))
#Note que foi usado a função len juntamente com a função strip, ou seja, a função len
#esta medindo o tamanho da frase sem os espaços, pois a função strip tirou o espaços antes e depois


                                #Divisao

#a função split divide a frase com base nos espaços entre as palavras e coloca cara palavra em um novo indice
exemplo9 = teste.split()
print(exemplo9)

                                #Junção

#a função join junta as palavras da frase
print(' '.join(teste))

                                #Fatiamento

#O fatiamento de string é realizado atravez dos []

#temos um padrao a ser seguido

# [inicio da frase a ser fatiada : Até aonde a frase vai ser fatiada : parametro para o fatiamento]

#veja que aqui estou apenas pegando apenas a letra que esta na posição 3
fatiamento = 'Eu vou ser a frase fatiada '
print(fatiamento[3])

#aqui estrou pegando a letra na posição 3 e indo até o final da frase
print(fatiamento[3:])

#neste exemplo note que n foi informado nenhum parametro antes dos ':' logo ele pega a letra na posição 0 até a 8
print(fatiamento[:8])

#Neste exemplo nao estou informando nenhum parametro, logo ele pega da letra na posição 0 até o final da frase
print(fatiamento[:])

#neste exemplo estou pulando de 2 em 2 e a cada pulo estou pegando apenas uma letra
print(fatiamento[::2])

#quase igual ao exemplo de cima, estou pulando de 2 em 2 porem estou indo da posição 0 a posição 10 da frase
print(fatiamento[0:10:2])
# #1 - Maior temperatura (sem usar max) - 
# # Com a lista temperaturas = [22, 31, 27, 35, 19], 
# # use um for para descobrir a maior temperatura.

print()
print('Exercicio 1')
print()

temperaturas = [22, 31, 27, 35, 19]
contador_temp = 0

for temp_item in temperaturas:
    if temp_item > contador_temp:
        contador_temp = temp_item
        
print("A maior temperatura é:", contador_temp, end= "°C")
print()

#end é similar a sep. Ele faz tal parte de texto aparecer no final.

#2 - Palavras longas - Com a lista `palavras = ["sol", "computador", "casa", "python", "janela"]`, 
# conte quantas palavras têm mais de 5 letras (use `len`).

print()
print('Exercicio 2')
print()

palavras = ["sol", "computador", "casa", "python", "janela"]
contador_pal = 0

for palavra in palavras:
    if len(palavra) > 5:
        contador_pal = contador_pal + 1
print("O numero de palavras com mais de 5 letras são:", contador_pal, end= " palavras!")
print()

#3 - Achar a Ana - Com a lista nomes = ["Ana", "Bruno", "Carla", "Ana"],
#  use um for e um if para mostrar na tela o nome sempre que ele for igual a “Ana”.
print()
print('Exercicio 3')

contador_ana = 0
nomes = ["Ana", "Bruno", "Carla", "Ana"]
for elemento in nomes:
    if elemento == ("Ana"):
        contador_ana = (contador_ana + 1)
    if contador_ana == 2:
        print()
        print("Encontrei a Ana duas vezes!")

#Script feito para deixar mais bonito a apresentação. Para fazer como o enunciado, deveria ser o seguinte:
# Remova o contador_ana, e faça a seguinte linha:
# for elemento in nomes:
#    if elemento == ("Ana"): 
# print('Encontrei a Ana!') ou só print(elemento).

#4 - Achar o Pedro - Com a lista nomes = ["Lucas", "Pedro", "Julia", "Marcos"], 
# use um for e um if para mostrar a mensagem Achei o Pedro! quando encontrar o nome “Pedro”.

print()
print('Exercicio 4')
print()

nomes2 = ["Lucas", "Pedro", "Julia", "Marcos"]
for item in nomes2:
    if item == ("Pedro"):
        print("Achei o Pedro!")

#5 - Contar Joãos - Com a lista nomes = ["João", "Maria", "João", "Paula"], 
# use um for, um if e uma variável contador começando em 0 
# para contar quantas vezes “João” aparece e mostre o total no final.

print()
print('Exercicio 5')
print()

nomes3 = ["João", "Maria", "João", "Paula"]
contador = 0

for nome in nomes3:
    if nome == ("João"):
        contador = (contador + 1)

print("O numero de vezes que João aparece na lista é:", contador, end=" vezes!")
print()

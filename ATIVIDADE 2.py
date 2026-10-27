# Solicitar nome do usuario 

nome = input('Digite o seu nome: ')

print('Bem-vindo,',nome)

print()

#1 - Pergunte ao usuário quais são seus três hobbies favoritos. 
# Depois, exiba uma mensagem listando esses hobbies.

lista_hobby1 = input('Bem-vindo ao clube, qual o seu hobby favorito? Liste tres, comecando pelo primeiro: ')
lista_hobby2 = input('Seu segundo hobby: ' )
lista_hobby3 = input('Seu terceiro hobby: ')

print('Entendido! Eles sao:')
print ('Hobby 1:', lista_hobby1)
print ('Hobby 2:', lista_hobby2)
print ('Hobby 3:', lista_hobby3)
print ('Obrigado!')

#2 - Peça ao usuário que informe 
# três destinos de viagem dos seus sonhos. 
# Depois, exiba os destinos escolhidos.

lista_viagem1 = input('Porfavor, liste lugares de interesse: ')

#TESTE DE SOMATORIA

#Input sempre retorna tipo texto

#Teste: Receba do usuario dois numeros e imprima soma

numero1 = int(input('informe o primeiro numero: '))
numero2 = int(input('informe o segundo numero: '))

soma = numero1 + numero2

print('A soma e: ', soma)
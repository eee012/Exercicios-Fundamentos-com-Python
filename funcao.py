print('\n', 'Exercicio 1', '\n')

nome1 = input('Informe o seu nome: ')
nome2 = input('Informe o seu nome: ')
nome3 = input('Informe o seu nome: ')

def boas_vindas(nome):
    return('Boas vindas ao curso, ' + nome)

print ((boas_vindas)(nome1))
print ((boas_vindas)(nome2))
print ((boas_vindas)(nome3))

print('\n', 'Exercicio 2', '\n')

num1 = input('Informe o seu numero: ')
num2 = input('Informe o seu numero: ')

def dobro(numero):
    return numero*2

print(dobro(int(num1)))
print(dobro(int(num2)))

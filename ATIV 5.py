# - Crie um programa de login. 
# Peça usuário e senha. 
# Se o usuário for "aluno" a senha for "1234", mostre "Login realizado". 
# Caso contrário, mostre "Usuário ou senha incorretos".

print('Exercicio 1')
print()

user_name = input('Digite seu usuario: ')
user_pwd = int(input('Digite sua senha: '))

if user_name == 'aluno' and user_pwd == int('1234'):
    print('Login realizado.')
else:
    print('Usuario ou senha incorreto.')

#- Peça ao usuário o dia da semana (ex.: sabado). 
# Se for "sabado" "domingo", mostre "Fim de semana!".
#  Caso contrário, mostre "Dia útil".

print()
print('Exercicio 2')
print()

day_week = input('Digite o seu dia da semana: ')

if day_week == 'sabado' or day_week == 'domingo':
    print('Fim de semana!')
else:
    print('Dia util.')

#3 - Crie a variável bateria_carregada = False. 
# Se a bateria estiver carregada, mostre "Conecte o carregador".
#  Caso contrário, mostre "Bateria ok". 
# Depois troque para True e veja a diferença.

print()
print('Exercicio 3')
print()

bateria_carregada = False

if not bateria_carregada == True:
    print('Conecte o carregador')
else:
    print('Carregando. . . ')

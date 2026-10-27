#1 - Escreva um programa que continue pedindo ao usuário para digitar a senha correta até que ele acerte. 
# Quando a senha correta for inserida, o programa deve exibir uma mensagem de sucesso e encerrar.

print('\n', 'Exercicio 1', '\n')

senha = input('Bem vindo! Digite sua senha:')
while senha != 'senha':
    print('Senha incorreta. Tente novamente!')
    senha = input('Digite sua senha:')

    if senha == 'senha':
        print('Senha correta! Finalizando..')

#2 - Peça ao usuário para adivinhar um número entre 1 e 20. O loop continuará até que o usuário acerte o número. 
# Informe ao usuário se o palpite foi maior ou menor que o número correto.

# **Dica:** Defina um número secreto e compare os palpites do usuário com esse número.

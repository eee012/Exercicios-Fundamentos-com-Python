#1 - Frete por peso - Peça o peso do pacote em kg. 
# Até 1 kg o frete é R$ 10; até 5 kg é R$ 20; acima de 5 kg é R$ 35.
#  Mostre o valor do frete.

#2 - Menu do banco - Mostre as opções 1 - Saldo, 2 - Extrato, 3 - Sair. 
# Peça a opção e mostre a mensagem correspondente. Se digitar outra coisa,
#  mostre "Opção inválida".

print('Exercicio 1')
print()

valor_frete = int(input('Diga o peso do pacote em KG: '))

if valor_frete == 1:
    print('RS10')

elif valor_frete >= 2 and valor_frete <= 5:
    print('RS20')

elif valor_frete >= 6:
    print('RS35')

print()
print('Exercicio 2')
print()

print('Menu do Banco:\n1 - Saldo\n2 - Extrato\n3 - Sair')
opcao_banco = int(input())

if opcao_banco >= 4:
    print('Opcao Invalida!')

elif opcao_banco == 1:
    (print('RS2010.15'))

elif opcao_banco == 2:
    print('Mostrando Extrato..')

elif opcao_banco == 3: 
    print('Obrigado!')

else:
    print('Opcao Invalida!')

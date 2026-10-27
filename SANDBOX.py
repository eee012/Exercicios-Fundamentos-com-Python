print()
print('Bem vindo a lista!')
primeiro_item = input('Porfavor, digite o primeiro item ' )
segundo_item = input('O segundo item ' )
terceiro_item = input('E o terceiro item ')
confirmacao = input('Deseja confirmar?' '(Y/N)' )  

confirmacao = False
confirmacao2 = False

if confirmacao == 'Y':
    input('Tem certeza?')
    confirmacao = True
    
elif confirmacao == True: 
     confirmacao2 = input(primeiro_item, segundo_item, terceiro_item, 'correto?' '(Y/N)')

elif confirmacao2 == 'Y':
     confirmacao2 == True
     print('Obrigado!')

     
elif confirmacao2 == 'N':
     confirmacao2 == False
     print('')
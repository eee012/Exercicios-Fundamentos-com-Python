# Total do carrinho - Crie a lista carrinho = [12.50, 30.00, 7.50]. 
# Use um for para somar e mostre o total.
print('EXEMPLO')

lista_carrinho = [12.50, 30.00, 7.50]
total = 0

for item in lista_carrinho:
    print(item)
    total += item

print('A soma é:',total)

print()
print('EXERCICIO 1')
print()

lista_temperaturas = [22, 31, 27, 35, 19]
temp_total = 0

for temperatura in lista_temperaturas:
    if temperatura >= temp_total: 
        temp_total = temperatura

print(temp_total)

palavras = ["sol", "computador", "casa", "python", "janela"]
contador = 0

for palavra in palavras:
    if len(palavra) > 5:
        contador = contador + 1

print(contador)



# Faça um algoritmo que leia 30 valores do tipo inteiro e armazene-os
# em um vetor. A seguir, o algoritmo deverá informar (1) todos os números
# pares que existem no vetor; (2) o menor e o maior valor existente no vetor;
# (3) quantos dos valores do vetor são maiores que a média desses valores:

valores = []
soma = 0
contador = 0

for i in range(30):
    valor = int(input("Digite um número: "))
    valores += [valor]
    soma += valor
    contador += 1

print("Números pares:")
for valor in valores:
    if valor%2 == 0:
        print(valor)

menor_valor = valores[0]
maior_valor = valores[0]
for valor in valores:
    if valor < menor_valor:
        menor_valor = valor
    if valor > maior_valor:
        maior_valor = valor
print(f'Menor valor no vetor: {menor_valor}')
print(f'Maior valor no vetor: {maior_valor}')

media = soma/contador
maiores_que_media = 0
for valor in valores:
    if valor > media:
        maiores_que_media += 1

print(f'Quantidade de valores maiores que a média: {maiores_que_media}')

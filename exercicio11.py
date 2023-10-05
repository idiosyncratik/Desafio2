# Faça um código para ler um vetor de 30
# números. Após isto, ler mais um número
# qualquer, calcular e escrever quantas
# vezes esse número aparece no vetor.
# Inicializar um vetor com 30 elementos
vetor = [0] * 30

for i in range(30):
    vetor[i] = int(input("Digite o valor: "))

numero_qlq = int(input("Digite qual dos números digitados deseja buscar: "))

contagem = 0
for num in vetor:
    if num == numero_qlq:
        contagem += 1

print(f"O número {numero_qlq} aparece {contagem} vezes no vetor.")

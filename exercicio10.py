# Faça um código para ler um valor N qualquer (que será o tamanho dos
# vetores). Após, ler dois vetores A e B (de tamanho N cada um) e depois
# armazenar em um terceiro vetor Soma a soma dos elementos do vetor A com
# os do vetor B (respeitando as mesmas posições) e escrever o vetor Soma.
valorN = int(input("Digite a quantidade: "))
vetorA = [0] * valorN
vetorB = [0] * valorN
soma = [0] * valorN
for x in range(valorN):
    vetorA[x] = int(input("Digite o valor de A: "))
    vetorB[x] = int(input("Digite o valor de B: "))
    soma[x] = vetorA[x] + vetorB[x]
print(f'O valor {vetorA} somado ao valor {vetorB} é igual a: {soma}.')
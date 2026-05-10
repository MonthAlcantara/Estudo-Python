num = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
if num < 0:
    print("Número inválido para cálculo de fatorial.")
else:
    for n in range(1, num+1):
        fatorial = fatorial * n

print(f"O fatorial de {num} é: {fatorial}")

numero_digitado = int(input("Digite um numero com no mínimo 2 digitos: "))

soma = 0
for n in range(1 , numero_digitado + 1):
    soma += n

print(f"O somatorio em for é {soma}")    

soma = numero_digitado
while True:
    soma += numero_digitado - 1
    numero_digitado -= 1
    if numero_digitado <= 0:
        break

print(f"O somatorio em while é {soma}")  
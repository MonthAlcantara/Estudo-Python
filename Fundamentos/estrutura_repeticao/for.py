times = ["Corinthians", "São Paulo", "Flamengo", "Cruzeiro"]

# Pode ser usado iterando uma lista pronta
for time in times:
    print(time)

soma = 0
#Pode ser usado apartir de um range predefinido
for i in range(1,6):
   idade = int(input(f"Entre com a idade {i}: "))     
   soma += idade
media = soma/5
print("A média de idade é: ", media)

#Range aceita até 3 parametros range([inicio,], fim [,passo]). Apenas o fim é obrigatório, os outros são opcionais. 
# O passo é o incremento, ou seja, o valor que será adicionado a cada iteração. Se o passo for negativo, a contagem será regressiva.   
#range(3)    o 3 nesse caso é o fim, ou seja, o range vai gerar os números 0, 1 e 2. O início é 0 por padrão e o passo é 1 por padrão.
#range(2,6)  2 e 6 nesse caso são o início e o fim, ou seja, o range vai gerar os números 2, 3, 4 e 5. O passo é 1 por padrão.  
#range(2,7,2)  Nesse caso o início é 2, o fim é 7 e o passo é 2, ou seja, o range vai gerar os números 2, 4 e 6. 
#              O número 7 não é incluído porque o range gera números até o fim, mas não inclui o fim.  
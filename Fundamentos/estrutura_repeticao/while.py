idade = 18
soma_idades = 0
repeticoes = 0
# O while é uma estrutura de repetição que executa um bloco de código enquanto uma condição for verdadeira.
while idade >= 18:
    idade = int(input("Digite a idade: "))
    if(idade >= 18):
        repeticoes += 1
        soma_idades += idade
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")
        
if repeticoes > 0 and soma_idades > 0:        
    print(f"A media das idades é: {soma_idades/repeticoes}")        
        

n = 0        
while True:
    n += 1        
    if n == 3:
        continue # O continue é usado para pular a iteração atual e continuar com a próxima iteração do loop.
    elif n == 10:
        break # O break é usado para sair do loop imediatamente, independentemente de a condição do loop ser verdadeira ou falsa.
    print(f"O valor de n é: {n}")
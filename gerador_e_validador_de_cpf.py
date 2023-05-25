# Importando biblioteca para propor aleatoriedade.
from random import randint


# Declarando variável usada nos loops 
valido = False


# Função responsável por calcular qual os verificadores devidos do cpf apresentado.
def calcula_verificador(n):
    soma = 0
    resto = 0
    resultado = 0
    for i in range(0,(8 + n)):
        soma += int(numero[i])*(9 + n - i)
    resto = (soma * 10) % 11
    resultado = resto if resto < 10 else 0 
    return str(resultado)

# Função responsável por retornar se o cpf apresentado é valido ou não.
def valida_cpf(cpf):
    cpf_esperado = False
    if numero != len(numero)*numero[0]:
        nove_digitos = numero[0:9]; digito_1 = calcula_verificador(1); digito_2 = calcula_verificador(2)
        cpf_esperado = nove_digitos + digito_1 + digito_2
    if cpf_esperado != False and cpf_esperado == numero: 
        valido = True
    return valido

# Algoritmo:
decisao = input().title().strip()

if decisao == "A":
    cpf = input("Digite o CPF para a verificação: ").strip()
    numero = (cpf.replace(".","")).replace("-","")
    if valida_cpf(numero) == True:
        print(f"O CPF {cpf} é considerado válido")

    else:
        print(f"O CPF {cpf} não é considerado válido")
    
elif decisao == "B":
    while valido == False:
        numero = ""
        for i in range(11):
            numero += str(randint(0,9))

        valido = valida_cpf(numero)

    print(numero)

else:
    print("Erro")

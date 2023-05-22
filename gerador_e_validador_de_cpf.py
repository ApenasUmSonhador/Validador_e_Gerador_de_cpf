
from random import randint
valido = False
def calcula_verificador(n):
    soma = 0; resto = 0; resultado = 0;
    for i in range(0,(8 + n)):
        soma += int(numero[i])*(9 + n - i)
    resto = (soma * 10) % 11
    resultado = resto if resto < 10 else 0 
    return str(resultado)

def valida_cpf(cpf):
    cpf_esperado = False; valido = False;
    if numero != len(numero)*numero[0]:
        nove_digitos = numero[0:9]; digito_1 = calcula_verificador(1); digito_2 = calcula_verificador(2)
        cpf_esperado = nove_digitos + digito_1 + digito_2
    if cpf_esperado != False and cpf_esperado == numero: 
        valido = True
    return valido

entrada = input().title().strip()
if entrada == "A":
    cpf = input("Digite o CPF para a verificação: ").strip()
    numero = (cpf.replace(".","")).replace("-","")
    if valida_cpf(numero) == True:
        print(f"O CPF {cpf} é considerado válido")
    else:
        print(f"O CPF {cpf} não é considerado válido")
    
elif entrada == "B":
    while valido == False:
        numero = ""
        for i in range(11):
            numero += str(randint(0,9))
        valido = valida_cpf(numero)
    print(numero)
else:
    print("Erro")
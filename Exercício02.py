#Depois reecreva a função leiaInt(), agora incluindo a possibilidade da digitação de um tipo
#invalido(fazendo as condições de erro). E depois Crie também uma função leiaFloat() com essa mesma
#funcionalidade.
RED   = "\033[1;31m"  
RESET = "\033[0;0m"
def linhas():
    print("-"*35)

def leiaInt(mensagemInt):
    x=False
    valor=0
    try:
        while True:
            valorInt=str(input(mensagemInt))
            if valorInt.isnumeric():
                valor=int(valorInt)
                x=True
            if x:
                break
            return valor
    except(ValueError,TypeError,ZeroDivisionError):
        print(RED+"ERRO! Você precisa digitar um valor válido."+RESET)
        linhas()
valorInt=leiaInt("Insira um número inteiro: ")
print(valorInt)

#Parte2(Não está com as regras acima)
def leiaFloat(mensagemFloat):
    x=False
    valorF=0
    while True:
        valorFloat=str(input(mensagemFloat))
        if valorFloat.isnumeric():
            valorF=float(valorFloat)
            x=True
        else:
            print(RED+"ERRO! Você precisa digitar um valor válido."+RESET)
            linhas()
        if x:
            break
    return valorF

valorFloat=leiaFloat("Insira um número Real: ")
print(valorFloat)
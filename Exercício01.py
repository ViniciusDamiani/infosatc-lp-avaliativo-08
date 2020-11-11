#Crie um programa que tenha a funcao leiaInt(), que vai funcionar de forma semelhante a função
#input() do python. So que fazendo a validação para aceitar apenas um valor númerico. Ex: inteiro,
#real. Obs: Se o usuario não digitar o valor, quero que ele atribua o valor 0 a aquela variável.
#Será usado função e loop.

RED   = "\033[1;31m"  
RESET = "\033[0;0m"
def linhas():
    print("-"*35)

def leiaInt(mensagem):
    x=False
    valor=0
    while True:
        valorInt=str(input(mensagem))
        
        if valorInt.isnumeric():
            valor=int(valorInt)
            x=True
        else:
            print(RED+"ERRO! Você precisa digitar um valor válido."+RESET)
            linhas()
        if x:
            break
    return valor


valorInt=leiaInt("Insira um número inteiro: ")
print(valorInt)

        




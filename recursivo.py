import math

def Encontra_Array_Cruzado_Maximo(A, inferior, meio, superior):
    soma_esquerda = -math.inf
    soma = 0
    maximo_esquerda = 0
    for i in range(meio, inferior, -1):
        soma = soma + A[i]
        if(soma > soma_esquerda):
            soma_esquerda = soma
            maximo_esquerda = i

    soma_direita = -math.inf
    soma = 0
    maximo_direita = 0
    for i in range(meio + 1, superior):
        soma = soma + A[i]
        if(soma > soma_direita):
            soma_direita = soma
            maximo_direita = i
    return maximo_esquerda, maximo_direita, (soma_esquerda + soma_direita)

def Encontra_Subarray_Maximo(A, inferior, superior):
    if superior == inferior:
        return inferior, superior, A[inferior] #Caso base, onde divide e volta com uma casa. 
    else:
        meio = int((inferior + superior) / 2)

        inferior_esquerda, superior_esquerda, soma_esquerda = Encontra_Subarray_Maximo(A, inferior, meio)
        inferior_direita, superior_direita, soma_direita = Encontra_Subarray_Maximo(A, meio + 1, superior)
        inferior_cruzamento, superior_cruzamento, soma_cruzamento = Encontra_Array_Cruzado_Maximo(A, inferior, meio, superior)
        
        if((soma_esquerda >= soma_direita) and (soma_esquerda >= soma_cruzamento)):
            return inferior_esquerda, superior_esquerda, soma_esquerda
        elif((soma_direita >= superior_direita) and (soma_direita >= soma_cruzamento)):
            return inferior_direita, superior_direita, soma_direita
        else:
            return inferior_cruzamento, superior_cruzamento, soma_cruzamento
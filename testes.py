from iterativo import *
from recursivo import *
from formatarTempo import *
import random
import time



entrada = []
tamanho = 700 #Quantidade de posições do vetor de entrada
limite = 10
for i in range(0,tamanho):
  entrada.append(random.randint(limite * -1,limite))  


print("Tamanho da Entrada: ", tamanho)

  
start_time = time.time()
dia_compra, dia_venda, lucro = subArranjoMaximoIterativo(entrada, tamanho)
print()
print("Algorítmo Iterativo:")
print("O melhor dia para compra é: ", dia_compra, " para venda: ",dia_venda," o lucro total é: ", lucro)
print("Tempo de Execução: " , time.time() - start_time)


start_time = time.time()
dia_compra, dia_vende, lucro = Encontra_Subarray_Maximo(entrada, 0, len(entrada) - 1)
print()
print("Algorítmo Recursivo:")
print("O melhor dia para compra é: ", dia_compra + 1, " para venda: ",dia_vende + 1," o lucro total é: ", lucro)
print("Tempo de Execução: " , time.time() - start_time)
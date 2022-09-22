import sys

def subArranjoMaximoIterativo(entrada, tamanho):
      
  # Buscando o índice da última posição da entrada
  ultimaPosicao = tamanho -1  

  # Calculando o tamanho dos vetores de resultado
  tamResult = tamanho
  for x in range(ultimaPosicao, 0, -1):    
    tamResult = tamResult + x    

  #print()
  #print("Quantidade de possíveis somas: ", tamResult)

  # Instanciando vetores de resultado com o tamanho do resultado
  inicios = [-sys.maxsize - 1] * tamResult  
  terminos = [-sys.maxsize - 1] * tamResult  
  somas = [-sys.maxsize - 1] * tamResult    
    
  # Variável para controlar o índice dos resultados das somas para guardar nos vetores de resultado
  posResult = 0
    
  # Calculando as somas das posições combinando o início e o final do subarranjo
  soma = 0
  for x in range(0,ultimaPosicao + 1 ,1):
    soma = entrada[x]
    for y in range(x,ultimaPosicao + 1,1):
      if y != x:              
        soma = soma + entrada[y]
      inicios[posResult] = x
      terminos[posResult] = y
      somas[posResult] = soma
      posResult = posResult + 1
        
  # Buscando a maior soma e a posição que ela se encontra no vetor de resultados
  soma = -sys.maxsize - 1
  for x in range(0,tamResult,1):
    if somas[x] > soma:
      soma = somas[x]
      posResult = x  

  return inicios[posResult] + 1, terminos[posResult] + 1, soma
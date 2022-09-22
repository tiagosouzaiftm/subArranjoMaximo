import sys
import json
import os



def write_json(new_data, filename='somas.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["somas"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

def subArranjoMaximoIterativoJson(entrada, tamanho):

  nomeArquivo = "somas.json"    
  
  if os.path.exists(nomeArquivo):
    os.remove(nomeArquivo)
    
  with open(nomeArquivo,'w') as file:          
        json.dump({"somas" : []}, file, indent = 4)  
  
  # Buscando o índice da última posição da entrada
  ultimaPosicao = tamanho -1  

  # Calculando o tamanho dos vetores de resultado
  tamResult = tamanho
  for x in range(ultimaPosicao, 0, -1):    
    tamResult = tamResult + x    

  
    
  # Variável para controlar o índice dos resultados das somas para guardar nos vetores de resultado
  posResult = 0
    
  # Calculando as somas das posições combinando o início e o final do subarranjo  
  soma = 0    
  #with open(nomeArquivo,'a') as arquivo:
  for x in range(0,ultimaPosicao + 1 ,1):
    soma = entrada[x]
    for y in range(x,ultimaPosicao + 1,1):
      if y != x:              
        soma = soma + entrada[y]                    
      #json.dump({'inicio' : x, 'termino' : y, 'soma' : soma}, arquivo)                      
      write_json({"inicio" : x + 1, "termino" : y + 1, "soma" : soma})
      posResult = posResult + 1
        
  # Buscando a maior soma e a posição que ela se encontra no vetor de resultados
  with open(nomeArquivo) as arquivo:
    somas = json.load(arquivo)    
    soma = max(somas['somas'], key=lambda sm: sm['soma'])
    

  return soma["inicio"], soma["termino"], soma["soma"]
import os

os.system("cls || clear")

contadorNotas = 0
soma = 0
media=0

while True:
    nota=float(input(f"Digite uma nota (entre 8 e 10): "))
    resposta=float(input(f"Deseja inserir mais uma nota? "))
    
    resposta=resposta.upper()


    if resposta !="N":
     break
    
    soma+=nota
    contadorNotas+=1

  
  

media=soma/contadorNotas

print(f"Média: {media}")
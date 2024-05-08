import os

os.system("clear||cls")

soma=0
media=0
nota=0

for i in range(1,5):

 
 nota = float (input("Digite sua nota: "))
 soma=soma+nota
media=soma/4
 
print(f"Media:{media}")
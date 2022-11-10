# for no python = for each

frutas = ["Morango", "Laranja", "Banana"]

print(frutas[0])

# Quantas frutas eu tenho?

print(len(frutas)) #length = tamanho

# Como colocar algo a mais no Array ... append

frutas.append("Pêra")
frutas.append("Uva")

print(len(frutas))

i=0 # i = index

# Mostrando Array com while

print("Exemplo com While")

while(i<len(frutas)):
  print(frutas[i])
  i+=1

print("Exemplo com For")

# Esse for é inteligente .. trabalha com o "next" ele vai passando um por um ...

for fruta in frutas:
  print(fruta)
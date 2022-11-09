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

while(i<len(frutas)):
  print(frutas[i])
  i+=1
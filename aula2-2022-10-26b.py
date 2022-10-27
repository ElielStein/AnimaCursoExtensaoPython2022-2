#Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "Você é bichão, mesmo..."

nome = input("Informe seu nome:")
nota = float(input("Digite a sua nota: "))

if (nota==10):
  print(f"{nome} você é o cara!")
elif (nota >=6 and nota < 10):
  print(f"{nome} good job")
elif (nota >=0 and nota < 6):
  print(f"{nome} reprovado, precisa melhorar!")
else:
  print("Nota inválida ... digite uma nota de 0 a 10")
  
  

  

  






  
  

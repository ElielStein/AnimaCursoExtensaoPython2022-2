# input() = entrada de dados, pedir pra usuario digitar

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
genero = input("M = Masculino, F = Feminino, O = Outros. Digite seu gênero: ")

print(f"Seu nome é {nome} e tem {idade} anos")

dobro = idade * 2

print("O dobro da sua idade é {}".format(dobro))

# If = estruturas condicioanais

#E se eu quisessem perguntar o gênero (M = Masculino e F = Feminino)
#Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)

if (idade >= 18) and genero == "M":
  print("Você é maior de idade e precisa/precisou prestar o serviço militar obrigatório")  
else:
  print("Você não precisa/precisou prestar serviço militar")


  
  

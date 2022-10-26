# input() = entrada de dados, pedir pra usuario digitar

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Seu nome é {nome} e tem {idade} anos")

dobro = idade * 2

print("O dobro da sua idade é {}".format(dobro))
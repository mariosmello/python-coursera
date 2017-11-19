#Faça um programa em Python que receba (entrada de dados) o valor
# correspondente ao lado de um quadrado, calcule e imprima (saída de dados)
# seu perímetro e sua área.

lado = input("Digite o lado do quadrado:")

lado = int(lado)
perimetro = (lado * 4)
area = (lado * lado)

#perímetro: 12 - área: 9
print("perímetro:",perimetro,"- área:",area)

import math

a = float(input("Valor de A: "))
b = float(input("Va1lor de B: "))
c = float(input("Valor de C: "))

delta = (b**2) - (4 * (a*c))

if delta == 0:
    x1 = ((b * -1) + math.sqrt(delta)) / (2*a)
    print("a raiz desta equação é X", x1)
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        x1 = ((b * -1) + math.sqrt(delta)) / (2*a)
        x2 = ((b * -1) - math.sqrt(delta)) / (2*a)
        if x1 <= x2:
            print("as raízes da equação são",x1,"e",x2)
        else:
            print("as raízes da equação são",x2,"e",x1)

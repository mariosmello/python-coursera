import math

x1 = int(input('X1: '))
y1 = int(input('Y1: '))
x2 = int(input('X2: '))
y2 = int(input('Y2: '))

x = (x2-x1)**2
y = (y2-y1)**2

distancia = math.sqrt(x+y);

if distancia >= 10:
    print('longe')
else:
    print('perto')

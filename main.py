import math as m

# H = input("Введите высоту (cm): ")
# V = input("Введите объём (cm): ")
# Ab = input("Введите площадь основания (cm): ")
# Al = input("Введите площадь поверхности (cm): ")
# A = input("Введите общую площадь (cm): ")

# Формулы:
# Ab = pi*pow(R, 2)
#     pow(R, 2) = Ab/pi
#     R = sqrt(Ab/pi)
# Al = 2*pi*R*H
#     R = Al/(2*pi*H)
#     H = Al/(2*pi*R)
# A = Al + Ab
#     Al = A - Ab
#     Ab = A - Al
# V = pi * pow(R, 2) * H
#     pow(R, 2) = V/(pi*H)
#     R = m.sqrt(V/(pi*H))
#     H = V/(pi*pow(R, 2))

print("Вас приветствует программа Python, которая решает задачки с геометрическими фигурами!")
figure = str(input("Введите фигуру (Доступные фигуры: Цилиндр, куб): "))
figure.upper()
if figure.upper() == 'ЦИЛИНДР' :
    cilR = float(input("Введите радиус основания (cm): "))
    cilAb = float(m.pi*pow(cilR, 2))
    cilAb = float('{:.3f}'.format(Ab))
    print("Радиус основания равен",Ab,"см2")

if figure.upper() == 'КУБ':
    cubI = float(input("Введите сторону: "))
    cubAb = pow(cubI,2)
    cubAl = (4*pow(cubI,2))
    cubAt = (6*pow(cubI,2))
    cubV = pow(cubI,3)
    print("Площадь основания равна", cubAb, "см2")
    print("Площадь боковых сторон равна", cubAl, "см2")
    print("Площадь всех сторон равна", cubAt, "см2")
    print("Объём равен", cubV, "см3")
else:
    print("В разработке :)")

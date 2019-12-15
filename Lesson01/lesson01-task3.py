# Ссылка на схемы
# https://drive.google.com/file/d/14vLKzw007Cj8Ld8VYsGee5cxRGMk5lHL/view?usp=sharing


print("введите координаты первой точки")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
print("введите координаты второй точки (вторая точка не должна совпадать с первой точкой)")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

if y1 == y2:
    print(f"Уравнение прямой через эти две точки: y = {y1}")
elif x1 == x2:
    print(f"Уравнение прямой через эти две точки: x = {x1}")
else:
    k = (y2 - y1) / (x2 - x1)
    b = (y1 * x2 - y2 * x1) / (x2 - x1)
    if b > 0:
        print(f"Уравнение прямой через эти две точки: y = {k}x + {b}")
    elif b < 0:
        print(f"Уравнение прямой через эти две точки: y = {k}x - {abs(b)}")
    else:
        print(f"Уравнение прямой через эти две точки: y = {k}x")
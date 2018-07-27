a = int(input("Введите число 1"))
b = int(input("Введите число 2"))
f = str(input("Введите оператор + - * /"))
e = eval("{} {} {}".format(a, f, b))
print(e)
# if f == "+":
#     print(a + b)
# elif f == "-":
#     print(a - b)
# elif f == "*":
#     print(a * b)
# elif f == "/" and b != 0:
#     print(a / b)
# elif f == "/" and b == 0:
#     print("Делить на ноль нельзя!")
# else:
#     print("Нет такого действия")


import math
while (True):
    print("Выберите действие:")
    print("1.Сложение")
    print("2.Вычитание")
    print("3.Умножение")
    print("4.Деление")
    print("5.Возведение в степень")
    print("6.Квадратный корень")
    print("7.Факториал")
    print("8.Синус")
    print("9.Косинус")
    print("10.Тангенс")
    print("11.Выход из программы")
    choice = int(input())
    match choice:
        case 1:
            a = int(input("Введите первое число "))
            b = int(input("Введите второе число "))
            print("Результат ",a + b)
        case 2:
            a = int(input("Введите первое число "))
            b = int(input("Введите второе число "))
            print("Результат ", a - b)
        case 3:
            a = int(input("Введите первое число "))
            b = int(input("Введите второе число "))
            print("Результат ", a * b)
        case 4:
            a = int(input("Введите первое число "))
            b = int(input("Введите второе число "))
            if b==0:
                print("На ноль делить нельзя")
            else:
                print("Результат ", a / b)
        case 5:
            a = int(input("Введите число "))
            b = int(input("Введите степень "))
            print("Результат ", a ** b)
        case 6:
            a = int(input("Введите число "))
            print("Результат ",a**0.5)
        case 7:
            a = int(input("Введите число "))
            print("Результат ",math.factorial(a))
        case 8:
            a = int(input("Введите угол(в градусах) "))
            a = math.radians(a)
            print("Результат ",math.sin(a))
        case 9:
            a = int(input("Введите угол(в градусах) "))
            a = math.radians(a)
            print("Результат ",math.cos(a))
        case 10:
            a = int(input("Введите угол(в градусах) "))
            a = math.radians(a)
            print("Результат ", math.tan(a))
        case 11:
            break
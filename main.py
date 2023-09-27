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
    try:
        choice = int(input())
    except ValueError:
        print("Надо вводить число")
    match choice:
        case 1:
            try:
                a = int(input("Введите первое число "))
                b = int(input("Введите второе число "))
                print("Результат ",a + b)
            except ValueError:
                print("Надо вводить число")
        case 2:
            try:
                a = int(input("Введите первое число "))
                b = int(input("Введите второе число "))
                print("Результат ", a - b)
            except ValueError:
                print("Надо вводить число")
        case 3:
            try:
                a = int(input("Введите первое число "))
                b = int(input("Введите второе число "))
                print("Результат ", a * b)
            except ValueError:
                print("Надо вводить число")
        case 4:
            try:    
                a = int(input("Введите первое число "))
                b = int(input("Введите второе число "))
                if b==0:
                    print("На ноль делить нельзя")
                else:
                    print("Результат ", a / b)
            except ValueError:
                print("Надо вводить число")
        case 5:
            try:
                a = int(input("Введите число "))
                b = int(input("Введите степень "))
                print("Результат ", a ** b)
            except ValueError:
                print("Надо вводить число")
        case 6:
            try:
                a = int(input("Введите число "))
                print("Результат ",a**0.5)
            except ValueError:
                print("Надо вводить число")
        case 7:
            try:
                a = int(input("Введите число "))
                print("Результат ",math.factorial(a))
            except ValueError:
                print("Надо вводить число")
        case 8:
            try:
                a = int(input("Введите угол(в градусах) "))
                a = math.radians(a)
                print("Результат ",math.sin(a))
            except ValueError:
                print("Надо вводить число")
        case 9:
            try:
                a = int(input("Введите угол(в градусах) "))
                a = math.radians(a)
                print("Результат ",math.cos(a))
            except ValueError:
                print("Надо вводить число")
        case 10:
            try:
                a = int(input("Введите угол(в градусах) "))
                a = math.radians(a)
                print("Результат ", math.tan(a))
            except ValueError:
                print("Надо вводить число")
        case 11:
            break

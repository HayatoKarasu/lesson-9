mn1 = set(input("Введите любые числа через пробел: "))

if len(mn1) <= 100000:
    mn2 = set(input("Введите любые числа ещё раз: "))
    
    if len(mn2) <= 100000:
        mn3 = mn1.intersection(mn2)
        print(mn3)
        print(len(mn3))
    else:
        print("Недопустимое количество чисел")

else:
    print("Недопустимое количество чисел")

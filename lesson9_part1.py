n = int(input("Введите любое число не больше 10000: "))
mn = set()

if 1 <= n <= 100000:
    print("Введите любые", n, "чисел через пробел")
    
    sp = list(map(int, input().split()))

    for i in sp:
        mn.add(i)
    
    print(len(mn))

else:
    print("Слишком большое число!")

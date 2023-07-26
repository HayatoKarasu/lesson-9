print("Введите любые числа через пробел")
sp = list(map(int, input().split()))

mn = set()

for i in sp:
    if i in mn:
        print("Yes")
    else:
        print("No")
        mn.add(i)
    

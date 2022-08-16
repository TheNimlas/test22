mains = input()
n = int(input())
for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    stroka = mains[a-1:b]
    print(stroka)
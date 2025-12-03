#39
n = int(input())

def number():
    for i in range(0, n+1):
        if i % 2 != 0:
            print(i)

number()

#40
n = int(input())

def number2():
    if n % 3 == 0:
        print(n)

number2()

#41
n = list(map(int, input().split()))

def number3(a, b, c, d):
    maximum = max(a, b, c, d)
    minimum = min(a, b, c, d)
    return maximum, minimum

ma, mi = number3(*n)
print("최댓값: ", ma,"최솟값: ", mi)

#42
n = int(input())

def number4():
    for i in range(0, n+1):
        if i % 2 != 0:
            print(i)

number4()

#43
n = int(input())

def factorial():
    result = 1 
    for i in range(1, n+1):
        result *= i
    print(result)

factorial()

#44
i = int(input())
j = int(input())

def number5(i, j):
    total = 0
    for a in range(1, i+1):
        for b in range(1, j+1):
            if a * b >= 30:
                total += a * b
    print(total)

number5(i, j)

#45
def number6(a):
    total = 0
    for i in a:
        total += i
    return total

a = [1, 2, 3, 4, 5]
print(number6(a))


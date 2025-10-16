#과제11
a = list(input())
b = input()

a.insert(len(a), b)
print(a)

#과제12
a = list(input())
b = a.pop()
c = a.pop()
print(a)

#과제13
a = input()

for index, value in enumerate(a, start = 101):
    print(index, value)

#과제14
a = [10, 20, 30, 40, 30, 20, 10]
result = a.count(20)

print(result)

#과제15
a = input()
b = list(map(int, a.split()))
c = min(b)
d = max(b)

print("최솟값", c)
print("최댓값", d)

#a = list(map(int, input().split())) 이렇게 쓰면 최솟값이 공백으로 출력되는데 원래 안 되는 건가여?? 아니면 잠시 오류난 건가여.. 일단 밑에 문제도 한번 입력 먼저 받고 형변환 다시 하긴 했어여

#과제16
a = input()
b = list(map(int, a.split()))

b.remove(min(b))
b.remove(max(b))

print(sum(b))

#과제17
a = [10, 20, 30, 40, 30, 20, 10]
a.remove(20)
a.remove(20)

print(a)

#과제18
a = [i for i in range(1,6)]
print(a)

#과제19
a = [i for i in range(1, 21) if i % 2 != 0]
print(a)

#과제20
a, b = map(int, input().split())
result = [2**i for i in range(a, b+1)]

del result[1]
del result[-2]

print(result)

#과제21
a = input('Hello,world! 입력')
a = a.replace('Hello', 'Hi')

print(a)

#과제22
a = input('임의의 문자 4개 입력')
a = " / ".join(a)

print(a)

#과제23
a = input('내 성을 입력')
b = a.lower()
c = b.rjust(10)

print(c)

#과제24
a = input('물품가격').split(';')
a.sort(reverse=True)

for b in a:
    print(b.rjust(9))

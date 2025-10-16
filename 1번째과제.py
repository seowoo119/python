#1
n = (-32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2)
new_tuple = n[1::2]
print(new_tuple)

#2
ex = input().split()
del ex[5::]
print (ex)

#3
a = list(input().split())
print( a[:2] )

#4
a = list(input().split())
print(a[1::2])

#5
a = list(input().split())
print(a[5::])

#6
a = list(input().split())
del a[:4]
print(a)

#7
a = list(input().split())
print(a[3::3])

#8
a = list(input().split())
print(3*a)

#9
a = list(input().split())
b = list(input().split())
print(a+b)

#10
a = list(input().split())
print(a[-1])

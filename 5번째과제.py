#32
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

c = set.union(a, b)
d = set.intersection(a, b)

print("합집합: ", c)
print("교집합: ", d)


#33
a = {11, 12, 13, 14, 15}
b = {12, 14, 16, 18, 20}

c = set.difference(a, b)
d = set.symmetric_difference(a, b)

print("차집합: ", c)
print("대칭차집합: ", d)


#34
a = {1, 2, 3, 4, 5}
a.update( {100} )
print(a)


#35
a = {100, 200, 300, 400, 500}

a1 = a.copy()
a1.intersection_update( {400, 500, 600, 700, 800} )
a2 = a.copy()
a2.difference_update( {400, 500, 600, 700, 800} )
a3 = a.copy()
a3.symmetric_difference_update( {400, 500, 600, 700, 800} )

print(a1, a2, a3)


#36
a = {100, 200, 300, 400, 500}

result1 = (a <= {100, 200, 300, 400, 500})
result2 = (a >= {100, 200, 300, 400, 500})

if result1 and result2:
    print("동시")
elif result1:
    print("부분")
elif result2:
    print("상위")


#37
a = {1, 2, 3, 4, 5}

a.add(1000)
a.remove(1000)

print(a)


#38
multiples = {x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0}
print(multiples)
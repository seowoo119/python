a = input('물품가격').split(';')
a.sort(reverse=True)

for b in a:
    print(b.rjust(9))
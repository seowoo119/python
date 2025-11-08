#25번
key = input().split()
value = list(map(int, input().split()))

d = dict(zip(key, value))

d = {k: v for k, v in d.items() if k not in ['alpha', 'delta']}

print(d)

#26번
park = dict({'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83})

eng = park.get('english')
sci = park.get('science')

print(eng, sci)

#27번
kim = dict({'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83})
kim.update(korean=100, english=100, mathematics=100, science=100)

print(kim)

#28번
lee = dict({'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83})

if 'english' in lee:
    del lee['english']

print(lee)

#29번
lim = dict({'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83})

print(lim.items())

#30번
choi = dict({'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83})

choi = {key: value for key, value in choi.items() if value >= 90}
print(choi)

#31번
yoo = dict({'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83})

a = yoo.values()
b = sum(a)/len(a)

print(b)
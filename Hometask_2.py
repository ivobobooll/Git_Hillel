
### 1)
#1.1

x = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
print (set(x))

#1.2
x = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
x.sort()
print (x[-3])
print (x[-2])
print (x[-1])

#1.3
x = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
y = x.index(min(x))
print (y)

#1.4
x = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1][::-1]
print (x)

# 2)

y = []
x = 0
while x <= 100:
   x = x + 1
   if x % 2 == 0:
       y.append(x)
print (y)

# 3)

dict_one = {'a': 1, 'b': 2, 'c': 3,  'd': 4}
dict_two = {'a': 6,  'b': 7, 'z': 20, 'x': 40}

allkeys = (list(dict_one.keys())) + (list(dict_two.keys()))

calculations = []

for item in allkeys:
    count = 0
    for x in allkeys:
        if x == item:
            count += 1
    calculations.append(count)

duplicates = set()
index = 0
while index < len(allkeys):
    if calculations[index] != 1:
        duplicates.add(allkeys[index])
    index += 1

print(duplicates)

# 4)

dict = {}
x = 1
while x <= 10:
   dict[x]=x*x
   x = x + 1
print (dict)
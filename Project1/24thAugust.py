# import random
# import numpy
fruits=['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)

fruits.remove('cherry')
print(fruits)

colors = ['red', 'green', 'blue']
colors.insert(1,'yellow')
print(colors)

letters = ['a', 'b', 'c', 'a', 'd']
x=letters.count('a')
print(x)

data = [10, 20, 30, 40, 50]
x =data[-1]
data.remove(x)
print(data)
print(x)

values = [4, 1, 7, 3, 9]
values.sort()
print(values)

cities = ['New York', 'Los Angeles', 'Chicago','Houston']
id=cities.index('Chicago')
print(id)

#demo1=name.replace("Sultana","Islam")
animals = ['dog', 'cat', 'elephant', 'lion']
id=animals.index('elephant')
animals.remove('elephant')
animals.insert(id,'tiger')
print(animals)

numbers = [5, 2, 8, 2, 1]
x=numbers.count(2)
print(x)

fruits = ['apple', 'banana', 'cherry']
reverse_fruits=fruits[::-1]
print(reverse_fruits)
# for a in fruits:
#     x=fruits[-1]
#     print(x)
#     fruits.remove(-1)
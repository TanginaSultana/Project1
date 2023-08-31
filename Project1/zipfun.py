name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
home=['dhaka','feni','chandpur','savar']

# using zip() to map values
mapped = zip(name, roll_no, home)

print(set(mapped))
#print(mapped)

names = ['Alice', 'Bob', 'Charlie',]
ages = [25, 30, 22]

zipped = zip(names, ages)

for item in zipped:
    print(item)

import math
list1 = [int(item) for item in input("sample input = ").split()]
n=len(list1)-1
x=0
for i in list1:
    x=x+i

x_ave=(x/(n+1))
#print(x_ave)

#result = [num ** 2 for num in numbers if num % 2 == 1]
list2=[(num-x_ave)**2 for num in list1]
#print(list2)

x=0
for i in list2:
    x=x+i
z=math.sqrt(x/n)
print("Output: ",z)
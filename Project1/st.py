name="Tangina Sultana"
name2='''My name is Tangina.
It is a 
work'''
name1=name.lower()
demo1=name.replace("Sultana","Islam")
spilt_txt1=demo1.split()
spilt_txt2=name2.split('e')
size_name=len(name)
p1=name.count('n')
p2=name.find('S')
print(p1," ",p2)
print(spilt_txt1[0],"\n")
print(spilt_txt2,"\n")
# print(name.endswith('na'))
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

txt = "        banana     "
txt1 = "        banana    guhgeiv     a"
x = txt1.rstrip()

print("of all fruits", x, "is my favorite/n")
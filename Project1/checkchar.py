number='1264666,yftyy,25666655'
character=0
for x in number:
    if number[x].isalpha():
        print("There is a charecter and it is",number[x])
        character=character+1
        break

if(character>0):
    print("There is no charecter")


#print(number)
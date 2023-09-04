num=[[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12,],[13, 14, 15, 16]]
#result = [num ** 2 for num in numbers if num % 2 == 1]
num2=num
i=0
j=0
for row in num2:
    j=0
    for col in row:
        if(col>9):
           if(num2[i][j]%10==0):
              num2[i][j]=int(num2[i][j]/10)
           else:
             num2[i][j]= num2[i][j]%10   
               
           j=j+1
    i=i+1

 
print("Output1: ",num2)


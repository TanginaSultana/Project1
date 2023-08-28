name = input("enter your name:")
bangla = int(input("enter the number you got in bangle:"))
english= int(input("enter the number you got in english:"))
math = int(input("enter the number you got in math:"))
islam = int(input("enter the number you got in islam:"))
ict = int(input("enter the number you got in ict:"))
ban_and_world = int(input("enter the number you got in ban_and_world:"))
physics = int(input("enter the number you got in physics:"))
chemistry = int(input("enter the number you got in chemistry:"))
biology = int(input("enter the number you got in biology:"))
home_science = int(input("enter the number you got in home_science:"))

if(bangla>=33 and bangla<=100 and english>=33 and english<=100 and math>=33 and math<=100 and islam>=33 and islam<=100 and ict>=33 and ict<=100 and ban_and_world>=33 and ban_and_world<=100 and physics>=33 and physics<=100 and chemistry>=33 and chemistry<=100 and biology>=33 and biology<=100 and home_science>=33 and home_science<=100):
    total_nuber=bangla+english+math+islam+ict+ban_and_world+physics+chemistry+biology+home_science
    print("\n")
    grade_point=total_nuber/10
    print("Your grade point is: ",grade_point)

    if(grade_point>=80 and grade_point<=100):
        print("Your grade is A+")
    elif(grade_point>=70 and grade_point<=79):
        print("Your grade is A")
    elif(grade_point>=60 and grade_point<=69):
        print("Your grade is B+")
    elif(grade_point>=50 and grade_point<=59):
        print("Your grade is B")
    elif(grade_point>=40 and grade_point<=49):
        print("Your grade is C+")
    elif(grade_point>=33 and grade_point<=39):
        print("Your grade is C")

    print("Percentage Rangr:")
    print("80-100  -->   A+")
    print("70-79  -->   A")
    print("60-69  -->   B+")
    print("50-59  -->   B")
    print("40-49  -->   C+")
    print("33-39  -->   C")
else:
    print("Fail")
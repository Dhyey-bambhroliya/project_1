a = int(input("enter the first number :- "))
b = int(input("enter the second number :- "))
print("1. + \t2. - \t3. X \t4. % ")
c = int(input("enter the choice :- "))

if (c==1):
    print("this is addition:-",a+b)
elif (c==2):
    print("this is sub:-",a-b)
elif (c==3):
    print("this is multiplication:-",a*b)
elif (c==4):
    print("this is is division:-",a/b)
else:
    print("nothing")
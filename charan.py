y= int(input("enter the gpa of first sem"))
print(y)
if y == 7 :
    print('nuvvu super ra chinnu')
else:
    print('neekante neecha nekrustudu evadu vundadu')
#                                   AGE CALCULATOR
dob = int(input("enter your birth year"))
age = 2024-dob
print("your age is ",age)
country = input("enter your native country")

#                            BASIC ATM
cash = 200
pin = int(input("enter the pin sir"))
if pin==9440:
    print("you have entered correct pin ")
    amount= int(input('inta kavali sir'))
    print('take the amount sir',amount)
    remaining = cash - amount
    print('the remainig money is',remaining)
else :
    print("the pin you have entered is wrong")
    print("you can try again sir")






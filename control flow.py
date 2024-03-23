budget = int(input("enter your budget for trip "))
if budget >= 30000:
    print("with this budget you can go to GOA")
elif 20000 <= budget <= 30000:              # you can also write by budget >= 20000 and budget <=30000
    print("you can go to all temples")
elif 10000 <= budget >= 20000:
    print("you can go to wonderla ")
else:
    print("you should be in pg")



name = input("peru cheppu ra ")
vowels = ["a", "e", "i", "o", "u"]
for character in name:
    if character in vowels:
        print(character, "it is an vowel")
        # break # if we place break here only one "if" will be executed
    else:
        print(character, "it is an consonant")

score = 0
scoreinfo = []
while score <= 100:
    import random
    scorevalue = random.randint(1,6)
    scoreinfo.append(scorevalue)
    score += scorevalue
    print("the score no hit is ", scorevalue)
    print("total score now ", score, "the present scores are ", scoreinfo)


# sum of things in an array
a = [23, 45, 67, 989, 34, 30]
sum = 0
for i in a:
    sum += i
print('total sum is ', sum)

# pass or fail checking by roll number
list = {1: {'mains': 'qualify', "percentile": 89},
        2: {'mains': 'qualify', "percentile": 84},
        3: {'mains': 'not qualify', "percentile": 54}}
roll = int(input("enter your roll number to check your faith "))
percentile = list[roll]["percentile"]
if percentile >= 81:
    print("you have successfully qualified the test ")
else:
    print("you have not qualified test please go and die")







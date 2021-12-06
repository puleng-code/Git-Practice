answer1 = input('Hello! Would you like to add or subtract? (Type "add" or "subtract"):  ')
print(answer1)
answer2 = int(input('Okay! What is your first number?:  '))
answer3 = int(input('What is your second number?:  '))
sum1 = int(answer2) + int(answer3)
sum2 = int(answer2) - int(answer3)


if answer1 == 'add': 
    print(answer2,"+",answer3,"= ",sum1)
elif  answer1 == 'subtract': 
   print(answer2,"-", answer3, "= ", sum2)
#else: 
 #   print('Please enter either "add" or "subtract"') 




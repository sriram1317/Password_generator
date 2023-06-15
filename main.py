# Basic password generator


import random


print("Welcome to password generator!")

#Getting values
passLen = int(input("How many letters would you like in your password?\n"))
passSym = int(input("How many symbols would you like?\n"))
passNum = int(input("How many num would you like?\n"))

# final passord string 
password = ""

#the lists from here we are going to take the charecters for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ['1','2','3','4','5','6','7','8','9','0']
sym = ['!','@','#','$','%','^','&','*','(',')','-','=','+','*','/','[',']','{','}',':',';',',','.','?','<','>']

# list to store the generated charecters
pass_gen = []

# get random letters from the list 
for i in range(0, passLen):
    pass_gen.append(random.choice(letters))

# get random number from the list
for i in range(0, passNum):
    pass_gen.append(random.choice(num))

# get random symbols from the list
for i in range(0, passSym):
    pass_gen.append(random.choice(sym))

#shuffling the generated list to get random charecters at random indices
random.shuffle(pass_gen)

# turning shuffled list to string
for i in pass_gen:
    password += i

# printing the result
print(f'your generated password is: {password}')

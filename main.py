# Basic password generator


import random
print("Welcome to password generator!")

passLen = int(input("How many letters would you like in your password?\n"))
passSym = int(input("How many symbols would you like?\n"))
passNum = int(input("How many num would you like?\n"))

totLen = passLen + passSym + passNum

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ['1','2','3','4','5','6','7','8','9','0']
sym = ['!','@','#','$','%','^','&','*','(',')','-','=','+','*','/','[',']','{','}',':',';',',','.','?','<','>']

letLen = len(letters)
numLen = len(num)
symLen = len(sym)

pass_gen = []

for i in range(0, passLen):
    pass_gen.append(random.choice(letters))

for i in range(0, passNum):
    pass_gen.append(random.choice(num))

for i in range(0, passSym):
    pass_gen.append(random.choice(sym))

password = ""
random.shuffle(pass_gen)

for i in pass_gen:
    password += i


print(f'your generated password is: {password}')

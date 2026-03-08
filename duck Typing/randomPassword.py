import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','#','$','%','&','(',')','*','+']

print("Welcome tp the password generator")
nr_letter = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbol would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = []
shufflePassword=""

for char in range(1,nr_letter+1):
    password.append(random.choice(letters))

for sym in range(1,nr_symbols+1):
    password.append(random.choice(symbol))

for numb in range(1,nr_numbers+1):
    password.append(random.choice(number))

random.shuffle(password)
for p in password:
    shufflePassword +=p

print(f"Your Password is :  {shufflePassword}")



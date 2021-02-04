#Password Generator Project
#There's also a way to do this by using random.choice and random.shuffle, I'll have it in mind next time
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

ez_pass = ''
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for i in range(0, nr_letters):
    ez_pass += letters[random.randint(0, len(letters) - 1)]

for i in range(0, nr_symbols):
    ez_pass += symbols[random.randint(0, len(symbols) - 1)]

for i in range(0, nr_numbers):
    ez_pass += numbers[random.randint(0, len(numbers) - 1)]

print('Easy password:', ez_pass)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


symbol_count = 0
number_count = 0
hard_pass = []

for i in range(nr_letters + nr_symbols + nr_numbers):
    hard_pass.append(letters[random.randint(0, len(letters) - 1)])

changed_indices = []
while len(changed_indices) < nr_symbols + nr_numbers:
    current_index = random.randint(0, len(hard_pass) - 1)
    if current_index not in changed_indices:
        if symbol_count < nr_symbols:
            hard_pass[current_index] = symbols[random.randint(0, len(symbols) - 1)]
            symbol_count += 1
        elif number_count < nr_numbers:
            hard_pass[current_index] = numbers[random.randint(0, len(numbers) - 1)]
            number_count += 1
        changed_indices.append(current_index)


password = ''.join(hard_pass)

print(f'Hard password {password}')

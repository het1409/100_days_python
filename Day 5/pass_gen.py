import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', 
           '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

l_l = int(input("letter length? \n"))
n_l = int(input("numbers length? \n"))
s_l = int(input("symbol length? \n"))

pwd = ""

for char in range(1, l_l + 1):
    pwd = pwd + random.choice(letters)
for char in range(1, n_l + 1):
    pwd = pwd + random.choice(numbers)
for char in range(1, s_l + 1):
    pwd = pwd + random.choice(symbols)

print(pwd)
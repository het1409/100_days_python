#add

def add (n1, n2):
    return n1 + n2

#Substract

def substract (n1, n2):
    return n1 - n2

#Multiply

def multiply (n1, n2):
    return (n1 * n2)

#Divide

def div (n1, n2):
    return (n1 / n2)
    
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": div
}

num_1 = int(input("What's the first number: "))
num_2 = int(input("What's the second number: "))

for calc in operations:
    print(calc)

symbol = input("Select from the above operations: ")
func = operations[symbol]
result = func(num_1, num_2)

print(f"{num_1} {symbol} {num_2} = {result}")
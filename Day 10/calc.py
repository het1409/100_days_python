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
def calculator():

    num_1 = int(input("What's the first number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num_2 = int(input("What's the second number: "))
        calc_func = operations[operation_symbol]
        result = calc_func(num_1, num_2)

        print(f"{num_1} {operation_symbol} {num_2} = {result}")

        if input(f"Type 'y' to continue with {result}, or type 'n' to start a new caculation: ") == "y":
            num_1 = result
        else:
            should_continue = False
            calculator()

calculator()    
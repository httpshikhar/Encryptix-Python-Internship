
b = int(input("Enter how many numbers you want : "))
m = []
for i in range(b):
    n = int(input("Enter numbers : "))
    m.append(n)

def add():
    sum = 0
    for i in m:
        sum += i
    print("\nSum of numbers is : ",sum)

def sub():
    sub = m[0]
    for i in m[1:]:
        sub -= i
    print("\nSubtraction of numbers is : ", sub)

def mul():
    mul = 1
    for i in m:
        mul *= i
    print("\nMultiplication of numbers is : ", mul)

def div():
    try:
        div = m[0]
        for i in m[1:]:
            div /= i
        print("\nDivision of numbers is : ", div)
    except(ArithmeticError):
        print("\nDivision by zero is not possible")

while True:
    print("\n1. Add numbers")
    print("2. Subtract numbers")
    print("3. Multiply numbers")
    print("4. Divide numbers")
    print("5. Exit")
    
    choice = int(input("Enter your choice : "))
    
    if choice == 1:
        add()

    if choice == 2:
        sub()

    if choice == 3:
        mul()

    if choice == 4:
        div()

    if choice == 5:
        break

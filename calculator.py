def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiplication(num1,num2):
    return num1 * num2
def division(num1,num2):
    if num2 !=0:
        return num1 / num2
    else:
        print("invalid input")
if __name__ == '__main__':
num1 = int(input("Enter the first value:"))
num2 = int(input("Enter the second value:"))
print("Select operation")
print("1.add")
print("2.subtract")
print("3.multiplication")
print("4.division")
print("5.to exit")
while True:
    operator = input("Enter the choice of operation")
    if operator == "1":
        print("The sum of the value is",add(num1,num2))
    elif operator == "2":
        print("The value is", subtract(num1, num2))
    elif operator == "3":
        print("The value is", multiplication(num1, num2))
    elif operator == "4":
        print("The value is", division(num1, num2))
    elif operator == "5":
        print("Thank you for exiting")
        break







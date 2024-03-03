# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero")

# num1 = input("Enter a number: ")
# num2 = input("Enter a second number: ")

while True:
    num1 = input("\nEnter a number: ")
    if num1 == 'q': break
    num2 = input("Enter a second number: ") 
    if num2 == 'q': break
         
    try:
        # if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
    except ValueError:
        print("Input must be a number.")
        continue
    else:
        sum = num1 + num2
        print(sum)



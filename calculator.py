a = int(input("enter your first number:"))
b = int(input("enter your second nummber:"))
c = input("please chose your operations:")
if c == "+":
    print("your sum is :", a+b)
elif c == "-":
    print("your difference is:", a-b)
elif c == "*":
    print("your multipied value is:", a*b)
elif c == "/":
    print("your division is :", a/b)
else:
    print("invalid operation")

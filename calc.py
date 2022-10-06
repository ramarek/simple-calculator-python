def calculator(x, y, kaye):
    result = 0

    if kaye == "+":
        result = x + y
        print(result)
    elif kaye == "-":
        result = x - y
        print(result)
    elif kaye == ":":
        result = x / y
        print(result)
    elif kaye == "*":
        result = x * y
        print(result)


calculator(float(input("enter x:")), float(input("enter y:")), str(input("enter kaye:")))

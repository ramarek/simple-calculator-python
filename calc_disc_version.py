calc_map = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    ":": lambda x, y: x / y,
    "*": lambda x, y: x * y,
}

x = float(input("enter x:"))
y = float(input("enter y:"))
key = input("enter kaye:")
result = calc_map[key](x, y)
print(result)

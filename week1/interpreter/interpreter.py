expression = input("Enter math expression (e.g. 3 + 4): ")
parts = expression.strip().split(" ")
x_str, operator, z_str = parts
x = int(x_str)
z = int(z_str)
result = 0
if operator == "+":
    result = x + z
elif operator == "-":
    result = x - z
elif operator == "*":
    result = x * z
elif operator == "/":
    result = x / z
print(f"{result:.1f}")

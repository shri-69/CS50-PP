import sys
names = []

print("Enter names one per line (Ctrl+D to finish):")

try:

    while True:
        name = input()
        if name:
            names.append(name)
except EOFError:
    pass


if not names:
    sys.exit("No names entered... but you said you'd enter at least one!")


farewell = "Adieu, adieu, to "

if len(names) == 1:
    farewell += names[0]
elif len(names) == 2:
    farewell += f"{names[0]} and {names[1]}"
else:
    
    farewell += ", ".join(names[:-1])
    farewell += f", and {names[-1]}"

print(farewell)

user_answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer = user_answer.strip().lower()
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")

text = input("Input: ")
vowels = "aeiouAEIOU"
shortened = ""
for char in text:
    if char not in vowels:
        shortened += char

print(f"Output: {shortened}")

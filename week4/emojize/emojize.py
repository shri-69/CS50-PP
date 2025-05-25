import emoji
user_input = input("Enter your text:): ")
emojized_text = emoji.emojize(user_input, language='alias')
print("Emojized text:")
print(emojized_text)

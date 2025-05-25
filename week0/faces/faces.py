def convert(text):

    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


def main():

    user_input = input("What's on your mind? ")
    output = convert(user_input)
    print(output)
if __name__ == "__main__":
    main()

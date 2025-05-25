menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0.0

    print("Welcome to our Taqueria! (Press Ctrl-D to finish your order)")

    try:
        while True:
            item = input("Item: ").strip().title()


            if item in menu:
                total += menu[item]

                print(f"Total: ${total:.2f}")
            else:

                continue

    except EOFError:
        print("\nThanks for your order!")  
        print(f"Your total is: ${total:.2f}")

if __name__ == "__main__":
    main()

def main():
    while True:
        try:
            fuel_input = input("How much fuel? (format X/Y): ").strip()
            parts = fuel_input.split('/')
            if len(parts) != 2:
                raise ValueError("Expected format X/Y")

            num = int(parts[0])
            denom = int(parts[1])

            if denom == 0:
                raise ZeroDivisionError("Can't divide by zero - no infinite tanks allowed!")

            if num > denom:
                raise ValueError("Fuel used can't be more than tank capacity")
            percentage = round((num / denom) * 100)
            if percentage <= 1:
                print("E")  # Empty
            elif percentage >= 99:
                print("F")  # Full
            else:
                print(f"{percentage}%")

            break

        except ValueError as ve:

            print("Invalid input. Please use format X/Y with X ≤ Y.")
        except ZeroDivisionError:
            print("Denominator can't be zero. Try again.")
if __name__ == "__main__":
    main()

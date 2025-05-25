def main():
    # Getting user input for meal cost and tip preference
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    # Basic tip calculation
    tip = dollars * percent

    # Displaying the final result, nicely formatted
    print(f"Leave ${tip:.2f}")

# Converts dollar string to float (e.g., "$50.00" → 50.0)
def dollars_to_float(d):
    # Just removing the dollar sign and converting to float
    amount = d.replace("$", "")
    return float(amount)

# Converts percent string to float (e.g., "15%" → 0.15)
def percent_to_float(p):
    # Removing percent sign, then dividing by 100
    stripped = p.replace("%", "")
    return float(stripped) / 100

main()


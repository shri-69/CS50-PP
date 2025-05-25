from datetime import date, datetime
import sys
import inflect

p = inflect.engine()

def main():
    bday_input = input("Date of Birth (YYYY-MM-DD): ")

    try:
        minutes = get_minutes_since_birth(bday_input)
        print(f"{p.number_to_words(minutes, andword='').capitalize()} minutes")
    except ValueError:
        sys.exit("Invalid date format")

def get_minutes_since_birth(birthdate_str):
    
    try:
        birth_date = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    except Exception:
        raise ValueError("Bad date")

    today = date.today()


    delta = today - birth_date
    total_minutes = delta.days * 24 * 60
    return round(total_minutes)

if __name__ == "__main__":
    main()

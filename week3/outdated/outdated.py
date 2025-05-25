def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date_input = input("Date: ").strip()


            if '/' in date_input:
                parts = date_input.split('/')
                if len(parts) != 3:
                    raise ValueError("Incorrect slash format.")
                month, day, year = map(int, parts)
            elif ',' in date_input:
                month_part, year = date_input.split(',')
                year = int(year.strip())

                month_name, day = month_part.strip().split()
                day = int(day)

                if month_name not in months:
                    raise ValueError("Invalid month name.")
                month = months.index(month_name) + 1

            else:
                raise ValueError("Unknown date format.")

            if not (1 <= month <= 12) or not (1 <= day <= 31):
                raise ValueError("Month or day out of range.")

            print(f"{year:04}-{month:02}-{day:02}")
            break

        except (ValueError, IndexError):
            continue

if __name__ == "__main__":
    main()

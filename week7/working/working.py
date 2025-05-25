import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):

    pattern = r'^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$'

    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid time format")


    h1, m1, mer1, h2, m2, mer2 = match.groups()


    m1 = m1 if m1 else "00"
    m2 = m2 if m2 else "00"

    try:
        h1 = int(h1)
        m1 = int(m1)
        h2 = int(h2)
        m2 = int(m2)
    except ValueError:
        raise ValueError("Non-integer time components")

    if not (1 <= h1 <= 12) or not (0 <= m1 < 60) or not (1 <= h2 <= 12) or not (0 <= m2 < 60):
        raise ValueError("Invalid time values")


    start = to_24_hour(h1, m1, mer1)
    end = to_24_hour(h2, m2, mer2)

    return f"{start} to {end}"

def to_24_hour(hour, minute, meridiem):
    
    if meridiem == "AM":
        if hour == 12:
            hour = 0
    elif meridiem == "PM":
        if hour != 12:
            hour += 12
    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()

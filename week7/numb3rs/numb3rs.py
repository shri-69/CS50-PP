import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$'
    match = re.match(pattern, ip)

    if not match:
        return False
    parts = match.groups()
    for part in parts:
        try:
            num = int(part)
            if num < 0 or num > 255:
                return False
        except ValueError:

            return False

    return True

if __name__ == "__main__":
    main()

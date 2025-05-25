import sys
import csv
import os

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    if not os.path.isfile(input_file):
        sys.exit(f"Error: File '{input_file}' not found")

    cleaned_rows = []

    try:
        with open(input_file, newline='') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                try:
                    last, first = row["name"].split(", ")
                    house = row["house"]
                    cleaned_rows.append({"first": first, "last": last, "house": house})
                except ValueError:
                    continue

    except Exception as e:
        sys.exit(f"Something went wrong while reading the input file: {e}")
    try:
        with open(output_file, mode='w', newline='') as outfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in cleaned_rows:
                writer.writerow(student)
    except Exception as e:
        sys.exit(f"Couldn’t write to output file: {e}")
if __name__ == "__main__":
    main()

import sys
import os
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py data.csv")

    csv_file = sys.argv[1]
    if not csv_file.endswith(".csv"):
        sys.exit("Error: File must be a .csv file")
    if not os.path.isfile(csv_file):
        sys.exit(f"Error: File '{csv_file}' not found")

    try:
        with open(csv_file, newline='') as f:
            reader = csv.reader(f)
            table_data = []
            try:
                headers = next(reader)
            except StopIteration:
                sys.exit("Error: CSV file is empty")
            for row in reader:
                table_data.append(row)
            print(tabulate(table_data, headers=headers, tablefmt="grid"))

    except Exception as e:

        sys.exit(f"Error while reading the file: {e}")
if __name__ == "__main__":
    main()

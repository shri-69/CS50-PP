import sys
import os
def is_not_code(line):
    stripped = line.strip()
    return not stripped or stripped.startswith('#')

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")

    file_path = sys.argv[1]
    if not file_path.endswith(".py"):
        sys.exit("Error: Not a Python file (must end with .py)")
    if not os.path.isfile(file_path):
        sys.exit(f"Error: File '{file_path}' does not exist")
    code_line_count = 0

    try:
        with open(file_path, 'r') as python_file:
            for line in python_file:
                if not is_not_code(line):
                    code_line_count += 1
    except Exception as e:
        sys.exit(f"Error reading file: {e}")
    print(code_line_count)
if __name__ == "__main__":
    main()

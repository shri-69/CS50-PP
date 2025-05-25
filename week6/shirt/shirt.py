import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    input_img_path = sys.argv[1]
    output_img_path = sys.argv[2]
    allowed_exts = (".jpg", ".jpeg", ".png")


    in_ext = os.path.splitext(input_img_path)[1].lower()
    out_ext = os.path.splitext(output_img_path)[1].lower()

    if in_ext not in allowed_exts or out_ext not in allowed_exts:
        sys.exit("Error: Only .jpg, .jpeg, or .png files allowed")
    if in_ext != out_ext:
        sys.exit("Error: Input and output file extensions must match")

    if not os.path.exists(input_img_path):
        sys.exit(f"Error: Could not find the file '{input_img_path}'")

    try:
        original = Image.open(input_img_path)

        shirt = Image.open("shirt.png")
        cropped = ImageOps.fit(original, shirt.size)

        cropped.paste(shirt, (0, 0), shirt)
        cropped.save(output_img_path)

    except Exception as err:
        sys.exit(f"Something went wrong: {err}")

if __name__ == "__main__":
    main()

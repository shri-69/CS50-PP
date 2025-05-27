# 👕 shirt.py — Try On the "I took CS50" Shirt Virtually

After completing CS50, students at Harvard traditionally receive an iconic “I took CS50” t-shirt.  
With `shirt.py`, you can try on a virtual version of that shirt—no shipping required!

---

## 📜 Description

`shirt.py` overlays a shirt image (`shirt.png`, with a transparent background) onto a user-provided input photo.  
The script resizes and crops the input to match the shirt’s size so that the overlay aligns perfectly, and then saves the final image.

---

## 🛠️ Features

- Accepts **exactly two** command-line arguments:
  1. Path to the input image (`.jpg`, `.jpeg`, or `.png`)
  2. Path to the output image (same extension as input)

- Validates:
  - Correct number of arguments
  - Supported file extensions
  - Matching extensions between input and output
  - Existence of the input file

- Resizes and crops the input image to match `shirt.png` using Pillow’s `ImageOps.fit`
- Overlays the shirt onto the resized input
- Saves the final image to the specified output path

---

## 🧪 Usage

```bash
python shirt.py input_image output_image

Example
  python shirt.py myface.jpg myface_with_shirt.jpg
💡 Place shirt.png in the same folder as shirt.py and your images.

🔍 Error Handling
Condition                                           	Exit Message
Incorrect number of arguments	                        Usage: python shirt.py input_image output_image
Unsupported file types	                              Error: Only .jpg, .jpeg, or .png files allowed
File extensions don't match	                          Error: Input and output file extensions must match
Input file doesn’t exist	                            Error: Could not find the file 'filename'
Any other exception	                                  Something went wrong: <error>

📦 Requirements
Python 3.x
Pillow

Install with:
pip install Pillow

📁 Project Structure
├── shirt.py
├── shirt.png
├── myphoto.jpg
└── myphoto_with_shirt.jpg

📸 Tips for Best Results
Use a portrait-style photo facing forward
Make sure your photo is framed like a traditional ID picture
The better aligned you are to the shirt layout, the more realistic the result!

👨‍💻 Author
Created as part of CS50’s Introduction to Python programming.
By [SHRIYA DHAWAN]

📝 License
MIT License — Free to use for learning and fun.

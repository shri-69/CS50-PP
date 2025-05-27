# 👕 CS50 Shirtificate Generator

This project generates a **custom PDF certificate** (aka "shirtificate") that places a user's name over an image of a CS50 t-shirt, simulating a certificate that says the user took CS50!

---

## 📦 Features

- Creates a PDF in **A4 portrait format**
- Adds the title: **"CS50 Shirtificate"**
- Overlays user's name with the text: **"[Name] took CS50"** in white on top of the shirt image
- Output is saved as `shirtificate.pdf`

---

## 🖼 Preview

Your output will look similar to:

CS50 Shirtificate
[Image of shirt]
SHRIYA DHAWAN took CS50


---

## 🔧 Requirements

- Python 3
- [`fpdf2`](https://pypi.org/project/fpdf2/)

Install via:

```bash
pip install fpdf

🧪 How to Use
Make sure the image shirtificate.png is in the same directory.

Run the script:
python shirtificate.py
Enter your name when prompted, and it will generate shirtificate.pdf.

📁 File Structure
├── shirtificate.py        # Main script
├── shirtificate.png       # T-shirt image
├── shirtificate.pdf       # Output file
└── README.md              # Documentation

📝 Notes
Image is centered horizontally.
Text is white and centered over the shirt image.
You can customize font, positioning, or add decorations (e.g., borders).

📜 License
MIT License — open-source, free to use and modify.


---

### ✅ Optional Enhancements
If you'd like to add a little flair, consider:
- Adding a **border** using `pdf.rect(...)`
- Placing a **footer** like "Powered by Python & FPDF"
- Supporting long names by **scaling font size dynamically**

Let me know if you’d like help implementing any of these or packaging the project!

# 🧩 File Extension to Media Type Mapper (Python)

This simple Python program maps common file extensions (e.g., `.jpg`, `.pdf`, `.zip`) to their corresponding **media types** (also known as **MIME types**). If the file extension is unknown or missing, it defaults to `application/octet-stream`.

---

## 📄 File

- `extensions.py`

---

## 🔍 Purpose

Operating systems use file extensions (like `.jpg`, `.gif`, etc.) to identify file types.  
Web browsers and servers use **MIME types** (like `image/jpeg`) for the same purpose.  
This program bridges the gap by identifying the MIME type based on a file's extension.

---

## 🧠 How It Works

1. Prompts the user for a file name.
2. Normalizes the input by:
   - Stripping leading/trailing whitespace
   - Converting it to lowercase
3. Checks the file extension and maps it to a media type.

---

## 🧮 Supported Extensions

| File Extension | Media Type              |
|----------------|--------------------------|
| `.gif`         | `image/gif`              |
| `.jpg`, `.jpeg`| `image/jpeg`             |
| `.png`         | `image/png`              |
| `.pdf`         | `application/pdf`        |
| `.txt`         | `text/plain`             |
| `.zip`         | `application/zip`        |
| *(Other)*      | `application/octet-stream` |

---

## 📥 Example

```bash
$ python extensions.py
File name: document.PDF
application/pdf

$ python extensions.py
File name: image.jpeg
image/jpeg

$ python extensions.py
File name: archive.tar.gz
application/octet-stream

🚀 How to Run
Make sure you have Python 3 installed. Then run:
python extensions.py

📜 License
This project is free to use for educational and personal learning.

✍️ Author
[SHRIYA DHAWAN]

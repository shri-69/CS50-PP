# ▶️ watch.py — YouTube Embed URL Parser

This Python script allows you to extract an **embedded YouTube video URL** from HTML and convert it into a **shorter, shareable `youtu.be` URL** format.

Inspired by HTML embed code (like from the "Share > Embed" option on YouTube), this project helps reverse the embed back to the easily shareable form.

---

## 🧠 What It Does

From HTML that includes:

```html
<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
  It will extract the src URL and return:
  https://youtu.be/xvFZjo5PgG0

🛠️ How It Works
- Uses Python’s re module (regular expressions) to find the src attribute inside an <iframe> tag that contains a YouTube embed link.
- Converts the embedded URL format:
  https://www.youtube.com/embed/VIDEO_ID

to:
 https://youtu.be/VIDEO_ID

✅ Supported Embed Formats
The parse() function supports the following src formats:
http://youtube.com/embed/VIDEO_ID
https://youtube.com/embed/VIDEO_ID
https://www.youtube.com/embed/VIDEO_ID

🧪 Example
Input HTML
<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player"></iframe>

Output
https://youtu.be/xvFZjo5PgG0

📝 Usage
Run the script:
python watch.py

Then enter or paste HTML input when prompted:
HTML: <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
https://youtu.be/xvFZjo5PgG0

If no valid YouTube iframe embed is found, it returns:
None

📁 File Structure
├── watch.py      # Main script
└── README.md     # This file

🚫 Limitations
Only works for one embed per input.
Assumes src attributes are wrapped in double quotes (").
Does not validate malformed HTML or handle other video providers.

👨‍💻 Author
Part of Harvard’s CS50 problem set series. Practice in regular expressions and HTML parsing.

📜 License
MIT License — free to use and modify for educational purposes.

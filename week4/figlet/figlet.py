import sys
import pyfiglet
import random
available_fonts = pyfiglet.FigletFont.getFonts()
if len(sys.argv) == 1:
    font_choice = random.choice(available_fonts)
elif len(sys.argv) == 3:
    flag, selected_font = sys.argv[1], sys.argv[2]
    if flag not in ["-f", "--font"]:
        sys.exit("Error: Invalid flag. Use -f or --font to specify a font.")

    if selected_font not in available_fonts:

        sys.exit("Error: Font not found. Please choose a valid font name.")

    font_choice = selected_font
else:

    sys.exit("Usage: python figlet.py OR python figlet.py -f <fontname>")
try:
    user_text = input("Enter text to display: ")
except Exception as e:
    sys.exit(f"Something went wrong while getting your input: {e}")
fig = pyfiglet.Figlet(font=font_choice)
print(fig.renderText(user_text))

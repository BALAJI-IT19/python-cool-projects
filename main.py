# import the following libraries
# will convert the image to text string
import pytesseract

# adds image processing capabilities
from PIL import Image

from langdetect import detect

# opening an image from the source path
img = Image.open('cn_sc01.png')

# describes image format in the output
print(img)
# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)

# write text in a text file and save it to source path
with open('abc.txt', mode='w') as file:
    file.write(result)
    print(result)
read_file = open("abc.txt", "r")
x = read_file.read()

print(detect(x))

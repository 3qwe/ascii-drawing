from PIL import Image, ImageDraw, ImageFont 
import os 

chars = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" 

char_width = 5
char_height = 5

img_of_king = Image.open('C:/images/king.jpg') 


WIDTH, HEIGHT = img_of_king.size 
img_of_king = img_of_king.resize((int(WIDTH / char_width), int(HEIGHT / char_height)), Image.NEAREST)   
width, height = img_of_king.size
img = img_of_king.load()

ascii_img = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0)) 

fnt = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 5)

d = ImageDraw.Draw(ascii_img)


def getChar(value):
    return chars[int(value * (len(chars) / 256))]   


for i in range(height):
    for j in range(width):
        r, g, b = img[j, i]                      
        k = int((r + g + b) / 3)
        d.text((j * char_width, i * char_height), getChar(k), font=fnt, fill=(r, g, b)) 

ascii_img.save('king.png') 
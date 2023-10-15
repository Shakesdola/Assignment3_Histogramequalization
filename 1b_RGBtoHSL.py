
from PIL import Image
import math

# Open the RGB image
image = Image.open('Chateau.png')

# Separate the image into its RGB channels
red_channel, green_channel, blue_channel = image.split()

# Create blank images for HSL channels
h_channel = Image.new('L', image.size)
s_channel = Image.new('L', image.size)
l_channel = Image.new('L', image.size)

for x in range(image.width):
    for y in range(image.height):
        r = red_channel.getpixel((x, y)) / 255.0
        g = green_channel.getpixel((x, y)) / 255.0
        b = blue_channel.getpixel((x, y)) / 255.0

        cmax = max(r, g, b)
        cmin = min(r, g, b)
        delta = cmax - cmin

        
        
        # Calculate Hue (H)
        if delta == 0:
            h = 0
        elif cmax == r:
            h = 60 * (((g - b) / delta) % 6) 
        elif cmax == g:
            h = 60 * (((b - r) / delta) + 2)
        else:
            h = 60 * (((r - g) / delta) + 4)
        h_channel.putpixel((x, y), int((h / 360) * 255))

        
        # Calculate Lightness (L)
        l = (cmax + cmin) / 2.0
        l_channel.putpixel((x, y), int(255 * l))
        
        
        # Calculate Saturation (S)
        if delta == 0:
            s = 0
        else:
            s = delta / (1 - abs(2 * l - 1))
        s_channel.putpixel((x, y), int(255 * s))
        

       
        
# Save each channel separately
h_channel.save('H_channel.png')
s_channel.save('S_channel.png')
l_channel.save('L_channel.png')
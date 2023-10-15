
from PIL import Image
import math

# Open the HSL channels
h_channel = Image.open('H_channel.png')
s_channel = Image.open('S_channel.png')
l_channel = Image.open('L_channel.png')

# Create a blank RGB image
rgb_image = Image.new('RGB', h_channel.size)

for x in range(h_channel.width):
    for y in range(h_channel.height):
        h = (h_channel.getpixel((x, y)) / 255.0) * 360.0
        s = s_channel.getpixel((x, y)) / 255.0
        l = l_channel.getpixel((x, y)) / 255.0

        # Calculate the HSL to RGB conversion
        c = (1 - abs(2 * l - 1)) * s
        X = c * (1 - abs((h / 60) % 2 - 1))
        m = l - c / 2

        r, g, b = 0, 0, 0

        if 0 <= h < 60:
            r, g, b = c, X, 0
        elif 60 <= h < 120:
            r, g, b = X, c, 0
        elif 120 <= h < 180:
            r, g, b = 0, c, X
        elif 180 <= h < 240:
            r, g, b = 0, X, c
        elif 240 <= h < 300:
            r, g, b = X, 0, c
        else:
            r, g, b = c, 0, X

        r = int((r + m) * 255)
        g = int((g + m) * 255)
        b = int((b + m) * 255)

        # Set the RGB pixel in the reconstructed image
        rgb_image.putpixel((x, y), (r, g, b))

# Save or display the reconstructed RGB image
rgb_image.save('Reconstructed_RGB.png')
rgb_image.show()
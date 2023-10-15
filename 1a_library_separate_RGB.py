
from PIL import Image

# Open the RGB image
image = Image.open('Chateau.png')

# Split the image into RGB channels
red_channel, green_channel, blue_channel = image.split()

# Save each channel as a separate image
red_channel.save('red_channel.png')
green_channel.save('green_channel.png')
blue_channel.save('blue_channel.png')

# Optionally, you can also display the individual channel images using the default image viewer
red_channel.show()
green_channel.show()
blue_channel.show()

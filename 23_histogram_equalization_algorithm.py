from PIL import Image
import numpy as np

# Histogram equalization function
def histogram_equalization(channel):
    # Calculate the histogram of the image
    histogram, _ = np.histogram(channel, bins=256, range=(0, 256))
    
    # Calculate the cumulative distribution function (Computing the cumulative histogram)
    cdf = histogram.cumsum()
    
    # Perform histogram equalization
    equalized_pixels = np.uint8(cdf / (width * height) * 255)
    
    return Image.fromarray(equalized_pixels[channel])


# Open the grayscale image
image = Image.open('Aeroplane.png').convert('L')
width, height = image.size

# Create an image with the equalized pixels
equalized_image = histogram_equalization(image)

# Save or display the equalized image
equalized_image.save('equalized_Aeroplane.png')
equalized_image.show()




# Load the R, G, and B channels as grayscale images
red_channel = Image.open('red_channel.png').convert('L')
green_channel = Image.open('green_channel.png').convert('L')
blue_channel = Image.open('blue_channel.png').convert('L')

# Calculate the width and height
width, height = red_channel.size


# Apply histogram equalization to each channel
red_equalized = histogram_equalization(red_channel)
green_equalized = histogram_equalization(green_channel)
blue_equalized = histogram_equalization(blue_channel)

# Merge the equalized channels into an RGB image
equalized_image = Image.merge("RGB", (red_equalized, green_equalized, blue_equalized))

# Save the equalized RGB image
equalized_image.save('rgb_equalized.png')
equalized_image.show()




# Load the L, H, and S channels as grayscale images
l_channel = Image.open('L_channel.png').convert('L')
h_channel = Image.open('H_channel.png').convert('L')
s_channel = Image.open('S_channel.png').convert('L')

# Calculate the width and height
width, height = l_channel.size

# Apply histogram equalization to the L channel
l_equalized = histogram_equalization(l_channel)

# Reconstruct the image with the new L channel and the original H and S channels
rgb_equalized = Image.merge("RGB", (h_channel, s_channel, l_equalized))

# Convert the result to an RGB image
#rgb_equalized = hsl_equalized.convert("RGB")

# Save the equalized HSL image as "HSL_equalized.png"
rgb_equalized.save('HSL_equalized.png')
rgb_equalized.show()

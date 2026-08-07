from rembg import remove
from PIL import Image

# path to your input image
input_path = "p1.jpeg"
output_path = "output.png"

# open the image
input_image = Image.open(input_path)

# remove the background
output_image = remove(input_image)

# save the result
output_image.save(output_path)

print(f"Saved to {output_path}")
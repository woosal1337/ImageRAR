from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np

text_to_show = "Welcome"

# Load image in OpenCV
image = cv2.imread("Backgrounds/templatefaded.png")

# Convert the image to RGB (OpenCV uses BGR)
cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Pass the image to PIL
pil_im = Image.fromarray(cv2_im_rgb)

draw = ImageDraw.Draw(pil_im)
# use a truetype font
font = ImageFont.truetype("Fonts/KDA.ttf", 40)

# Draw the text
draw.text((200, 20), text_to_show, font=font)

# Get back the image to OpenCV
cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

cv2.imshow('Fonts', cv2_im_processed)
cv2.waitKey(0)

cv2.destroyAllWindows()
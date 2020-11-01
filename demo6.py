import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import time

## Make canvas and set the color
img = np.zeros((200,400,3),np.uint8)
b,g,r,a = 0,255,0,0

## Use cv2.FONT_HERSHEY_XXX to write English.
text = time.strftime("%Y/%m/%d %H:%M:%S %Z", time.localtime())
cv2.putText(img,  text, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (b,g,r), 1, cv2.LINE_AA)

## Use simsum.ttc to write Chinese.
fontpath = "./simsun.ttc"
font = ImageFont.truetype(fontpath, 32)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
draw.text((50, 100),  "OK", font = font, fill = (b, g, r, a))
img = np.array(img_pil)

## Display
cv2.imshow("res", img);cv2.waitKey();cv2.destroyAllWindows()
cv2.imwrite("res.png", img)
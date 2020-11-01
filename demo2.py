import cv2
import numpy as np

def  drawOpenCVText():
    # Create a black image
    img = np.zeros((640, 720, 3), np.uint8)
    #change the black image to white image by filling all values with 255
    img.fill(255)

    """                      
    Availble font lists
    FONT_HERSHEY_COMPLEX
    FONT_HERSHEY_COMPLEX_SMALL
    FONT_HERSHEY_DUPLEX
    FONT_HERSHEY_PLAIN
    FONT_HERSHEY_SCRIPT_COMPLEX
    FONT_HERSHEY_SCRIPT_SIMPLEX
    FONT_HERSHEY_SIMPLEX
    FONT_HERSHEY_TRIPLEX
    FONT_ITALIC
    """
    fontscale = 1.0
    # (B, G, R)
    color = (0, 0, 255)
    # select font
    fontface = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img, "FONT_HERSHEY_COMPLEX", (25, 40), fontface, fontscale, color)
    fontface = cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(img, "FONT_HERSHEY_COMPLEX_SMALL", (25, 80), fontface, fontscale, color)
    fontface = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(img, "FONT_HERSHEY_DUPLEX", (25, 120), fontface, fontscale, color)
    fontface = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(img, "FONT_HERSHEY_PLAIN", (25, 160), fontface, fontscale, color)
    fontface = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    cv2.putText(img, "FONT_HERSHEY_SCRIPT_COMPLEX", (25, 200), fontface, fontscale, color)
    fontface = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.putText(img, "FONT_HERSHEY_SCRIPT_SIMPLEX", (25, 240), fontface, fontscale, color)
    fontface = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, "FONT_HERSHEY_SIMPLEX", (25, 280), fontface, fontscale, color)
    fontface = cv2.FONT_HERSHEY_TRIPLEX
    cv2.putText(img, "FONT_HERSHEY_TRIPLEX", (25, 320), fontface, fontscale, color)
    fontface = cv2.FONT_ITALIC
    cv2.putText(img, "FONT_ITALIC", (25, 360), fontface, fontscale, color)

    cv2.namedWindow('putText Example')
    #display and save image

    cv2.imshow('putText Example', img)
    cv2.imwrite("output.jpg", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    drawOpenCVText()

if __name__ == '__main__':
    main()
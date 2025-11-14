import cv2 as cv
import numpy as np


# ------------------------------------------------- Reading and Displaying an Image -------------------------------------------------
image = cv.imread('download.jpg') #it will load the pic 
# if image is not None:
#     print('image read successfully')
    # cv.imshow('bike Image',image) # it will show the pic in a window
#     cv.waitKey(0) # it will wait for any key to be pressed to close the window
#     cv.destroyAllWindows() # it will destroy all the windows opened by opencv
# else :
#     print('image not read')


# ----------------------------------------------Save Image ---------------------------

# cv.imwrite('bike_copy.jpg',image)    # it will save the image with the name bike_copy.jpg


# ------------------------------- Image Dimensions --------------------------------------
# if we want to know the height , width and channels of the image then we can use shape attribute
# image_shape = image.shape
# print('Image Shape:', image_shape)  # it will print the shape of the image in the format (height, width,color channels)

# if image is not None:
#     h,w,c=image.shape
#     print(f"height: {h}\n width: {w}\n channels: {c}")



# ----------------------------------------- Greyscale Conversion --------------------------------------
# gray = cv.cvtColor(image,cv.COLOR_RGB2GRAY) # it will convert the image to greyscale
# cv.imshow('Gray Image',gray) # it will show the greyscale image in a window
# cv.waitKey(0)
# cv.destroyAllWindows()


# ------------------------------------- Resize Immages ----------------------------------

# input_image = input('Give the path of Images \n')

# if input_image :
#     load_image = cv.imread(input_image)
#     if load_image is not None:
#       resized= cv.resize(load_image,(100,100))
#                                 # (width,height)
#       cv.imshow('Original Image',load_image)
#       cv.imshow('Resized Image',resized)
#       cv.waitKey(0)
#       cv.destroyAllWindows()
# else:
#     print('Input Image is not found')   


# --------------------------------------- Croping Images ------------------------------
# open cv images are just numy array it will be 2D array or 3D array
#    croped_image = load_image[start Y:End Y, Start X: End X ]

# user_input = input('Enter your image path \n')

# if user_input is not None:
#     load_image = cv.imread(user_input)
#     croped_image = load_image[50:400,50:300]
#     cv.imshow('cropped image',croped_image)
#     cv.waitKey(0)
#     cv.destroyAllWindows()

# ------------------------------------------------ fliping Images -----------------------------


# user_input = input('Enter your image path \n')

# if user_input is not None:
#     load_image = cv.imread(user_input)
#     h,w = load_image.shape[:2]
#     center = (w/2,h/2)
#     M = cv.getRotationMatrix2D(center,120,2.0)
#     rotatePic  = cv.warpAffine(load_image,M,(w,h))

#     cv.imshow('Roated image',rotatePic)
#     cv.waitKey(0)
#     cv.destroyAllWindows()




# ---------------------------------------- Draw line o the pic -----------------------------------------


# user_input = input('Enter your image path \n')

# if user_input is not None:
#     load_image = cv.imread(user_input)
#     h,w = load_image.shape[:2]

#     pt1 =(20,10)
#     pt2 = (300,h)
#     color =(255,0,0)
#     thickness = 4

#     cv.line(load_image,pt1,pt2,color,thickness)

#     cv.imshow('Lined Pic ',load_image)
#     cv.waitKey(0)
#     cv.destroyAllWindows()


# --------------------------------------- Draw Rectengule -------------------------------
# user_input = input('Enter your image path \n')

# if user_input is not None:
#     load_image = cv.imread(user_input)

#     pt1 = (5,80)
#     pt2 =(80,100)
#     color =(0,0,255)
#     thickness = 2
#     cv.rectangle(load_image,pt1,pt2,color,thickness)
#     cv.imshow('rectangle',load_image)
#     cv.waitKey(0)
#     cv.destroyAllWindows()

# ---------------------------------- Work On Video --------------------------------
#  if we are using webCame for capturing video then we will pass "0" in source if we are using other outer sourse then we will use "1"


# cap = cv.VideoCapture(0)
# while True :
#     ret,frame = cap.read()
#     if not ret:
#       print('Could not read Frame')
#       break
#     cv.imshow('WebCame Feed',frame)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#        print('Quetting ----')
#        break
# cap.release()
# cv.destroyAllWindows()



# ----------------------------------------------- Image Filtering Process --------------------------------------
"""
Blurring (or smoothing) is an image processing technique used to:
          1) Reduce image noise and detail.
          2) Remove unwanted high-frequency content (edges, textures).
          3) Prepare an image for further processing (like edge detection or thresholding).
"""

# ----------------------------- GaussianBlur -----------------------------------
"""
In this every pixle will be added then take its averege then it will be replaced 
with that pixcle we want to blur it , it will not blur the surrounding pixcle 
"""

# Syntex :
"""
blurred_image = cv.GaussianBlur(image,(kernel_size_x,kernel_size_Y),sigma)
         1) in kernel we will put only odd values not even values
         2) sigma will be detect how much strong the blur will be if we will
            pass "0" then it will be detect by itself
         3)     (kernel_size_x,Kernel_size_y)
                     (3,3) ------> Light blur
                     (9,9) ------> Strong Blur
                     (21,21) ----> Super Blur 

"""

# blurred_image = cv.GaussianBlur(image,(21,21),10)

# cv.imshow('Original Image',image)
# cv.imshow('Blured Image',blurred_image)
# cv.waitKey(0)
# cv.destroyAllWindows()



# ----------------------------------------- Median Blur ------------------------------------

# blur_original = cv.imread('boy.png')

# blured= cv.medianBlur(blur_original,5)
# cv.imshow('Original image',blur_original)
# cv.imshow('Blured Image',blured)
# cv.waitKey(0)
# cv.destroyAllWindows()

# --------------------------------------- Sharpness Of Pic -----------------------------

pic_for_sharped = cv.imread('girl2.jpg')

kernel = np.array([[
     0,-1,0],
    [-1,5,-1],
    [0,-1,0] 
    ])

sharped_pic = cv.filter2D(pic_for_sharped,-99,kernel)
cv.imshow('Original Pic ',pic_for_sharped)
cv.imshow('sharped Pic',sharped_pic)
cv.waitKey(0)
cv.destroyAllWindows()









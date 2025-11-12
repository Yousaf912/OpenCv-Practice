import cv2 as cv


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
user_input = input('Enter your image path \n')

if user_input is not None:
    load_image = cv.imread(user_input)

    pt1 = (5,80)
    pt2 =(80,100)
    color =(0,0,255)
    thickness = 2
    cv.rectangle(load_image,pt1,pt2,color,thickness)
    cv.imshow('rectangle',load_image)
    cv.waitKey(0)
    cv.destroyAllWindows()






import cv2 as cv

# ---------------------------------------- Functions --------------------------------
# ----------------------- Show pic ----------
def show_pic(title, pic):
    cv.imshow(title, pic)
    cv.waitKey(0)
    cv.destroyAllWindows()
# ----------------------- Save pic ----------
def save_pic(filename, pic):
    cv.imwrite(filename, pic)
# ----------------------- Get Input ----------
def perform_task(title, pic):
    num = int(input('What do you want? \n 1. Save Image \n 2. Show Image\n'))
    if num == 1:
        file_name = input('Enter file name to save image: ')
        if file_name:
            save_pic(file_name, pic)
            print('Pic is Saved')
    elif num == 2:
        show_pic(title, pic)
    else:
        print('Invalid choice!')

# --------------- Get data for Rectangule Or line --------------------
def getData ():
            pt1_x = int(input('Enter the Value of Starting "X" '))
            pt1_y = int(input('Enter the Value of Starting "Y" '))
            pt2_x = int(input('Enter the Value of Ending "X" '))
            pt2_y = int(input('Enter the Value of Ending "Y" '))
            thickness = int(input('Enter the Thickness of the Line'))
            color_input = int(input('Chose Color of line \n 1. Blue \n 2.Green \n 3.Red \n'))
            if color_input == 1:
                color = (255,0,0)
            elif color_input == 2:
                color = (0,255,0) 
            elif color_input == 3:
                color = (0,0,255)
            if pt1_x is not None and pt1_y is not None and pt2_x is not None and pt2_y is not None and color is not None :
             pt1 = (pt1_x,pt1_y)
             pt2 = (pt2_x,pt2_y)    
            return(pt1,pt2,color,thickness)        
    

# ------------------------------------------------ Main Function --------------------------------------

user_input = input('Enter the path of Image \n')

if user_input:
    load_image = cv.imread(user_input)

    choice = int(input('What do you want to do ? \n '
                       '1. Change Color Of Pic \n '
                       '2. Resize the Pic \n'
                       '3. Crop the Pic \n'
                       '4. Flip image \n'
                       '5. Draw Line \n'
                       '6. Draw Ractangle \n'
                       
                       ))
# ---------------------------------------------------- Change Color --------------------------------
    if choice == 1:
        gray_pic = cv.cvtColor(load_image, cv.COLOR_RGB2GRAY)
        if gray_pic is not None:
            print('pic is recolred')
            perform_task('Grayscale Image', gray_pic)
# ---------------------------------------------------  Change Size ---------------------------------
    elif choice == 2:
        width = int(input('Enter the width: '))
        height = int(input('Enter the height: '))
        if width and height:
            resized_pic = cv.resize(load_image, (width, height))
            print('pic is resized')
            perform_task('Resized Image', resized_pic)
        else:
            print('Invalid height or width')
# ------------------------------------------ ------------Crop Pic  ---------------------------------
    elif choice ==3:

        start_y = int(input('Enter the start value of height \n'))
        end_y = int(input('Enter the End value of Height \n'))
        start_x = int(input('Enter the start value of width \n '))
        end_x = int(input('Enter the end value of width \n'))

        if start_y is not None and end_y is not None and start_x is not None and end_x is not None:
            croped_image = load_image[start_y:end_y,start_x:end_x]
            if croped_image is not None:
                print ('Image is croped')
                perform_task('Croped Image',croped_image)
# ----------------------------------------------------- Filp Image --------------------------------
    elif choice == 4:
        if load_image is not None :
         h,w = load_image.shape[:2]
         center =(h/2,w/2)
         axis = int(input('Enter the axis \n'))
         size_input =  int(input('Select the Size  \n 1. Half \n 2. Full \n 3. Original '))
         if size_input == 1:
            size = 0.5
         elif size_input == 2:
           size = 1.0
         elif size_input == 3:
            size = 2.0
         else:
            print("Invalid choice! Defaulting to full size.")
            size = 1.0

            
         if axis is not None :
          M = cv.getRotationMatrix2D(center,axis,size)
          fliped_pic = cv.warpAffine(load_image,M,(w,h))
          if fliped_pic is not None:
              print('Pic is flipped')
              perform_task('Flipped Pic',fliped_pic)
# --------------------------------------------------- Draw Line On Pic ----------------------------
    elif choice == 5:
        if load_image is not None:
             pt1, pt2, color, thickness = getData()
             lined_pic = cv.line(load_image,pt1,pt2,color,thickness)
             perform_task('Lined Pic',lined_pic)
# -------------------------------------------------- Draw Rectangel -------------------------------
    
    elif choice == 6:
        if load_image is not None:
            pt1,pt2,color,thickness = getData()
            rectangle_pic = cv.rectangle(load_image,pt1,pt2,color,thickness)
            perform_task('Rectangle Pic',rectangle_pic)

else:
    print('Please add valid input')

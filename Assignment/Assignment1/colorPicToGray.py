import cv2 as cv

user_input = input('Enter the Path of Image \n')

if user_input:
    load_image = cv.imread(user_input)
    if load_image is not None:
        gray_image = cv.cvtColor(load_image, cv.COLOR_BGR2GRAY)
        show_or_save = input('What do you want?\n 1. Save Image \n 2. Show Image \n')

        if int(show_or_save) == 1:
            file_name = input('Enter output file name (e.g., gray_image.png):\n')
            if not file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                file_name += '.png'  # default extension
            pic_saved = cv.imwrite(file_name, gray_image)
            if pic_saved:
                print('✅ Picture saved successfully!')
            else:
                print('❌ Failed to save picture.')
        elif int(show_or_save) == 2:
            cv.imshow('Gray Image', gray_image)
            cv.waitKey(0)
            cv.destroyAllWindows()
        else:
            print("❌ Invalid option.")
    else:
        print('❌ Image could not be loaded (check path).')
else:
    print('❌ No path entered.')

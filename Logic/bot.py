import win32api

from Logic import mouse_emulating
from Logic import Images
from PIL import Image, ImageGrab
import time, os
import tkinter

#global vars
#для корректирования координат при разных разрешениях
im1_multiplayerx1 = 0.44791666666666666666666666666667
im1_multiplayery1 = 0.64351851851851851851851851851852
im1_multiplayerx2 = 0.47395833333333333333333333333333
im1_multiplayery2 = 0.66203703703703703703703703703704

im2_multiplayerx1 = 0.52083333333333333333333333333333
im2_multiplayery1 = 0.64351851851851851851851851851852
im2_multiplayerx2 = 0.546875
im2_multiplayery2 = 0.66203703703703703703703703703704

speed = 0.1 #скорость бота

def logic():
        root = tkinter.Tk()
        resolution = (root.winfo_screenwidth(), root.winfo_screenheight()) #system resolution
        print(resolution)

        position = "left"
        image_compare = Images.CalcImageHash(Image.open("ComparePNG.png"))

        while True:

                time.sleep(speed)
                coords_image1 = (int(resolution[0]*im1_multiplayerx1), int(resolution[1]*im1_multiplayery1),
                                 int(resolution[0]*im1_multiplayerx2), int(resolution[1]*im1_multiplayery2))

                coords_image2 = (int((resolution[0]*im2_multiplayerx1)), int(resolution[1]*im2_multiplayery1),
                                 int(resolution[0]*im2_multiplayerx2), int(resolution[1]*im2_multiplayery2))

                print(coords_image1)
                if position == "left":
                        image1 = ImageGrab.grab(coords_image1) #сдвиг относительно get_pos() +30
                        #time_exec = int(time.time())
                        #image1.save(os.getcwd() + "\\cut_snap__ {}".format(time_exec) + ".png", "PNG")
                        #print(str(Images.CompareFiles(image1, image_compare)) +  "\\cut_snap__ {}".format(time_exec) + ".png")

                        if Images.CompareFiles(image1, image_compare) <= 20:
                                position = "right"
                                #print("LEFT_SIDE_SWITCHING")

                                mouse_emulating.mouse_pos((1029, 714)) #switch to opposite side (to right)


                elif position == "right":
                        image2 = ImageGrab.grab(coords_image2)

                        if Images.CompareFiles(image2, image_compare) <= 20:
                                #print("RIGHT_SIDE_SWITCHING")
                                position = "left"
                                mouse_emulating.mouse_pos((798, 714)) #switch to opposite side (to left)


                mouse_emulating.left_click()

                if win32api.GetAsyncKeyState(ord("q")) == 1 or win32api.GetAsyncKeyState(ord("Q")) == 1:
                        quit()





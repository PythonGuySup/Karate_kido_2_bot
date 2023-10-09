import win32api, win32con
import time

x_pad = 0
y_pad = 0
def click(func):
    def clicking():

        win32api.mouse_event(func()[0], 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(func()[1], 0, 0)
        #print(func.__name__)
    return clicking

def long_click(func):

    def long_clicking():
        win32api.mouse_event(func(), 0, 0)
        time.sleep(0.1)
        #print(func.__name__)

    return long_clicking
@click
def left_click():
   return win32con.MOUSEEVENTF_LEFTDOWN, win32con.MOUSEEVENTF_LEFTUP

@long_click
def left_down():
    return win32con.MOUSEEVENTF_LEFTDOWN


@long_click
def left_up(*args):
    return win32con.MOUSEEVENTF_LEFTUP



def mouse_pos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

#относительные координаты(относительно окна игры)
def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    return x, y

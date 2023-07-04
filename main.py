import pyautogui
import time
import keyboard

clickTime = 1000


def click(met, x_pos, y_pos):
    if met == "left":
        pyautogui.click(x_pos, y_pos)
    elif met == "right":
        pyautogui.click(button="right", x=x_pos, y=y_pos)
    elif met == "two-clicks":
        pyautogui.click(clicks=2, x=x_pos, y=y_pos)


def startAutoclicker():
    while not keyboard.is_pressed('esc'):
        x, y = pyautogui.position()
        click(method, x, y)
        time.sleep(clickTime / 1000)


def main():
    global clickTime, method

    while not keyboard.is_pressed('esc'):
        print("Welcome to the Autoclicker, before using it you need to setup some things (press ESC to stop the program)")
        clickTime = int(input(
            "Select the time between the clicks in ms (leave blank for 1000): ") or 1000)

        method = input(
            "Now select the method of the click between Right Btn./Left Btn./Two Clicks ('left', 'right', 'two-clicks', leave blank = 'left'): ")
        if method not in ['right', 'left', 'two-clicks']:
            print("Error: cannot detect method")
            return

        print("All good, Autoclicker started. Press ESC in the terminal to block it!")
        startAutoclicker()

    print("Program Blocked")


main()

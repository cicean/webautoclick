import pyautogui, time, threading


def updateNaWu():
    # active the game layout
    pyautogui.click(448, 38)
    #time.sleep(1)
    #pyautogui.click(178, 402)
    time.sleep(2)
    pyautogui.click(245, 854)
    time.sleep(3600)
    print(pyautogui.position())
    #pyautogui.moveTo(36, 125)
    #pyautogui.click()
    #print(pyautogui.position())
    #pyautogui.moveTo(448, 38)
    #pyautogui.moveTo(33, 38)



if __name__ == "__main__":
    print("Start run Test")
    while True:
        updateNaWu()
    print("Done one time clock!")
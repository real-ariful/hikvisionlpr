import pyautogui
import time


while True:
    pyautogui.size()
    pyautogui.click(100, 60)

    time.sleep(60)

    #Move to drag postion#Zoom -120
    pyautogui.moveTo(1360,200)
    pyautogui.click(1350,300, duration=0.1)
    #pyautogui.dragTo(1350, 320, duration=0.5, button='left') 
    #pyautogui.click(1350,350, duration=0.5)
    #pyautogui.dragTo(1360,300)
    #pyautogui.dragRel(0, 200, duration=0.5)  # drag mouse 10 pixels down

    ##pyautogui.moveTo(100, 150)
    ##pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
    ##pyautogui.dragTo(100, 150)
    ##pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down
    ##
    ## pyautogui.moveTo(240,155)
    ##  pyautogui.moveTo(240,420)
    ## pyautogui.moveTo(520,155) pyautogui.moveTo(520,420)
    ##120% zoom ---(300,310)  (655,310)(655,650) (300,650) (580,450)
    time.sleep(2)
    im = pyautogui.screenshot('test1.png', region=(260,150, 280, 300))
    time.sleep(60)

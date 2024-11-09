import pyautogui
import time
import keyboard
 
def ss ():
    captura_de_ecran = pyautogui.screenshot()
    captura_de_ecran.save('captura_de_ecran.png')
 
def cautare_google():
    if (pyautogui.locateOnScreen(r"search_bar.png")!=None):
        camp_google = pyautogui.locateOnScreen(r"search_bar.png")
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write("https://www.youtube.com/@DanCadar")
        pyautogui.press('enter')
        time.sleep(2)
        click_video()
        click_videoclip()
        click_subscribe()
 
def click_video():
    pyautogui.click(1794,545)
    time.sleep(1)
    pyautogui.scroll(-100)
 
def click_videoclip():
    time.sleep(2)
    pyautogui.click(1710,894)
 
def afisare_coordonate():
    while not keyboard.is_pressed('z'):
        print( pyautogui.position() )
        time.sleep(0.1)
 
def click_subscribe():
    time.sleep(1.5)
    pyautogui.click(1734, 625)
 
#afisare_coordonate()
cautare_google()
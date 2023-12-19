#info accompagnateur

import pyautogui  
import time

time.sleep(5)
pyautogui.write("nom")   #nom 
pyautogui.press('tab')

pyautogui.write("prenom")   #prénom 
pyautogui.press('tab')

pyautogui.write("NEPH")  #numero NEPH
pyautogui.press('tab')

pyautogui.write("jj/mm/aaaa")   #date inscrite sur le permis
pyautogui.press('tab')

pyautogui.click(939, 949)

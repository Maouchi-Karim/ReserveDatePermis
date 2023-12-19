import pyautogui, time, winsound, subprocess, pyperclip
from PIL import ImageGrab
from PIL import Image


k = 1
flag = 1

time.sleep(5)

pyautogui.press('win')
time.sleep(1)
pyautogui.write("mozila")
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)

for i in range(91, 96):
    pyautogui.write("https://candidat.permisdeconduire.gouv.fr/api/v1/candidat/creneaux?code-departement=0")
    pyautogui.write(str(i))
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(0.7)
    pyautogui.click(123, 222)
    time.sleep(0.7)
    pyautogui.hotkey('ctrl', 't')

pyautogui.hotkey('ctrl', 'w')
time.sleep(3)

while (flag):
    
    for j in range(1, 6):
        pyautogui.hotkey('ctrl', str(j))
        pyautogui.press('f5')
        time.sleep(1)
        pyautogui.click(133, 274)
        pyautogui.click(133, 274)


        time.sleep(0.5)


        screenshot1 = ImageGrab.grab()
        pix_reco  = screenshot1.getpixel((639, 615))

        screenshot2 = ImageGrab.grab()
        many_req  = screenshot2.getpixel((639, 615))

        texte_copie = pyperclip.paste()
        value = 90 + j
        

        if texte_copie != "[]" and pix_reco != (255, 255, 255) and texte_copie != '{ "message": "Too many requests!" }' :
         
            print("GO! GO! GO!")     
            winsound.Beep(500, 300)
            subprocess.run(["python", "connection.py"])
            
            time.sleep(1)

            for i in range(4):
                pyautogui.press('down')
                time.sleep(0.2)


            pyautogui.click(1588, 1004)
            time.sleep(2)
            pyautogui.click(795, 373)
            pyautogui.write(str(value))
            pyautogui.press('enter')
            time.sleep(0.4)
            pyautogui.press('enter')
            time.sleep(0.4)
            pyautogui.click(1180, 450)
            time.sleep(0.4)
            pyautogui.click(477, 609)
            time.sleep(0.4)
            pyautogui.click(985, 945)
            time.sleep(0.4)
            pyautogui.click(768, 659)
            time.sleep(0.4)
            subprocess.run(["python", "info_accomp.py"])
            time.sleep(0.4)
            for l in range (4):
                pyautogui.press('down')


            time.sleep(0.4)
            pyautogui.click(403, 781)
            time.sleep(0.4)
            pyautogui.click(430, 858)
            time.sleep(0.4)
            pyautogui.click(1023, 942)
            exit()


        if pix_reco == (255, 255, 255) :
            subprocess.run(["python", "connection.py"])
            for k in range (6):
                pyautogui.hotkey('ctrl','w')
            subprocess.run(["python", "escale.py"])
            flag = 0
    
    time.sleep(5)




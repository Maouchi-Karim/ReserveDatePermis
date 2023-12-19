import pyautogui, time, keyboard
from PIL import ImageGrab
from PIL import Image



captcha = Image.open("captcha.png")
print("a")

pyautogui.press('win')
time.sleep(0.8)
pyautogui.write("mozila")
time.sleep(0.6)
pyautogui.press('enter')
time.sleep(3)

pyautogui.write("https://candidat.permisdeconduire.gouv.fr/")
pyautogui.press('enter')
time.sleep(5)

screenshot = ImageGrab.grab()
pixel_color = screenshot.getpixel((56, 490))

print(pixel_color)
if pixel_color != (22, 22, 22):
    pyautogui.write("mail")      #pour un mail de la forme mail@gmail.com
    keyboard.press_and_release('alt gr + à')
    pyautogui.write("gmail.com")
    pyautogui.press('tab')
    pyautogui.write("mdp")   #mot de passe
    time.sleep(0.3)
    pyautogui.press('tab')
    time.sleep(0.3)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')

    time.sleep(3)

    pyautogui.click(972, 961)

    time.sleep(3)


    screenshot = ImageGrab.grab()            #résout un captcha grace à l'extension : Buster: Captcha Solver for Humans
    pixel_color = screenshot.getpixel((56, 490))

    while(pixel_color != (22, 22, 22)):
        pyautogui.click(847, 778)
        time.sleep(1.5)
        pyautogui.click(985, 787)
        time.sleep(3)


        verif_captcha = ImageGrab.grab(bbox=(719, 561, 1170, 671))   
        verif_captcha.save("verif_captcha.png")
        time.sleep(0.5)
        screenshot = ImageGrab.grab()
        pixel_color = screenshot.getpixel((56, 490))
        time.sleep(0.5)



    time.sleep(0.5)

    pyautogui.click(963, 755)

time.sleep(1)






"""verif_captcha = ImageGrab.grab(bbox=(721, 547, 721 + 447, 547 + 108))
verif_captcha.save("verif_captcha.png")

time.sleep(3)
if captcha == verif_captcha :
    print("oui")
else : 
    print("non")
    
while(verif_captcha != captcha ):
    
    print("je suis dans le boucle")
    pyautogui.click(847, 778)
    time.sleep(1)
    pyautogui.click(985, 787)
    time.sleep(3)
    verif_captcha = ImageGrab.grab(bbox=(721, 547, 721 + 447, 547 + 108))
    verif_captcha.save("verif_captcha.png")
    time.sleep(30)"""







        
    

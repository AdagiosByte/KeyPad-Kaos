import pyautogui
import time

gameOver = False
#start game
pyautogui.click(520,500)

while gameOver == False:
#for x in range(0,6):
    a = pyautogui.screenshot()
    
    num = 1
    targetX = {0:320,1:520,2:720,3:380,4:510,5:660,6:390,7:510,8:630}
    targetY = {0:500,1:400,2:300}
    #pyautogui.moveTo(320,500) # 1
    #pyautogui.moveTo(520,500) # 2
    #pyautogui.moveTo(720,500) # 3
    #pyautogui.moveTo(380,400) # 4
    #pyautogui.moveTo(510,400) # 5
    #pyautogui.moveTo(660,400) # 6
    #pyautogui.moveTo(390,300) # 7
    #pyautogui.moveTo(510,300) # 8
    #pyautogui.moveTo(630,300) # 9
    
    for num in range(0,9):
    #z,y = pyautogui.position()
        numy = num % 3
        i = a.getpixel((targetX[num],targetY[numy]))
        
        if i[0] < 50 and i[1] < 50 and i[2] < 50:
            t = str(1 + num)
            print(t)
            pyautogui.press(t)
            break
    #print(i)
    #time.sleep(1)
    a = pyautogui.screenshot()
    #check for game over
    i = a.getpixel((520,500))
    if i[0] > 50 and i[0] < 100:
        gameOver = True
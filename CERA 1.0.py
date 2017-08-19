import pyautogui as p

x,y=p.locateCenterOnScreen('C:\\Users\\PM\\Desktop\\yourpng.PNG')
p.click(x,y)

p.typewrite('BOT: Hii Harikaa !!!!!')
p.press('enter')


count = 0
while count < 100:
    p.typewrite('HAI DUDE! ')
    p.press('enter')
    print(count)
    count += 1

import pyautogui as p

x,y=p.locateCenterOnScreen('C:\\Users\\PM\\Desktop\\2.PNG')
p.click(x,y)

p.typewrite('BOT: Hii Harikaa !!!!!')
p.press('enter')


count = 0
while count < 100:
    p.typewrite('good night harika')
    p.press('enter')
    p.typewrite('sweet dreams')
    p.press('enter')
    print(count)
    count += 1
p.typewrite('Bye harika !!!!!')
p.press('enter')
p.typewrite('BOT:I AM CERA 1.0 CREATED BY DILEEP :) ')
p.press('enter')

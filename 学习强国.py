
import pyautogui
import time
import cv2
import random

#part 1打开学习强国

time.sleep(3)
click1=pyautogui.locateCenterOnScreen(r'G:\study\xxqg\1.png',region=(0, 0, 367, 1048),confidence=0.9)
print(click1,"逍遥模拟器坐标")#逍遥模拟器坐标
pyautogui.doubleClick(click1)
time.sleep(10)
click2=pyautogui.locateCenterOnScreen(r'G:\study\xxqg\2.png',region=(114, 70, 1750-114, 415-70),confidence=0.9)
print(click2,"学习强国坐标")
pyautogui.click(click2)
time.sleep(2)


#part 2 我要选读文章 12分
time.sleep(2)

huadong1=(933,866)
def hua():#定义滑动函数
    pyautogui.moveTo(huadong1)
    pyautogui.dragRel(40+random.randint(-20,20),-500+random.randint(-50,50),duration=1)#滑动
    time.sleep(1+random.randint(-1,2))

pyautogui.click(778,148)#要闻
b=0
while b<2:
    a=230
    while a<900:
        time.sleep(2)
        pyautogui.click(930,a)#点击第一个新闻

        time.sleep(1)

        hua()
        hua()
        hua()
        time.sleep(2)

        pyautogui.click(702,90)#返回
        a=a+120
    time.sleep(2)
    b=b+1
    pyautogui.scroll(-2)#滚动



time.sleep(2)
#part 3  视听学习 12分
pyautogui.click(1071,1019)#点击电视台
time.sleep(3)
c=0
while c<7:
    pyautogui.click(950,400)#点击第一个新闻
    time.sleep(90+random.randint(-10,20))#等待1min
    pyautogui.click(702,90)#返回
    time.sleep(1)
    pyautogui.moveTo(937,509)
    pyautogui.scroll(-2)#滚动
    time.sleep(2)   
    c=c+1



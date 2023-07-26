import pyautogui
import time
import cv2
import numpy as np

def load_groups():
    with open("groups.txt", "r") as file:
        content = file.read()
        groupList = content.split()
        print(groupList)
        return groupList
    
def goToGroupWebSide(groupId):
    X = 1455
    Y = 58  
    pyautogui.moveTo(X, Y)
    pyautogui.click()
    print('Open pasek')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    time.sleep(1)
    pyautogui.typewrite("https://www.facebook.com/groups/"+str(groupId))
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

def fakeClick():
    X = 1300
    Y = 600
    pyautogui.moveTo(X, Y)
    pyautogui.click()

def moveAndClick(x,y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def searchImage(path):
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    element = pyautogui.locateOnScreen(path)
    print(element)
    cv2.rectangle(
        screenshot,
        (element.left, element.top),
        (element.left + element.width, element.top + element.height),
        (0,255,255),
        2
    )

    return element.left + (element.width/2), element.top + (element.height /2)
        
    cv2.imshow('Screenshot', screenshot)
    cv2.waitKey(0)

def writeText(text):
    pyautogui.typewrite(text)

groupList = load_groups()

for groupId in groupList:
    try:
        main(groupId)
    except:
        print('cos poszlo nie tak')




def main(groupId):
    print(groupId)
    goToGroupWebSide(groupId)
    fakeClick()
    time.sleep(5)

    x,y = searchImage('assets/napiszCos.png')
    moveAndClick(x,y)
    time.sleep(2)
    writeText('Ala ma kota kot ma ale')

    x,y = searchImage('assets/zieloneZdjecia.png')
    moveAndClick(x,y)
    time.sleep(2)

    x,y = searchImage('assets/fbAddImage.png')
    moveAndClick(x,y)
    time.sleep(2)

    IMAGE_PATH = 'C:\\Users\\Lorek\\Desktop\\fbAutoPoster\\Selenium\\assets\\duszek.jpg'
    writeText(IMAGE_PATH)
    time.sleep(1)
    pyautogui.press('enter')

    x,y = searchImage('assets/submitButton.png')
    moveAndClick(x,y)
    time.sleep(10)
    
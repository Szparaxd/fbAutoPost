import pyautogui
import time
import cv2
import numpy as np
import random
import pyperclip

textList = [
  {
    "text": "Przebieg: 160 tys km, Cena: 76900 zl \nhttps://samochody.pl/samochody-osobowe/BMW/4%20Seria/Gorz%C3%B3w%20Wielkopolski/bmw-4-seria-coupe-gorzow-wielkopolski/ij843A_4v/pl",
    "img_path": ""
  },
  {
    "text": "BMW Seria 4, przebieg: 160000km, Cena: 76900 zl \nhttps://samochody.pl/samochody-osobowe/BMW/4%20Seria/Gorz%C3%B3w%20Wielkopolski/bmw-4-seria-coupe-gorzow-wielkopolski/ij843A_4v/pl",
    "img_path": ""
  },
  {
    "text": "Mazda 6 z przebiegiem: 152.000 km, o pojemnosci 1800 cm3 \nCena: 9300 zl\n https://samochody.pl/samochody-osobowe/Mazda/6/Lutomiersk/mazda-6-kombi-lutomiersk/vuoVHC44P/pl",
    "img_path": ""
  },
  {
    "text": "Hyundai ix35 z przebiegiem: 121 tys km z silnikiem benzynowym o pojemnosci 1591cm3\n Rok produkcji: 2012 Cena: 44.900 zl\n https://samochody.pl/samochody-osobowe/Hyundai/ix35/%C5%81%C3%B3d%C5%BA/hyundai-ix35-suv-lodz/sFilXBNsf/pl",
    "img_path": ""
  },
  {
    "text": "Renault Megane III \nPrzebieg: 142200 km, poj,: 1,6 BENZYNA, moc: 110 KM\nCena: 34800 zl\n https://samochody.pl/samochody-osobowe/Renault/Megane/%C5%81%C3%B3d%C5%BC/renault-megane-hatchback-lodz/xpLOVfeWi/pl",
    "img_path": ""
  },
  {
    "text": "Cena: 34800 zl\nhttps://samochody.pl/samochody-osobowe/Renault/Megane/%C5%81%C3%B3d%C5%BC/renault-megane-hatchback-lodz/xpLOVfeWi/pl",
    "img_path": ""
  },
  {
    "text": "Fiat Panda II, przebieg: 200.000km, pojemnosc: 1100 cm3\nCena: 6900zl \n https://samochody.pl/samochody-osobowe/Fiat/Panda/Lutomiersk/fiat-panda-lutomiersk/WkrfIE3xQ/pl",
    "img_path": ""
  },
  {
    "text": "Czy zdarzylo Ci sie kiedys zastanawiac, jaki jest dokladny model, marka, rok produkcji czy pojemnosc silnika pojazdu, ktory wlasnie minal Cie na ulicy?\n\nTeraz mozesz to zrobic w mgnieniu oka, dzieki naszej darmowej platformie !\nhttps://auto-info.gratis/",
    "img_path": ""
  },
  {
    "text": "Wiedziales ze, podajac numer z tablicy rejestracyjnej mozesz uzyskac: marke, model, rok produkcji, date pierwszej rejesracji pojazdu ?\nhttps://www.facebook.com/auto.info.gratis24",
    "img_path": ""
  },
  {
    "text": "Zgubiles lub znalazles tablice rejestracyjna? Zamiesc darmowe ogloszenie !\nhttps://www.facebook.com/groups/zgubiono.znaleziono.tablice.rejestracyjna",
    "img_path": ""
  },
  {
    "text": "Byles Swiadkiem zle zaparkowanego pojazdu ? Kierowca bez uprawnien stal na 'kopercie' ?\nZrob zdjecie i dodaj do naszej bazy a my naglosnimy ta sytuacje.\nhttps://auto-info.gratis/zle_parkowanie/",
    "img_path": ""
  },
  {
    "text": "Skradziono Twoje auto ? Pomoz Sobie i innym, dodaj zgloszenie do bazy.\nNie obiecujemy ze uda sie je odnalezc ale moze pomoze to w wykryciu sprawcow\nhttps://auto-info.gratis/skradziony_pojazd/",
    "img_path": ""
  },
  {
    "text": "Dodaj informacje o miejscu i czasie odnalezienia tablicy rejestracyjnej.\nPomozesz w ten sposob znalezc pojazd i wlasciciela do ktorego nalezy.\nhttps://auto-info.gratis/znaleziona_rejestracja/",
    "img_path": ""
  },
  {
    "text": "Dodaj informacje o miejscu i czasie zgubienia tablicy rejestracyjnej. Naglosnimy sprawe aby pomcc Ci jak najszybciej odzyskac zgube.\https://auto-info.gratis/zgubiona_rejestracja/",
    "img_path": ""
  },
  {
    "text": "Dobra wiadomosc dla wszystkich milosnikow motoryzacji i wlascicieli samochodow.\nOd tego roku warsztaty samochodowe zarejestrowane w Krajowym Rejestrze Napraw Pojazdow maja mozliwosc wystawiania raportow z naprawy w formie elektronicznej.\nDzieki temu mozemy jeszcze latwiej sledzic historie napraw naszych pojazdow i zachowac wszystkie niezbedne dokumenty w jednym miejscu.\n\nPrzy najblizszej okazji popros warsztat o wpisanie reportu z naprawy do KRNP\nwww.krnp.pl\n#wybierambezpiecznywarsztat",
    "img_path": ""
  },
  {
    "text": "Dobra wiadomosc dla wszystkich milosnikow motoryzacji i wlascicieli samochodow.\nOd tego roku warsztaty samochodowe zarejestrowane w Krajowym Rejestrze Napraw Pojazdow maja mozliwosc wystawiania raportow z naprawy w formie elektronicznej.\nDzieki temu mozemy jeszcze latwiej sledzic historie napraw naszych pojazdow i zachowac wszystkie niezbedne dokumenty w jednym miejscu.\n\nPrzy najblizszej okazji popros warsztat o wpisanie reportu z naprawy do KRNP\nwww.krnp.pl\n#wybierambezpiecznywarsztat",
    "img_path": ""
  },
  {
    "text": "Dobra wiadomosc dla wszystkich milosnikow motoryzacji i wlascicieli samochodow.\nOd tego roku warsztaty samochodowe zarejestrowane w Krajowym Rejestrze Napraw Pojazdow maja mozliwosc wystawiania raportow z naprawy w formie elektronicznej.\nDzieki temu mozemy jeszcze latwiej sledzic historie napraw naszych pojazdow i zachowac wszystkie niezbedne dokumenty w jednym miejscu.\n\nPrzy najblizszej okazji popros warsztat o wpisanie reportu z naprawy do KRNP\nwww.krnp.pl\n#wybierambezpiecznywarsztat",
    "img_path": ""
  },
  {
    "text": "Dobra wiadomosc dla wszystkich milosnikow motoryzacji i wlascicieli samochodow.\nOd tego roku warsztaty samochodowe zarejestrowane w Krajowym Rejestrze Napraw Pojazdow maja mozliwosc wystawiania raportow z naprawy w formie elektronicznej.\nDzieki temu mozemy jeszcze latwiej sledzic historie napraw naszych pojazdow i zachowac wszystkie niezbedne dokumenty w jednym miejscu.\n\nPrzy najblizszej okazji popros warsztat o wpisanie reportu z naprawy do KRNP\nwww.krnp.pl\n#wybierambezpiecznywarsztat",
    "img_path": ""
  }
]



def load_groups():
    with open("groups.txt", "r") as file:
        content = file.read()
        groupList = content.split()
        print(groupList)
        return groupList
    
def goToGroupWebSide(groupId):
    X = 268
    Y = 63  
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
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

groupList = load_groups()



for groupId in groupList:
    try:
        random_time_1 = random.randint(40,65)
        random_time_2 = random.randint(45,75)

        print(groupId)
        goToGroupWebSide(groupId)
        fakeClick()
        time.sleep(random_time_1)

        x,y = searchImage('assets/napiszCos.png')
        moveAndClick(x,y)
        time.sleep(3)

        post_element = random.choice(textList)

        writeText(post_element['text'])
        time.sleep(random_time_2)

        if post_element['img_path']:
            x,y = searchImage('assets/zieloneZdjecia.png')
            moveAndClick(x,y)
            time.sleep(2)

            x,y = searchImage('assets/fbAddImage.png')
            moveAndClick(x,y)
            time.sleep(2)

            writeText(post_element['img_path'])
            time.sleep(1)
            pyautogui.press('enter')

        x,y = searchImage('assets/submitButton.png')
        moveAndClick(x,y)
        time.sleep(35)

        # x,y = searchImage('assets/komentarz.png')
        # moveAndClick(x,y)
        # time.sleep(3)
        # writeText('kom')
        # time.sleep(12)
    
    except:
        print('Pominięto dla grupy' + str(groupId))
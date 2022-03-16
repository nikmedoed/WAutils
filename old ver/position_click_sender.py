from time import sleep
from pyautogui import *
import autopy
from imageToClipboard import imageToC
import pyperclip

positions = {
    'search': (380, 206),
    'user': (376, 336),
    'chat': (912, 991),
    'clean': (653, 207),
    'attach': (1571, 151)
}

PAUSE = 1

def send(txtList):
    for i in txtList:
        if "`photo`" in i:
            # imageToC(i[8:])
            # sleep(2)
            keyDown('ctrl')
            press('v')
            sleep(0.2)
            keyUp('ctrl')
            sleep(2)
            press('enter')
            sleep(3)
        else:
            # pyperclip.copy(i)
            # hotkey('ctrl', 'v')
            for part in i.split('\n'):
                autopy.key.type_string(part)
                hotkey('shift', 'enter')
            press('enter')


# Если браузер уже открыт на нужной странице на главыном экране 1920*1080
def sender(base):
    with open("messages/contracts/mes.txt", "r", encoding="utf-8") as m:
        txtList = list(map(lambda x: x.strip(), m.read().split("===")))
    for i in base:
        click(positions['search'])
        click(positions['search'])
        hotkey('ctrl', 'a')
        press('backspace')
        autopy.key.type_string(i)
        sleep(3)
        click(positions['user'])
        sleep(2)
        click(positions['chat'])
        click(positions['chat'])
        send(txtList)
        print(i)


if __name__ == "__main__":
    with open("base/base.txt", "r", encoding="utf-8") as b:
        # base = list(map(lambda x: x.split("\t"), b.read().split("\n")))
        base = b.read().split("\n")
    print(sender(base))
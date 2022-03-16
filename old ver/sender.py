from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def send(txtList, browser):
    inp = browser.find_element_by_xpath('//footer/div[1]/div[2]/div/div[2]')

    for i in txtList:
        inp.click()
        sleep(1)
        for part in i.split('\n'):
            inp.send_keys(part)
            ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(
                Keys.ENTER).perform()
        inp.send_keys("\n")
        # browser.find_element_by_xpath('//footer/div[1]/div[3]/button').click()

def sender(base):
    with open("messages/contracts/mes.txt", "r", encoding="utf-8") as m:
        txtList = list(map(lambda x: x.strip(), m.read().split("===")))
    browser = webdriver.Chrome()
    browser.get('https://web.whatsapp.com/')
    input("enter как авторизируешься")
    search = browser.find_element_by_xpath('//div[1]/div/label/div')
    for i in base:
        search.clear()
        try:
            mess = getMesList(txtList, i)
            search.send_keys(i[2])
            sleep(2)
            pers = browser.find_elements_by_xpath('//div[2]/div[1]/div/span/span/span')
            pers[0].click()
            sleep(1) # готовы отправлять
            send(mess, browser)
            print(i)
            # res.append(te)
        except:
            print(i, "Неудачно")
    browser.close()

def getMesList (txtList, person):
    return list(map(lambda x: x.replace("#", person[0]).replace("$", person[1]), txtList))

if __name__ == "__main__":
    with open("base/base.txt", "r", encoding="utf-8") as b:
        base = list(map(lambda x: x.split("\t"), b.read().split("\n")))
    print(sender(base))
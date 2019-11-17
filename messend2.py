from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

with open("../smsbase.txt", "r", encoding="utf8") as b:
    base = list(map(lambda x: x.split("\t"), b.read().split("\n")))

with open("sms.txt", "r", encoding="utf8") as m:
    sms = m.read()

browser = webdriver.Chrome()
browser.get('https://messages.google.com/web/conversations/new')
input("введите, как будете готовы")

for i in base:
    chat = browser.find_element_by_xpath('/html/body/mw-app/div/main/mw-main-container/div[1]/mw-main-nav/div/mw-fab-link/a')
    chat.click()
    sleep(2)
    search = browser.find_element_by_xpath('//div/input')
    search.click()
    search.send_keys(i)
    send=False
    while not(send):
        try:
            sleep(2)
            pers = browser.find_elements_by_xpath(
                '/html/body/mw-app/div/main/mw-main-container/div[1]/mw-new-conversation-container/div/mw-contacts-list/div/mw-contact-row/div/div')
            if len(pers)==0:
                print(i)
                search.clear()
            else:
                pers[0].click()
                sleep(3)
                inp = browser.find_element_by_xpath(
                    '/html/body/mw-app/div/main/mw-main-container/div[1]/mw-conversation-container/div/div/mws-message-compose/div[2]/div/mws-autosize-textarea/textarea')
                for part in sms.strip().split('\n'):
                    inp.send_keys(part)
                    ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(
                        Keys.ENTER).perform()
                inp.send_keys('\n')
            send=True
        except:
            sleep(10)
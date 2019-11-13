from selenium import webdriver
from time import sleep

def checkBase(base):
    browser = webdriver.Chrome()
    browser.get('https://web.whatsapp.com/')
    input("enter как авторизируешься")
    inp = browser.find_element_by_xpath('//div[1]/div/label/input')
    res = []
    inp.click()
    for i in base:
        inp.send_keys(i)
        sleep(2)
        pers = browser.find_elements_by_xpath('//div[2]/div[1]/div/span/span/span')
        te = '%s\t%s' % (i.split(' - ')[1], len(pers))
        print(te)
        res.append(te)
        inp.clear()
    browser.close()
    # print(res)
    with open('verificated.txt', 'w', encoding="utf-8") as f:
        f.write('\n'.join(res))
    return res

if __name__ == "__main__":
    with open("../base.txt", "r", encoding="utf8") as b:
        base = b.read().split("\n")
    checkBase(base)
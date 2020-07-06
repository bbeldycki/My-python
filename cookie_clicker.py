# action chains
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "D:\programy\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5) # czekamy 5 sec
# robimy to bo np. stronka musi sie zaladowac
# to daje czas na to wszystko

cookie = driver.find_element_by_id("bigCookie")
count_cookie = driver.find_element_by_id("cookies")

items = [driver.find_element_by_id("productPrice"+str(i)) for i in range(1,-1,-1)]


# lista akcji
actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(count_cookie.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
        

#actions.click() # klik myszy gdziekolwiek jest
#actions.perform() # wykona akcje

#import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=r'C:/Users/hanna/Documents/ChromeDriver/chromedriver.exe')  # Optional argument, if not specified will search path.


#connect to dominion
driver.implicitly_wait(10) # seconds
driver.get("https://dominion.games")
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'username-input')))

loginForm = driver.find_element_by_name('loginForm')
_inputs = driver.find_elements_by_xpath('//form[@name="loginForm"]//input')
_inputs[0].send_keys("cavegiraffe")
_inputs[1].send_keys("Hh100896")
loginForm.submit()
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'tab-button')))

#start bot game
bot_match = driver.find_element(By.XPATH, "//button[contains(.,'1 Bot')]")
bot_match.click()
start = driver.find_element(By.XPATH, "//*[contains(text(), 'Start Game')]")
start.click()

#get/print cards in supply
supply = driver.find_elements_by_class_name("visible-supply")
driver.implicitly_wait(10)
cardNames = []
for i in range(len(supply)):
    try:
        cardName= supply[i].find_element_by_class_name("full-card-name").text
    except:
        cardName= supply[i].find_element_by_class_name("landscape-name").text
    print(cardName)
    cardNames.append(cardName)
print(len(cardNames))

#buy phase stuff
#autoplay treasure
autoTreasure = driver.find_element(By.XPATH, "//*[contains(text(), 'Autoplay Treasures')]")
autoTreasure.click()

#buy a card
for i in range(len(supply)):
    cardCost = 0
    try:
        cardCost = int(supply[i].find_element_by_class_name("coin-cost-mini-text").text)
    except:
        print("no cost")
    if cardCost < 4:
            print("Found one")
            buyCard = supply[i].find_element_by_class_name("mini-card").click()
            break

#driver.quit()

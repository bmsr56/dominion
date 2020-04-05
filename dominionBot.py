#import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=r'C:/Users/hanna/Documents/ChromeDriver/chromedriver.exe')  # Optional argument, if not specified will search path.


#connect to dominion
driver.get("https://dominion.games")
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'username-input')))

loginForm = driver.find_element_by_name('loginForm')
_inputs = driver.find_elements_by_xpath('//form[@name="loginForm"]//input')
_inputs[0].send_keys("USERNAME")
_inputs[1].send_keys("PASSWORD")
loginForm.submit()
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'tab-button')))

#start bot game
bot_match = driver.find_element(By.XPATH, "//button[contains(.,'1 Bot')]")
bot_match.click()

# =============================================================================
# 
# #untested
# kingdomCards = driver.find_elements_by_xpath("//div[@ng-repeat='kingdom-viewer-group' and contains(., 'card in group')]")
# =============================================================================


#driver.quit()
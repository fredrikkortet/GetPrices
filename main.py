import time
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = FirefoxOptions()
driver = webdriver.Firefox(options=options,service=Service(f"{os.environ['HOME']}/Documents/Programming/WebDriver/geckodriver"))
driver.get("https://www.willys.se/erbjudanden/butik")

print(driver.title)
time.sleep(1)
search = driver.find_element(By.ID,"onetrust-accept-btn-handler")
search.click()
search = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/main/section/div[2]/div[2]/div[1]/div[2]/div/div/input")
search.send_keys("willys halmstad öster")
time.sleep(1)
search = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/main/section/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/ul/ul/div")
search.click()
time.sleep(1)
search = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/main/section/div[2]/div[2]/div[2]/div/div/div[4]/div/button")
search.click()
 
try:
    grid = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"Grid_grid__1YmC6"))
    )
    price = grid.find_elements(By.CLASS_NAME,"PriceLabel_product-price-text__3xFzK")
    for a in price:
        temp = a
        print(temp.text)
except:
    driver.quit()


driver.quit()


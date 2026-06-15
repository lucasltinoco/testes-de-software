from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://duckduckgo.com")

search = driver.find_element(By.CSS_SELECTOR, "input[name='q']")
search.send_keys("calculator")
search.send_keys(Keys.ENTER)

time.sleep(5)

print(driver.page_source)

input("ENTER para fechar")

driver.quit()
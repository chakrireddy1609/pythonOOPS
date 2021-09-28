import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("/Users/chakri/Desktop/chromedriver")
driver.get("https://www.speedtest.net/")
driver.find_element_by_class_name("start-text").click()
driver.implicitly_wait(20)
wait = WebDriverWait(driver,20)
wait.until(expected_conditions.element((By.CSS_SELECTOR,"[class*='download-speed']")))
speed = driver.find_element_by_css_selector("[class*='download-speed']").text
print(speed)
driver.close()

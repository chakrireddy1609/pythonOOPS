import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("/Users/chakri/Desktop/chromedriver")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_xpath("//input[@type='search']").send_keys("m")
time.sleep(4)
list1 = []
list2 = []
names = driver.find_elements_by_xpath("//h4[@class='product-name']")
for name in names:
    list1.append(name.text)
buttons = driver.find_elements_by_xpath("//button[text()='ADD TO CART']")

assert len(buttons) == 11
for button in buttons:
    button.click()
driver.find_element_by_css_selector(".cart-icon").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
cart_names = driver.find_elements_by_xpath("//tr/td[2]/p")
for cart_name in cart_names:
    list2.append(cart_name.text)
assert list1 == list2
amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amount in amounts:
    sum += int(amount.text)

sum_displayed = driver.find_element_by_class_name("totAmt").text
assert sum == int(sum_displayed)

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"promoInfo")))
discounted_sum = driver.find_element_by_class_name("discountAmt").text
assert sum > float(discounted_sum)




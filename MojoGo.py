from selenium import webdriver

driver = webdriver.Chrome("/Users/chakri/Desktop/chromedriver")
driver.get("http://mojogo.staging.joveo.com/")
driver.find_element_by_xpath("//input[@formcontrolname='email']").send_keys("kgrovor+adecco@joveo.com")
driver.find_element_by_xpath("//input[@formcontrolname='password']").send_keys("joveo1520")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//button[contains(@class,'login-btn')]").click()
jobs_name = driver.find_elements_by_xpath("//span[@class='name']")
assert len(jobs_name) != 0
print("Count of Active jobs : ", driver.find_element_by_xpath("//div[contains(@class,'active-tab')]/p[2]").text)
driver.find_element_by_xpath("//p[text()='Not published']").click()
print("Count of Not Published jobs : ", driver.find_element_by_xpath("//div[contains(@class,'active-tab')]/p[2]").text)
driver.find_element_by_xpath("//p[text()='Free']").click()
print("Count of Free jobs : ", driver.find_element_by_xpath("//div[contains(@class,'active-tab')]/p[2]").text)
driver.find_element_by_xpath("//p[text()='Sponsored']").click()
print("Count of Sponsored jobs : ", driver.find_element_by_xpath("//div[contains(@class,'active-tab')]/p[2]").text)
driver.find_element_by_xpath("//p[text()='All']").click()
print("Count of All jobs : ", driver.find_element_by_xpath("//div[contains(@class,'active-tab')]/p[2]").text)
driver.find_element_by_xpath("//mat-icon[@data-mat-icon-name='sponsoring']//*[name()='svg']").click()
publisher_names = driver.find_elements_by_xpath("//tr[@role='row']/td[1]/span")
assert len(publisher_names) != 0




driver.close()
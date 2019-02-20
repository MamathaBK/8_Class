import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://in.linkedin.com/")
driver.maximize_window()
driver.implicitly_wait(30)

elements = driver.find_elements_by_xpath("//input[@type='text' or @type='password' or @type='email']")
print(type(elements))
print(len(elements))
time.sleep(10)

for text in elements:
    text.send_keys("Qspiders")

driver.close()
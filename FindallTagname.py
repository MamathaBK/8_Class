from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(30)

tags = driver.find_elements_by_tag_name("a")
print(len(tags))

driver.close()
from selenium import webdriver

driver = webdriver.Chrome()
#driver = webdriver.Firefox(executable_path ="G:\Automation\Driver\geckodriver-v0.30.0-win64\geckodriver.exe")

#driver = webdriver.Ie(executable_path ="G:\Automation\Driver\edgedriver_win32\msedgedriver.exe")

driver.get("https://www.w3schools.com/python/")

print(driver.title)
driver.close()

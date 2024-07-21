from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Ie(executable_path="G:\Automation\Driver\edgedriver_win32\msedgedriver.exe")

driver.get("https://www.youtube.com/")

print(driver.title)

driver.get("https://www.pavantestingtools.com/")

print(driver.title)

driver.back()

print(driver.title)

driver.forward()

print(driver.title)

driver.close()


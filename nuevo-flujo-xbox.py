import pytest
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait



driver = webdriver.Chrome(r"C:\Users\sergio.reyes\Downloads\chromedriver_win32\chromedriver")
driver.maximize_window()
driver.get("https://www.microsoft.com/en-us/")
print(driver.title)
assert "Microsoft" in driver.title


driver.find_element_by_xpath("//button[@id='search']").click()
driver.find_element_by_xpath("//input[@id='cli_shellHeaderSearchInput']").send_keys("Xbox")
driver.implicitly_wait(3000)
driver.find_element_by_xpath("//button[@id='search']").click()
driver.implicitly_wait(3000)
driver.find_element_by_xpath("//div[@id='R1MarketRedirect-1']/button").click()
driver.execute_script("window.scrollTo(0, 1050)")
driver.implicitly_wait(3000)
driver.find_element_by_xpath("//body/div[2]/section[1]/div[2]/div[3]/div[3]/div[2]/div[1]/ul[1]/li[1]/div[1]/a[1]/div[1]").click()
driver.implicitly_wait(3000)




if driver.current_url == ("https://www.xbox.com/en-US/consoles/xbox-series-x"):
    print("La url: https://www.xbox.com/es-MX/consoles/xbox-series-x es valida")

else:
    print("URL no valida")

if driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/nav[1]/ul[1]/li[1]/a[1]").is_displayed():
    print("Overview button is displayed")

else:
    print("Overview button is not displayed")

if driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/nav[1]/ul[1]/li[2]/a[1]").is_displayed():
    print("Games button is displayed")

else:
    print("Games button is not displayed")

if driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/nav[1]/ul[1]/li[3]/a[1]").is_displayed():
    print("Specs button is displayed")

else:
    print("Specs button is not displayed")

if driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]").is_displayed():
    print("Gallery button is displayed")

else:
    print("Gallery button is not displayed")

if driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/nav[1]/ul[1]/li[5]/a[1]").is_displayed():
    print("Unbox button is displayed")

else:
    print("Unbox button is not displayed")
driver.implicitly_wait(3000)
driver.find_element_by_xpath("//span[contains(text(),'CHECK AVAILABILITY')]").click()
driver.implicitly_wait(3000)
driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[24]/section[1]/div[2]/div[1]/section[1]/div[2]/ul[1]/li[2]/div[1]/img[1]").click()
driver.implicitly_wait(3000)
driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[24]/section[1]/div[2]/div[1]/section[1]/div[2]/ul[1]/li[3]/div[1]/img[1]").click()
driver.implicitly_wait(3000)
driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[24]/section[1]/div[2]/div[1]/section[1]/div[2]/ul[1]/li[4]/div[1]/img[1]").click()
driver.implicitly_wait(3000)
driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[24]/section[1]/div[2]/div[1]/section[1]/div[2]/ul[1]/li[1]/div[1]/img[1]").click()
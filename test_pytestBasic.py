import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains



def test_unosquare_page():
    driver = webdriver.Chrome(r"C:\Users\sergio.reyes\Downloads\chromedriver_win32\chromedriver")
    driver.maximize_window()
    driver.get("https://www.unosquare.com/")
    print(driver.title)
    assert "Unosquare" in driver.title

    driver.find_element_by_xpath("//header/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//header/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//header/div[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//header/div[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//header/div[1]/nav[1]/div[1]/ul[1]/li[6]/a[1]").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//header/div[1]/nav[1]/div[1]/ul[1]/li[7]/a[1]").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//header/div[1]/nav[1]/div[1]/ul[1]/li[8]/a[1]").click()
    driver.implicitly_wait(10)

    driver.find_element_by_xpath("//header/div[1]/nav[1]/a[1]/img[1]").click()
    driver.implicitly_wait(10)
    element_to_hover_over = driver.find_element_by_xpath("//header/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]")
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()
    driver.find_element_by_xpath("//a[normalize-space()='Nearshore Development Services']").click()
    driver.implicitly_wait(10)

    driver.find_element_by_xpath("//a[normalize-space()='Contact Us']").click()
    driver.implicitly_wait(10)
    driver.execute_script("window.scrollTo(0, 850)")
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//input[@id='name-2a32df81-981f-4329-b943-9f2e76efe5f0']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//input[@id='email-2a32df81-981f-4329-b943-9f2e76efe5f0']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//input[@id='company-2a32df81-981f-4329-b943-9f2e76efe5f0']").click()
    driver.implicitly_wait(10)

    if driver.find_element_by_xpath(
            "//div[@class='hs_name hs-name hs-fieldtype-text field hs-form-field']//label[@class='hs-error-msg'][normalize-space()='Please complete this required field.']").is_displayed():
        print("Name Complete field warning was found")

    else:
        print("Name Complete field warning not found")

    if driver.find_element_by_xpath(
            "//div[@class='hs_email hs-email hs-fieldtype-text field hs-form-field']//label[@class='hs-error-msg'][normalize-space()='Please complete this required field.']").is_displayed():
        print("Email Complete field warning was found")

    else:
        print("Email Complete field warning not found")

    driver.find_element_by_xpath("//input[@id='name-2a32df81-981f-4329-b943-9f2e76efe5f0']").send_keys("Sergio")
    driver.find_element_by_xpath("//input[@id='email-2a32df81-981f-4329-b943-9f2e76efe5f0']").send_keys(
        "Sergio@gmail.com")
    driver.find_element_by_xpath("//input[@id='company-2a32df81-981f-4329-b943-9f2e76efe5f0']").send_keys("Unosquare")

    element = driver.find_element_by_xpath("//input[@value='Submit']")
    print(f"Submit button is enabled: {element.is_enabled()}")
    driver.find_element_by_xpath("//header/div[1]/nav[1]/div[1]/ul[1]/li[8]/a[1]").click()

    if driver.find_element_by_xpath("//section[@id='content1']").is_displayed():
        print("Recent Posts contains elements")

    else:
        print("Recent posts contains no elements")
    lista = []
    lista.insert(0, driver.find_element_by_xpath(
        "//header/div[3]/div[1]/div[2]/main[1]/section[1]/div[1]/div[1]/a[1]").text)
    lista.insert(1, driver.find_element_by_xpath(
        "//header/div[3]/div[1]/div[2]/main[1]/section[1]/div[2]/div[1]/a[1]").text)
    lista.insert(2, driver.find_element_by_xpath(
        "//header/div[3]/div[1]/div[2]/main[1]/section[1]/div[3]/div[1]/a[1]").text)
    lista.insert(3, driver.find_element_by_xpath(
        "//header/div[3]/div[1]/div[2]/main[1]/section[1]/div[4]/div[1]/a[1]").text)
    lista.insert(4, driver.find_element_by_xpath(
        "//header/div[3]/div[1]/div[2]/main[1]/section[1]/div[5]/div[1]/a[1]").text)

    for i in range(5):
        print(lista[i])

    driver.find_element_by_xpath("//label[contains(text(),'POPULAR POSTS')]").click()
    if driver.find_element_by_xpath("//section[@id='content2']").is_displayed():
        print("Popular posts contains elements")

    else:
        print("Popular posts contains no elements")

    lista.insert(0, driver.find_element_by_xpath("//header/div[3]/div[1]/div[2]/main[1]/section[2]/div[1]").text)
    lista.insert(1, driver.find_element_by_xpath("//header/div[3]/div[1]/div[2]/main[1]/section[2]/div[2]").text)
    lista.insert(2, driver.find_element_by_xpath("//header/div[3]/div[1]/div[2]/main[1]/section[2]/div[3]").text)
    lista.insert(3, driver.find_element_by_xpath("//header/div[3]/div[1]/div[2]/main[1]/section[2]/div[4]").text)
    lista.insert(4, driver.find_element_by_xpath("//header/div[3]/div[1]/div[2]/main[1]/section[2]/div[5]").text)

    for i in range(5):
        print(lista[i])


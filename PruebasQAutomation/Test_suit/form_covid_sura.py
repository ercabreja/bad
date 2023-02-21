from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, json

driver = webdriver.Firefox(executable_path="C:\Python-Selenium\PruebasQAutomation\firefox_webdriver\geckodriver.exe")

with open("C:\Python-Selenium\PruebasQAutomation\Test_suit\employers\employers.json") as json_file:
    data = json.load(json_file)

    for p in data["employers"]:
        print(p["user"] + " is loading!")
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)

        inputusername = driver.find_element(By.ID, "user-name").send_keys(p["user"])
        inputpassword = driver.find_element(By.ID, "password").send_keys(p["pass"])
        time.sleep(3)


        btnLoging = driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

        print(p["user"] + " is DONE!")
        

        driver.close()
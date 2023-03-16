
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from loginPage import TestLoginPage
from loginPage import TestHomePage
import time
import unittest


# Iniciar el navegador y navegar a la página de inicio de sesión
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://practicetestautomation.com/practice-test-login/')
login_page = TestLoginPage(driver)

# Ingresar credenciales y hacer clic en el botón de login y cierra sesion
login_page.enter_username('student')
login_page.enter_password('Password123')
login_page.click_submit()
login_page.click_submitBTNlogout()
#time.sleep(5)

# nevega a la siguiente pagina y llena los campos
driver.get('https://testingqarvn.com.es/datos-personales/')
home_page = TestHomePage(driver)
home_page.enter_username2("elvis")

# Llena los campos
home_page.enter_lastname("cabreja")
home_page.enter_email("elvisrafael@gmail.com")
home_page.enter_phone("8097195183")
home_page.enter_address("santo domingo 30002")
home_page.click_submit2()
#time.sleep(2)

def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
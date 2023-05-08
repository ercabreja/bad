# importamos las librerías necesarias
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from objets import LoginPage
from objets import FormPage
import selectors
import unittest
import time

class TestForm(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
        
    def test_login_and_fill_form(self):
        # creamos instancias de las clases LoginPage y FormPage
        login_page = LoginPage(self.driver)
        form_page = FormPage(self.driver)
        
        # abrimos la página de inicio de sesión
        self.driver.get('https://practicetestautomation.com/practice-test-login/')
        
        # iniciamos sesión
        login_page.login('student', 'Password123')
        
        
        # abrimos la página del formulario
        self.driver.get('https://testingqarvn.com.es/datos-personales/')
        
        # completamos el formulario
        form_page.fill_form('elvis', 'cabreja', 'elvisrafael@gmail.com', '8097195183', 'santo Domingo')
        time.sleep(2)
        
        
        
        # verificamos que se haya enviado el formulario
        
        message = self.driver.find_element(By.XPATH, "//p[text()='Gracias por tu encuesta.']").is_enabled()
        
        if message == True:
            print("Formulario enviado exitosamente")
            
        else:
            print ("No se logro validar el envio del formulario")
   

        
    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()

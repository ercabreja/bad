# importamos las librerías necesarias
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# creamos la clase LoginPage para la página de inicio de sesión
class LoginPage:
    
    # definimos los elementos de la página de inicio de sesión
    username_field = (By.CSS_SELECTOR, '#username')
    password_field = (By.ID, 'password')
    login_button = (By.ID, 'submit')
    logout_button = (By.XPATH, "//a[text()='Log out']")
    
    def __init__(self, driver):
        self.driver = driver
    
    # definimos el método para iniciar sesión
    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        self.driver.find_element(*self.logout_button).click()
        # esperamos a que la página de inicio de sesión desaparezca antes de continuar
        #WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.login_button))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.logout_button))
        
# creamos la clase FormPage para la página del formulario
class FormPage:
    
    # definimos los elementos del formulario
    name_field = (By.ID, 'wsf-1-field-21')
    lastname_field = (By.ID, 'wsf-1-field-22')
    email_field = (By.ID, 'wsf-1-field-23')
    phone_field = (By.ID, 'wsf-1-field-24')
    address_field = (By.ID, 'wsf-1-field-28')
    submit_button = (By.ID, 'wsf-1-field-27')
    
    
    def __init__(self, driver):
        self.driver = driver
    
    # definimos el método para completar el formulario
    def fill_form(self, name, lastname, email, phone, address):
        self.driver.find_element(*self.name_field).send_keys(name)
        self.driver.find_element(*self.lastname_field).send_keys(lastname)
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.phone_field).send_keys(phone)
        self.driver.find_element(*self.address_field).send_keys(address)
        self.driver.find_element(*self.submit_button).click()

        
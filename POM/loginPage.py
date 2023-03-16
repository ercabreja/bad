from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestLoginPage(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'username')
        self.password_input = (By.ID, 'password')
        self.submit_button = (By.ID, 'submit')
        self.submit_logoutBTN = (By.XPATH, "//a[text()='Log out']")
        
        
    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_input)).send_keys(username)
        
    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password_input)).send_keys(password)
        
    def click_submit(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.submit_button)).click()
        
    def click_submitBTNlogout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.submit_logoutBTN)).click()

class TestHomePage(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.ID, 'wsf-1-field-21')
        self.lastname_input = (By.XPATH, "//input[@id='wsf-1-field-22']")
        self.email_input = (By.XPATH, "//input[@id='wsf-1-field-23']")
        self.phone_input = (By.XPATH, "//input[@id='wsf-1-field-24']")
        self.address_input = (By.XPATH, "//textarea[@id='wsf-1-field-28']")
        self.btn_submit = (By.XPATH, "//button[@id='wsf-1-field-27']")
        
    def enter_username2(self, name):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.name_input)).send_keys(name)
    def enter_lastname(self, lastname):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.lastname_input)).send_keys(lastname)
    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.email_input)).send_keys(email)
    def enter_phone(self, phone):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.phone_input)).send_keys(phone)
    def enter_address(self, address):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.address_input)).send_keys(address)
    def click_submit2(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_submit)).click()
        
        
    
    
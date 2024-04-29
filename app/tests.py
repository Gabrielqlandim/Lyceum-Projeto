from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()

class Historia1(LiveServerTestCase):
    def cadastro(self):
        nome = 'admin1'
        email = 'admin1@cesar.school'
        senha = '123'
        
        sleep(2)
        driver.find_element(By.ID, 'cadastrar-btn').click()
        driver.find_element(By.ID, 'nome').send_keys(nome)
        driver.find_element(By.ID, 'email').send_keys(email)
        driver.find_element(By.ID, 'senha').send_keys(senha)
        driver.find_element(By.ID, 'botao').click()
        sleep(2)
        driver.find_element(By.ID, 'login-btn').click()

    def login(self):
        nome = 'admin1'
        email = 'admin1@cesar.school'
        senha = '123'

        driver.find_element(By.ID, 'nome').send_keys(nome)
        driver.find_element(By.ID, 'senha').send_keys(senha)
        sleep(2)
        driver.find_element(By.ID, 'botao').click()

    def test_login(self):
        driver.get('http://localhost:8000/')
        self.cadastro()
        self.login()
        

import pytest
import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestConsultarBelt():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5) #espera de 5 segundos para os elementos da pagina carregarem
        self.driver.maximize_window()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_consultar_Belt_Enter(self):
        self.driver.get('http://demostore.supersqa.com/')
        #self.driver.set_window_size(1280, 680)
        self.driver.find_element(By.ID, 'woocommerce-product-search-field-0')
        self.driver.find_element(By.ID, 'woocommerce-product-search-field-0').send_keys("Belt")
        self.driver.find_element(By.ID, 'woocommerce-product-search-field-0').send_keys(Keys.ENTER)
        time.sleep(3)
        assert self.driver.find_element(By.XPATH, '//*[@id="product-17"]/div[2]/h1').text == "Belt"
        assert self.driver.find_element(By.XPATH, '//*[@id="product-17"]/div[2]/p/span/bdi').text == "$37.14"

    def test_consultar_Belt_Pagina_2(self):
        self.driver.get('http://demostore.supersqa.com/')
        self.driver.find_element(By.CSS_SELECTOR, '#main > div:nth-child(2) > nav > ul > li:nth-child(2) > a').click()
        assert self.driver.current_url == 'http://demostore.supersqa.com/page/2/'



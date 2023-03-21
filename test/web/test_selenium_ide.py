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

    @pytest.mark.parametrize('termo, produto, preco, xpathText, xpathPrice',[
        ('belt', 'Belt', '$37.14', '//*[@id="product-17"]/div[2]/h1', '//*[@id="product-17"]/div[2]/p/span/bdi'),
        ('album', 'Album', '$15.00', '//*[@id="product-24"]/div[2]/h1', '//*[@id="product-24"]/div[2]/p/span/bdi'),
        ('beanie', 'Beanie', '$18.00', '//*[@id="main"]/ul/li[2]/a[1]/h2','//*[@id="main"]/ul/li[2]/a[1]/span[2]/ins/span/bdi')
    ])
    def test_consultar_produto_Enter(self, termo, produto, preco, xpathText, xpathPrice):
        self.driver.get('http://demostore.supersqa.com/')
        self.driver.get_screenshot_as_file('D:/python/Automated-Tests-Python/test/prints/homepage.png')
        self.driver.find_element(By.ID, 'woocommerce-product-search-field-0')
        self.driver.find_element(By.ID, 'woocommerce-product-search-field-0').send_keys(termo)
        self.driver.find_element(By.ID, 'woocommerce-product-search-field-0').send_keys(Keys.ENTER)
        assert self.driver.find_element(By.XPATH, xpathText).text == produto
        assert self.driver.find_element(By.XPATH, xpathPrice).text == preco

    def test_consultar_Belt_Pagina_2(self):
        self.driver.get('http://demostore.supersqa.com/')
        self.driver.find_element(By.CSS_SELECTOR, '#main > div:nth-child(2) > nav > ul > li:nth-child(2) > a').click()
        assert self.driver.current_url == 'http://demostore.supersqa.com/page/2/'

    def test_consultar_freeshipping_msg(self):
        self.driver.get('http://demostore.supersqa.com/')
        assert self.driver.find_element(By.CSS_SELECTOR, '#wpfront-notification-bar-table > tbody > tr > td > div').text == 'Free shipping on orders over $50'



from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import test_data
from Test_Locators import locators
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import time


class Test_Pim2:
    url = "https://opensource-demo.orangehrmlive.com"

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()

    def test_get_title(self, booting_function):
        self.driver.get(self.url)
        assert self.driver.title == 'AT1'
        print("SUCCESS # Web Title Captured Successfully")

    def test_login(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=test_data.Selectors.input_box_username).send_keys(
            test_data.Data.username)
        self.driver.find_element(by=By.NAME, value=test_data.Selectors.input_box_password).send_keys(
            test_data.Data.password)
        self.driver.find_element(by=By.XPATH, value=test_data.Selectors.login_xpath).click()
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS # LOGGED IN WITH USERNAME {username} and PASSWORD {password}".format(
            username=test_data.Data.username, password=test_data.Data.password))

    def test_PIM2 (self):
            try:
                self.driver.get(test_data.Data().url)
                self.driver.maximize_window()
                self.driver.implicitly_wait(10)
                action = ActionChains(self.driver)
                wait = WebDriverWait(self.driver, 20)

                #click on pim
                self.driver.find_element(by=By.XPATH, value=locators.Locators.xpath).click()

                #click on delete
                self.driver.find_element(by=By.XPATH, value=locators.Locators.xpath1).click()


            except NoSuchElementException as e:
                print("Error!")














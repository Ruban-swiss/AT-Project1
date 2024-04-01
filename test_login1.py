from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import test_data
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import pytest
import time


class Test_Login1:
    url = "https://opensource-demo.orangehrmlive.com"

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()

    def test_get_title(self, booting_function):
        self.driver.get(self.url)
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS # Web Title Captured Successfully")

    def test_validlogin(self, booting_function):
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




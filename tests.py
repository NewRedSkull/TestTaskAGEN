from selenium import webdriver

import unittest
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import page
import locators


file = open('credentials.properties')
credentials = file.readlines()
valid_email = credentials[0]
valid_pass = credentials[1]
not_valid_pass = credentials[2]
not_valid_email = credentials[3]

class TestLogin(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome('/Users/andrii/Downloads/chromedriver_mac64/chromedriver') #Firefox, Explorer, Safari
        self.driver.get('https://courses.ultimateqa.com/users/sign_in')
        self.driver.maximize_window()
        self.driver.add_cookie({'name': 'visitor_id', 'value': '317826872', 'domain': '.ultimateqa.com'}) #will work to get past capcha at a local machine, if add all google cookies. But only the time wile cookie is available;
        self.driver.add_cookie({'name': '1P_JAR', 'value': '2019-8-16-8', 'domain': '.google.com'})
        self.driver.add_cookie({'name': 'ANID', 'value': 'AHWqTUmM7mUzSXbuvCupxc5ZjD3x1wT5WwBPUKSGXLt_zVUk6fzwKO-CDbfVBali', 'domain': '.google.com'})
        self.driver.add_cookie({'name': 'APISID', 'value': 'xmAODungRPICK7_n/A6m1DPNEZ5hdCymQd', 'domain': '.google.com'})
        self.driver.add_cookie({'name': 'DV', 'value': 'AwOaDyq7tUFOUP5Ji-7m9IjnjB6ZyVYGgEm9tUxalQIAAAAGqafRlXCn-AAAAGC9VCFbQNaLYwAAAA', 'domain': 'www.google.com'})
        self.driver.add_cookie({'name': 'HSID', 'value': 'A23iCMr2nwzJjXMkk', 'domain': '.google.com'})
        self.driver.add_cookie({'name': 'NID', 'value': '188=ta2D2TllJte7O10XLryhRnhxdhQCAkKkiMHE_kX3uGDixqrnr_oskGa0kUDV7EG8mJJOtzkPwqLOFX-DHPSPhSsFadbsOhB3JR_lLj_cpc-cOk5_DSu4JHxs5xw9I7mlTcAHIs3kexIWufHUtdpab5u3OyhaVEMNYQoilIaFs0DKXwLbvz00WG6k_KJ2QKiLaxAuYNn3Si2tjxXt_FtrUicG6wol4uM-fI9XrSNhB_eF5agaQPivxynsjxWESpplUcTlyoXh', 'domain': '.google.com'})
        self.driver.add_cookie({'name': 'SAPISID', 'value': 'AGeWx7CgjeIg8rc5/A2vZeqvTQETPplVqU', 'domain': '.google.com'})
        self.driver.add_cookie({'name': 'SEARCH_SAMESITE', 'value': 'CgQIy40B', 'domain': '.google.com'})
        self.driver.add_cookie({'name': 'SID', 'value': 'nQdUoIkrkPhWkd-dWq--qfkaSFz8oNRJQjiklVIwJp4kVl0oOP6r8o9Udaslu-SU7TRKeQ.', 'domain': '.google.com'})
        self.driver.add_cookie({'name': 'SIDCC', 'value': 'AN0-TYubMppZ97O0vkN3ZsCyGqu06LPFf3mbXn0ZeUUm_0X6AFTwghIb9gt1NXlcter3OyRHJA', 'domain': '.google.com'})
        self.driver.add_cookie({'name': 'SSID', 'value': 'A4G1XdlG6rmYR8Ux3', 'domain': '.google.com'})

    def test_login_positive(self):
        page.LoginField.email_field_enter_value(self, valid_email)
        page.PassWordField.password_field_enter_value(self, valid_pass)
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locators.LoginPageLocators.sigh_in_button))
        finally:
            self.driver.quit()
        page.SighnInButton.click_button(self)
        try:
            page.AfterLOginPadeDashboard.capcha(self)
        except NoSuchElementException:
            return "No element capcha"


    def test_pass_negative(self):
        page.LoginField.email_field_enter_value(self, valid_email)
        page.PassWordField.password_field_enter_value(self, not_valid_pass)
        time.sleep(4)
        page.SighnInButton.click_button(self)
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locators.LoginPageLocators.sigh_in_button))
        finally:
            self.driver.quit()
        page.SighnInButton.click_button(self)
        try:
            page.LoginFailed.login_failed(self)
        except NoSuchElementException:
            return "No element no login"


    def test_login_login_negative(self):
        page.LoginField.email_field_enter_value(self, not_valid_email)
        page.PassWordField.password_field_enter_value(self, valid_pass)
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locators.LoginPageLocators.sigh_in_button))
        finally:
            self.driver.quit()
        page.SighnInButton.click_button(self)

        assert page.LoginFailed.login_failed(self)


    def test_existance_of_the_password_field(self):
        assert page.PassWordField.password_field(self)

    def test_existance_of_the_email_field(self):
        assert page.LoginField.login_field(self)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

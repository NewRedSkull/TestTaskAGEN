from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time
import page

valid_email = 'testtesttest@test.com'
valid_password = 'test1234'


class TestLogin(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome('/Users/andrii/Downloads/chromedriver_mac64/chromedriver') #Firefox, Explorer, Safari
        self.driver.maximize_window()
        #cookie = {'name':'userverify?k=6Lem7ZYUAAAAAMc3Y--CC6s7WYl5pOZ_AzkG7zlC','SIDCC':'AN0-TYvhTeK1KPFCO8jguAmnpeoWiA9Eyg-Pu7ME98lklPaPEYjvLxrCmOEZAevHLiso2tYAvz8-', 'path':'/', 'domain':'.google.com', 'priority':'high'}
        #self.driver.get_cookie(cookie)
        self.driver.get('https://courses.ultimateqa.com/users/sign_in')


    def test_login_positive(self):

        page.LoginField.email_field_enter_value(self, valid_email)
        page.PassWordField.password_field_enter_value(self, "delta")
        page.SighnInButton.click_button(self)
        button = self.driver.find_element_by_css_selector('div.form__button-group')
        time.sleep(7)


    def test_existance_of_the_password_field(self):
        page.PassWordField.password_field_enter_value(self, "delta")
        assert True

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()


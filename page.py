from locators import LoginPageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class LoginField(BasePage):

    def email_field_enter_value(self, email):
        #enters valuer into the field (email_field)
        element = self.driver.find_element(*LoginPageLocators.email_field)
        element.send_keys(email)


class PassWordField(BasePage):

    def password_field_enter_value(self, password):
        # enters valuer into the field (passwod_field)
        element = self.driver.find_element(*LoginPageLocators.password_field)
        element.send_keys(password)


class SighnInButton(BasePage):

    def click_button(self):
        button = self.driver.find_element(*LoginPageLocators.sigh_in_button)
        button.click()


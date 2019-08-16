from locators import LoginPageLocators
from locators import AfterLoginPageLocators

class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver


class LoginField(LoginPage):

    def email_field_enter_value(self, email):
        #enters valuer into the field (email_field)
        element = self.driver.find_element(*LoginPageLocators.email_field)
        element.send_keys(email)

    def login_field(self):
        return self.driver.find_element(*LoginPageLocators.email_field)


class PassWordField(LoginPage):

    def password_field_enter_value(self, password):
        # enters valuer into the field (passwod_field)
        element = self.driver.find_element(*LoginPageLocators.password_field)
        element.send_keys(password)

    def password_field(self):
        return self.driver.find_element(*LoginPageLocators.password_field)


class SighnInButton(LoginPage):

    def click_button(self):
        button = self.driver.find_element(*LoginPageLocators.sigh_in_button)
        button.click()

    def get_button(self):
        return self.driver.find_element(*LoginPageLocators.sigh_in_button)


class AfterLOginPadeDashboard(LoginPage):

    def dashboard(self):
        dashboard = self.driver.find_element(*AfterLoginPageLocators.my_dashboard)
        return dashboard

    def capcha(self):
        capcha = self.driver.find_element(*AfterLoginPageLocators.capcha)
        return capcha

class LoginFailed(LoginPage):

    def login_failed(self):
        login_failed = self.driver.find_element(*LoginPageLocators.not_valid_pass_exeption)
        return login_failed



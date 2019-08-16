from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    email_field = (By.ID, 'user[email]')
    password_field = (By.ID, 'user[password]')
    sigh_in_button = (By.CSS_SELECTOR, 'div.form__button-group > input')
    remember_me_check_box = (By.XPATH, '//*[@id="user[remember_me]"]')
    not_valid_pass_exeption = (By.CSS_SELECTOR, '#notice > ul > li')

class AfterLoginPageLocators(object):
    my_dashboard = (By.XPATH, '/html/body/header/div/div/nav/ul/li[1]/a')
    capcha = (By.CLASS_NAME, 'rc-imageselect-response-field')
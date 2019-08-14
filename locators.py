from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    email_field = (By.ID, 'user[email]')
    password_field = (By.ID, 'user[password]')
    sigh_in_button = (By.CSS_SELECTOR, '#sign_in_93d3670639 > div.form__button-group > input') ##sign_in_93d3670639 > div.form__button-group > input
    remember_me_check_box = (By.XPATH, '//*[@id="user[remember_me]"]')
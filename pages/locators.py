from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login"
    LOGIN_FORM = (By.CSS_SELECTOR, "[id='login_form']")
    REGISTER_FORM = (By.CSS_SELECTOR, "[id='register_form']")

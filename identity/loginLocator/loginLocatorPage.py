from selenium.webdriver.common.by import By


class LoginActionLocator:
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "submit")
    LOGOUT = (By.ID, "logout")


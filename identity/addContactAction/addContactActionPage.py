from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec
from identity import addContactLocator
from identity.addContactLocator import addContactLocatorPage
from identity.addContactLocator.addContactLocatorPage import AddContactLocatorPage


class AddContactActionPage:
    def __init__(self, driver):
        self.driver = driver

    def add_contact_btn(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(AddContactLocatorPage.addContactBtn)
        )
        element.click()

    def enter_first_name(self):

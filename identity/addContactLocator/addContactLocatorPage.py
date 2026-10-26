from selenium.webdriver.common.by import By


class AddContactLocatorPage:
    addContactBtn = (By.ID, "add-contact")
    firstname = (By.ID, "firstName")
    lastname = (By.ID, "lastName")
    dateOfBirth = (By.ID, "birthdate")
    email = (By.ID, "email")
    address1 = (By.ID, "street1")
    address2 = (By.ID, "street2")
    city = (By.ID, "city")
    province = (By.ID, "stateProvince")
    postalCode = (By.ID, "postalCode")
    country = (By.ID, "country")
    submitBtn = (By.ID, "submit ")

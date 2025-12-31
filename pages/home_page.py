from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    CONTACT_TITLE = (By.XPATH, "//h2[normalize-space()='Send Us a Message']")

    NAME = (By.ID, "g2-name")
    EMAIL = (By.ID, "g2-email")
    MESSAGE = (By.ID, "contact-form-comment-g2-message")
    SUBMIT = (By.XPATH, "//button[@type='submit' or contains(., 'Submit')]")
    GO_BACK = (By.XPATH, "//a[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'go back')]")


    WARNINGS = (By.XPATH, "//*[contains(.,'Warning')]")
    SENT_MSG = (By.XPATH, "//*[contains(.,'Your message has been sent')]")

    def clear_contact_form_fields(self):
        self.driver.find_element(*self.NAME).clear()
        self.driver.find_element(*self.EMAIL).clear()
        self.driver.find_element(*self.MESSAGE).clear()

    def fill_contact_form(self, name: str, email: str, message: str):
        self.driver.find_element(*self.NAME).send_keys(name)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.MESSAGE).send_keys(message)

    def submit_contact_form(self):
        self.driver.find_element(*self.SUBMIT).click()

    def wait_go_back_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.GO_BACK))

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    CONTACT_TITLE = (By.XPATH, "//h2[normalize-space()='Send Us a Message']")

    NAME = (By.ID, "g2-name")
    EMAIL = (By.ID, "g2-email")
    MESSAGE = (By.ID, "contact-form-comment-g2-message")
    SUBMIT = (By.XPATH, "//button[@type='submit' or contains(@class,'pushbutton')]")

    WARNINGS = (By.XPATH, "//*[contains(.,'Warning')]")
    SENT_MSG = (By.XPATH, "//*[contains(.,'Your message has been sent')]")


    def contact_block_is_visible(self):
        self.wait_visible(self.CONTACT_TITLE)

    def submit_empty_form(self):
        # make sure the form section is loaded/visible
        self.contact_block_is_visible()
        self.click(self.SUBMIT)

    def submit_contact_form(self, name: str, email: str, message: str):
        self.contact_block_is_visible()
        self.wait_visible(self.NAME).send_keys(name)
        self.wait_visible(self.EMAIL).send_keys(email)
        self.wait_visible(self.MESSAGE).send_keys(message)
        self.click(self.SUBMIT)

import unittest
from pages.home_page import HomePage
from src.config import BASE_URL, DEFAULT_TIMEOUT
from src.driver_factory import create_driver


class TestContactForm(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver()
        self.page = HomePage(self.driver, timeout=DEFAULT_TIMEOUT)
        self.page.open(BASE_URL)

    def test_empty_contact_form_shows_warning(self):
        self.page.submit_empty_form()
        warnings = self.driver.find_elements(*self.page.WARNINGS)
        self.assertTrue(len(warnings) > 0, "Expected validation warnings")

    def test_valid_contact_form_submit(self):
        self.page.submit_contact_form(
            name="Olga Test",
            email="olga.test@example.com",
            message="Hello! This is an automated unittest message."
        )
        self.page.wait_visible(self.page.SENT_MSG)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

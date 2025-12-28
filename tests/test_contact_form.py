import unittest

from pages.home_page import HomePage
from src.driver_factory import create_driver
from src.config import BASE_URL


class TestContactForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = create_driver()
        cls.driver.get(BASE_URL)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get(BASE_URL)
        self.page = HomePage(self.driver)


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


if __name__ == "__main__":
    unittest.main()

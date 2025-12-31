import unittest

from src.config import BASE_URL
from src.driver_factory import create_driver
from pages.home_page import HomePage


class TestCrossBrowserContactForm(unittest.TestCase):
    def test_contact_form_chrome_maximized(self):
        driver = create_driver()  # пока используем то, что уже работает (chrome)
        try:
            driver.maximize_window()

            page = HomePage(driver)
            driver.get(BASE_URL)

            # (4) assert title after open + print
            self.assertTrue(len(driver.title) > 0, "Title should not be empty")
            print("[Chrome | maximized] Home page title:", driver.title)

            # (6) clear fields
            page.wait_visible(page.NAME)
            page.clear_contact_form_fields()

            # (7) fill + submit
            page.fill_contact_form(
                name="Olga Test",
                email="olga.test@example.com",
                message="Chrome maximized test"
            )
            page.submit_contact_form()

            # (8) wait Go Back visible
            page.wait_go_back_visible()

            # (9) assert title + print
            self.assertTrue(len(driver.title) > 0, "Title after submit should not be empty")
            print("[Chrome | maximized] After submit title:", driver.title)

        finally:
            driver.quit()


if __name__ == "__main__":
    unittest.main()

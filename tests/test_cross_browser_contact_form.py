import unittest

from src.config import BASE_URL
from src.driver_factory import create_driver
from pages.home_page import HomePage


class TestCrossBrowserContactForm(unittest.TestCase):
    def test_contact_form_firefox_maximized(self):
        driver = create_driver("firefox")
        try:
            driver.maximize_window()

            page = HomePage(driver)
            driver.get(BASE_URL)

            self.assertTrue(len(driver.title) > 0, "Title should not be empty")
            print("[Firefox | maximized] Home page title:", driver.title)

            page.wait_visible(page.NAME)
            page.clear_contact_form_fields()

            page.fill_contact_form(
                name="Olga Test",
                email="olga.test@example.com",
                message="Firefox maximized test"
            )
            page.submit_contact_form()

            page.wait_go_back_visible()

            self.assertTrue(len(driver.title) > 0, "Title after submit should not be empty")
            print("[Firefox | maximized] After submit title:", driver.title)

        finally:
            driver.quit()

    def test_contact_form_chrome_1820x1050(self):
        driver = create_driver()
        try:
            driver.set_window_size(1820, 1050)

            page = HomePage(driver)
            driver.get(BASE_URL)

            self.assertTrue(len(driver.title) > 0, "Title should not be empty")
            print("[Chrome | 1820x1050] Home page title:", driver.title)

            page.wait_visible(page.NAME)
            page.clear_contact_form_fields()

            page.fill_contact_form(
                name="Olga Test",
                email="olga.test@example.com",
                message="Chrome 1820x1050 test"
            )
            page.submit_contact_form()

            page.wait_go_back_visible()

            self.assertTrue(len(driver.title) > 0)
            print("[Chrome | 1820x1050] After submit title:", driver.title)

        finally:
            driver.quit()

    def test_contact_form_firefox_1820x1050(self):
        driver = create_driver("firefox")
        try:
            driver.set_window_size(1820, 1050)

            page = HomePage(driver)
            driver.get(BASE_URL)

            self.assertTrue(len(driver.title) > 0, "Title should not be empty")
            print("[Firefox | 1820x1050] Home page title:", driver.title)

            page.wait_visible(page.NAME)
            page.clear_contact_form_fields()

            page.fill_contact_form(
                name="Olga Test",
                email="olga.test@example.com",
                message="Firefox 1820x1050 test"
            )
            page.submit_contact_form()

            page.wait_go_back_visible()

            self.assertTrue(len(driver.title) > 0, "Title after submit should not be empty")
            print("[Firefox | 1820x1050] After submit title:", driver.title)

        finally:
            driver.quit()

    def test_contact_form_edge_maximized(self):
        driver = create_driver("edge")
        try:
            driver.maximize_window()

            page = HomePage(driver)
            driver.get(BASE_URL)

            self.assertTrue(len(driver.title) > 0, "Title should not be empty")
            print("[Edge | maximized] Home page title:", driver.title)

            page.wait_visible(page.NAME)
            page.clear_contact_form_fields()

            page.fill_contact_form(
                name="Olga Test",
                email="olga.test@example.com",
                message="Edge maximized test"
            )
            page.submit_contact_form()

            page.wait_go_back_visible()

            self.assertTrue(len(driver.title) > 0, "Title after submit should not be empty")
            print("[Edge | maximized] After submit title:", driver.title)

        finally:
            driver.quit()

    def test_contact_form_edge_1820x1050(self):
        driver = create_driver("edge")
        try:
            driver.set_window_size(1820, 1050)

            page = HomePage(driver)
            driver.get(BASE_URL)

            self.assertTrue(len(driver.title) > 0, "Title should not be empty")
            print("[Edge | 1820x1050] Home page title:", driver.title)

            page.wait_visible(page.NAME)
            page.clear_contact_form_fields()

            page.fill_contact_form(
                name="Olga Test",
                email="olga.test@example.com",
                message="Edge 1820x1050 test"
            )
            page.submit_contact_form()

            page.wait_go_back_visible()

            self.assertTrue(len(driver.title) > 0, "Title after submit should not be empty")
            print("[Edge | 1820x1050] After submit title:", driver.title)

        finally:
            driver.quit()








if __name__ == "__main__":
    unittest.main()

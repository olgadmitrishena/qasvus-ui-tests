import unittest

from src.config import BASE_URL
from src.driver_factory import create_driver
from pages.home_page import HomePage


class TestCrossBrowserContactForm(unittest.TestCase):

    def _run_contact_form_flow(self, browser: str, window: str):
        driver = create_driver(browser)
        try:
            if window == "1820x1050":
                driver.set_window_size(1820, 1050)
            else:
                driver.maximize_window()

            page = HomePage(driver)
            driver.get(BASE_URL)

            self.assertTrue(len(driver.title) > 0, "Title should not be empty")
            print(f"[{browser.capitalize()} | {window}] Home page title:", driver.title)

            page.wait_visible(page.NAME)
            page.clear_contact_form_fields()

            page.fill_contact_form(
                name="Olga Test",
                email="olga.test@example.com",
                message=f"{browser} {window} test"
            )
            page.submit_contact_form()

            page.wait_go_back_visible()

            self.assertTrue(len(driver.title) > 0, "Title after submit should not be empty")
            print(f"[{browser.capitalize()} | {window}] After submit title:", driver.title)

        finally:
            driver.quit()

    def test_contact_form_cross_browser(self):
        browsers = ["chrome", "firefox", "edge"]
        windows = ["maximized", "1820x1050"]

        for browser in browsers:
            for window in windows:
                with self.subTest(browser=browser, window=window):
                    self._run_contact_form_flow(browser, window)


if __name__ == "__main__":
    unittest.main()

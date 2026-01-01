from tests.base_test import BaseTest
import os


class TestContactForm(BaseTest):

    def _run_contact_form_flow(self, browser: str, window: str):
        driver = create_driver(browser)
        try:
            # окно
            if window == "1820x1050":
                driver.set_window_size(1820, 1050)
            else:
                driver.maximize_window()

            page = HomePage(driver)
            driver.get(BASE_URL)

            # title after open + print
            self.assertTrue(len(driver.title) > 0, "Title should not be empty")
            print(f"[{browser.capitalize()} | {window}] Home page title:", driver.title)

            # clear fields
            page.wait_visible(page.NAME)
            page.clear_contact_form_fields()

            # fill + submit
            page.fill_contact_form(
                name="Olga Test",
                email="olga.test@example.com",
                message=f"{browser} {window} test"
            )
            page.submit_contact_form()

            # wait Go Back
            page.wait_go_back_visible()

            # title after submit + print
            self.assertTrue(len(driver.title) > 0, "Title after submit should not be empty")
            print(f"[{browser.capitalize()} | {window}] After submit title:", driver.title)

        finally:
            driver.quit()


    def test_empty_contact_form_shows_warning(self):
        test_cases = [
            {"name": "", "email": "", "message": ""},
            {"name": "Olga", "email": "", "message": ""},
            {"name": "", "email": "test@test.com", "message": ""},
        ]

        for case in test_cases:
            with self.subTest(case=case):
                self.page.clear_contact_form_fields()
                self.page.fill_contact_form(case["name"], case["email"], case["message"])
                self.page.submit_contact_form()

                warnings = self.driver.find_elements(*self.page.WARNINGS)
                self.assertTrue(len(warnings) > 0, msg=f"Expected warnings for case: {case}")

    def test_valid_contact_form_submit(self):
        self.page.clear_contact_form_fields()
        self.page.fill_contact_form("Olga Test", "olga.test@example.com",
                                    "Hello! This is an automated unittest message.")
        self.page.submit_contact_form()

        self.page.wait_visible(self.page.SENT_MSG)

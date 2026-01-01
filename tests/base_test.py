import os
import unittest
from datetime import datetime
from src.config import BASE_URL
from pages.home_page import HomePage
from src.driver_factory import create_driver


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = create_driver()
        self.page = HomePage(self.driver)
        self.page.open(BASE_URL)

    def tearDown(self):
        # 1) Определяем: тест упал или нет
        test_failed = False

        # errors + failures хранятся в результате прогона
        outcome = getattr(self, "_outcome", None)
        if outcome and getattr(outcome, "result", None):
            result = outcome.result
            test_failed = bool(result.failures or result.errors)

        # 2) Если упал — сохраняем скриншот
        if test_failed and getattr(self, "driver", None):
            os.makedirs("artifacts", exist_ok=True)
            ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            name = f"artifacts/{self.id()}__{ts}.png"
            self.driver.save_screenshot(name)
            print(f"\n[artifact] saved screenshot: {name}")

        # 3) Закрываем браузер
        if getattr(self, "driver", None):
            self.driver.quit()

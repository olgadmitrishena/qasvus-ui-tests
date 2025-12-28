import unittest

from src.driver_factory import create_driver
from src.config import BASE_URL
from pages.home_page import HomePage


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver()
        self.driver.get(BASE_URL)
        self.page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

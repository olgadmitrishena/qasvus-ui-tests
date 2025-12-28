from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def create_driver(browser: str = "chrome", headless: bool = False):
    """
    Create and return a Selenium WebDriver instance.
    For now: Chrome only (we'll add Firefox/Edge later).
    """
    if browser != "chrome":
        raise ValueError(f"Unsupported browser: {browser}")

    options = ChromeOptions()
    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

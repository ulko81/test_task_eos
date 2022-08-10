from locators.reg_auth_locator import RegAuthLocator
from pages.all_page import AllPage


class RegAuthPage(AllPage, RegAuthLocator):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

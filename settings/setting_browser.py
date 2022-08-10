import os
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

DEFAULT_URL = 'https://eos.com/crop-monitoring/'


class SettingsBrowser:
    @staticmethod
    def set_chrome(width=1920, height=1080):
        options = webdriver.ChromeOptions()
        capabilities = DesiredCapabilities.CHROME
        options.add_argument('--window-size={width_},{height_}'.format(width_=width, height_=height))
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('user-agent=Auto_tester')
        return webdriver.Chrome(options=options, desired_capabilities=capabilities,
                                executable_path=os.path.abspath('../drivers/chromedriver.exe'))

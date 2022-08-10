from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

from exception import *


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.delay = 1

    def delay_by_step(self):
        time.sleep(self.delay)

    def check_els(self, item):
        self.delay_by_step()
        try:
            return self.wait.until(expected_conditions.presence_of_all_elements_located(item))
        except TimeoutException:
            return False

    def check_find_els(self, el, item):
        self.delay_by_step()
        try:
            return WebDriverWait(el, self.timeout).until(expected_conditions.presence_of_all_elements_located(item))
        except TimeoutException:
            return False

    def check_visible_els(self, item):
        self.delay_by_step()
        try:
            return self.wait.until(expected_conditions.visibility_of_any_elements_located(item))
        except TimeoutException:
            return False

    def check_invisible_el(self, item):
        self.delay_by_step()
        try:
            return self.wait.until(expected_conditions.invisibility_of_element_located(item))
        except TimeoutException:
            return False

    def check_visible_find_els(self, el, item):
        self.delay_by_step()
        try:
            return WebDriverWait(el, self.timeout).until(expected_conditions.visibility_of_any_elements_located(item))
        except TimeoutException:
            return False

    def check_invisible_find_el(self, el, item):
        self.delay_by_step()
        try:
            return WebDriverWait(el, self.timeout).until(expected_conditions.invisibility_of_element(item))
        except TimeoutException:
            return False

    def click_left(self, el, step):
        self.delay_by_step()
        try:
            ActionChains(self.driver).click(el).perform()
        except ElementClickInterceptedException:
            raise ElementNotClickAble(el, step)

    def fill_field(self, el, data, step, clear=False):
        self.delay_by_step()
        try:
            if clear:
                el.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
            el.send_keys(data)
        except NoSuchElementException:
            raise ElementNotFoundException(el, step)

    def get_els(self, item, step):
        self.delay_by_step()
        try:
            return self.wait.until(expected_conditions.presence_of_all_elements_located(item))
        except TimeoutException:
            raise ElementNotFoundException(item, step)

    def get_find_els(self, el, item, step):
        self.delay_by_step()
        try:
            return WebDriverWait(el, self.timeout).until(expected_conditions.presence_of_all_elements_located(item))
        except TimeoutException:
            raise ElementNotFoundException(item, step)

    def get_visible_els(self, item, step):
        self.delay_by_step()
        try:
            return self.wait.until(expected_conditions.visibility_of_any_elements_located(item))
        except TimeoutException:
            raise ElementNotFoundException(item, step)

    def get_visible_find_els(self, el, item, step):
        self.delay_by_step()
        try:
            return WebDriverWait(el, self.timeout).until(expected_conditions.visibility_of_any_elements_located(item))
        except TimeoutException:
            raise ElementNotFoundException(item, step)

    def scroll_to_el(self, el, step):
        self.delay_by_step()
        try:
            ActionChains(self.driver).move_to_element(el).perform()
        except NoSuchElementException:
            raise ElementNotFoundException(el, step)

    def check_url_to_be(self, url):
        self.delay_by_step()
        try:
            return self.wait.until(expected_conditions.url_to_be(url))
        except TimeoutException:
            return False

    def check_url_contains(self, url):
        self.delay_by_step()
        try:
            return self.wait.until(expected_conditions.url_contains(url))
        except TimeoutException:
            return False

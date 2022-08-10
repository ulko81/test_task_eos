from pages.base import BasePage
from locators.all_locator import AllLocator


class AllPage(BasePage, AllLocator):
    def __init__(self, driver, timeout=10):
        BasePage.__init__(self, driver, timeout)

    def get_div_data_id(self, text, step):
        item = f'{self.div_data_id[0]}', f'{self.div_data_id[1].format(text)}'
        return self.get_visible_els(item, step)

    def get_div_class(self, text, step):
        item = f'{self.div_class[0]}', f'{self.div_class[1].format(text)}'
        return self.get_visible_els(item, step)

    def check_get_h1_normalize_space(self, text):
        item = f'{self.h1_normalize_space[0]}', f'{self.h1_normalize_space[1].format(text)}'
        return self.check_visible_els(item)

    def check_block_h1(self):
        return self.check_visible_els(self.h1)

    def find_input_data_id(self, el, text, step):
        locator = f'{self.input_data_id[0]}', f'{self.input_data_id[1].format(text)}'
        return self.get_visible_find_els(el, locator, step)

    def find_btn_data_id(self, el, text, step):
        locator = f'{self.btn_data_id[0]}', f'{self.btn_data_id[1].format(text)}'
        return self.get_visible_find_els(el, locator, step)

    def find_check_box(self, el, step):
        return self.get_visible_find_els(el, self.check_box, step)

from selenium.webdriver.common.by import By


class AllLocator:
    div_data_id = By.XPATH, './/div[@data-id="{}"]'
    div_class = By.XPATH, './/div[@class="{}"]'
    input_data_id = By.XPATH, './/input[@data-id="{}"]'
    btn_data_id = By.XPATH, './/button[@data-id="{}"]'
    check_box = By.XPATH, './/label//input'
    h1 = By.TAG_NAME, 'h1'
    h1_normalize_space = By.XPATH, '//h1[normalize-space(text())="{}"]'

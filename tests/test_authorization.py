import pytest
from pages.reg_auth_page import RegAuthPage
from methods.reg_auth_method import RegAuthMethod
from helpers.user_data import USER
from settings.setting_browser import DEFAULT_URL


class TestAuthorization(RegAuthMethod):
    @pytest.mark.authorization
    def test_authorization_success(self, desktop_browser):
        email = USER.get('login').get('email')
        password = USER.get('login').get('password')
        browser = desktop_browser()
        authorization_page = RegAuthPage(browser)
        registration_block = authorization_page.get_div_data_id(text='registration-form',
                                                                step='Find registration form')[0]
        auth_btn = authorization_page.find_btn_data_id(el=registration_block, text='sign-in-button',
                                                       step='Find sign-in-button')
        authorization_page.click_left(el=auth_btn[0], step='Click by sign_up_btn')
        authorization_block = authorization_page.get_div_data_id(text='login-form', step='Find login form')[0]
        self.fill_reg_auth(page=authorization_page, block=authorization_block,
                           email=email, password=password, click='sign-in-btn')
        self.check_url_contains(driver=browser, url_contains=DEFAULT_URL + '/main-map/fields/all')

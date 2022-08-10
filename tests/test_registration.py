import pytest
from pages.reg_auth_page import RegAuthPage
from helpers.texts import TEXT
from methods.reg_auth_method import RegAuthMethod
from helpers.user_data import USER
from settings.setting_browser import DEFAULT_URL


class TestRegistration(RegAuthMethod):

    @pytest.mark.registration
    def test_registration_success(self, desktop_browser):
        first_name = USER.get('registration').get('first_name')
        last_name = USER.get('registration').get('last_name')
        email = USER.get('registration').get('email')
        password = USER.get('registration').get('password')
        browser = desktop_browser()
        registration_page = RegAuthPage(browser)
        registration_block = registration_page.get_div_data_id(text='registration-form',
                                                               step='Find registration form')[0]
        self.fill_reg_auth(page=registration_page, block=registration_block, first_name=first_name, last_name=last_name,
                           email=email, password=password, check_box=True, click='sign-up-btn')
        self.check_url_contains(driver=browser, url_contains=DEFAULT_URL+'/login/confirm/')
        self.check_h1(driver=browser, exp_h1=TEXT.get('please_verify_your_email_address'))
        confirm_block = registration_page.get_div_class(text='content', step='Find confirm form')[0]
        self.fill_confirm(page=registration_page, block=confirm_block,  click='submit-code-btn')
        self.check_url_contains(driver=browser, url_contains=DEFAULT_URL + '/main-map/fields/all')

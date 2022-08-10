from helpers.texts import TEXT
from methods.all_page_method import AllPageMethod
from  helpers.general_method import GeneralMethod


class RegAuthMethod(GeneralMethod, AllPageMethod):

    @staticmethod
    def fill_field(page, block, field, field_data):
        input_field = page.find_input_data_id(el=block, text=field, step=f'Find field {field}')
        page.fill_field(el=input_field[0], data=field_data, step=f'Fill field {field}')

    # check_box = False if need checked True
    def fill_reg_auth(self, page, block, first_name=False, last_name=False,  password=False, email=False,
                      check_box=False, click=False):
        if first_name:
            self.fill_field(page=page, block=block, field='first_name', field_data=first_name)
        if last_name:
            self.fill_field(page=page, block=block, field='last_name', field_data=last_name)
        if email:
            self.fill_field(page=page, block=block, field='email', field_data=email)
        if password:
            self.fill_field(page=page, block=block, field='password', field_data=password)
        if check_box:
            checkbox = page.find_check_box(el=block, step='Find checkbox')
            page.click_left(el=checkbox[0], step='Click checkbox')
        if click:
            reg_button = page.find_btn_data_id(el=block, text=click, step='Find sign-up-btn')
            page.click_left(el=reg_button[0], step='Click by sign_up_btn')

    def fill_confirm(self, page, block, click=False):
        code = self.get_email_code()
        self.fill_field(page=page, block=block, field='confirm-code-input', field_data=code)
        if click:
            reg_button = page.find_btn_data_id(el=block, text=click, step='Find sign-up-btn')
            page.click_left(el=reg_button[0], step='Click by sign_up_btn')

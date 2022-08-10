from pages.all_page import AllPage


class AllPageMethod:
    @staticmethod
    def check_url_contains(driver, url_contains, timeout=10):
        all_page = AllPage(driver=driver, timeout=timeout)
        result_url = all_page.check_url_contains(url_contains)
        current_url = driver.current_url
        assert(result_url is not False,
               f'Missing in URL "{url_contains}" (timeout: {timeout}s). Actual URL: "{current_url}"')

    @staticmethod
    def check_h1(driver, exp_h1, timeout=10):
        all_page = AllPage(driver=driver, timeout=timeout)
        result_h1 = all_page.check_get_h1_normalize_space(exp_h1)
        act_h1 = all_page.check_block_h1()
        if act_h1:
            act_h1 = act_h1[0].get_attribute('textContent').strip()
        assert (result_h1 is not False,
                f'Mismatch H1 (timeout: {timeout}s). Expected H1: "{exp_h1}" Actual H1: "{act_h1}"')

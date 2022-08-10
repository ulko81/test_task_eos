import pytest

from settings.setting_browser import *

@pytest.fixture()
def desktop_browser(request):
    request.instance.driver = None

    def wrap_desktop_browser(url=None):
        driver_url = f'{DEFAULT_URL}{url}'
        request.instance.driver = SettingsBrowser().set_chrome()
        request.instance.driver.get(driver_url)
        return request.instance.driver
    yield wrap_desktop_browser
    if request.instance.driver:
        request.instance.driver.quit()


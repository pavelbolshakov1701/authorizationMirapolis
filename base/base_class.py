from selenium.webdriver import ActionChains
import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    '''Method get current url'''

    def get_current_url(self):
        get_url = self.driver.current_url
        print('get url', get_url)

    '''Method assert word'''

    def assert_word(self, xpath_word, res):
        value = xpath_word.text
        assert value == res
        print('Good value word')

    def assert_comparison_word(self, res1, res2):
        assert res1 == res2
        print('Good comparison')

    '''Method screenshot'''

    def screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\User\\Desktop\\phyton\\pythonProject\\autorizationMirapolis'
                                    '\\screenshot\\' + name_screenshot)

    '''Method assert url'''

    def assert_url(self, res):
        get_url = self.driver.current_url
        assert get_url == res
        print('Good value url')

    '''Method action chains'''

    def action_chains(self):
        action = ActionChains(self.driver)
        return action

    '''Method scroll'''

    def driver_scroll(self, res):
        return self.driver.execute_script('window.scrollTo(0, ' + res + ')')

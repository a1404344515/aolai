import time

from base.base_driver import init_driver
from page.page import Page


class TestDengLu:
    def setup(self):
        self.driver=init_driver()
        self.page=Page(self.driver)
    def teardown(self):
        time.sleep(2)
        self.driver.quit()
    def test_denglu(self):
        self.page.shouye().click_wo()
        self.page.wo().click_denglu()
        self.page.denglu().input_id('itheima_test')
        self.page.denglu().input_mima('itheima')
        self.page.denglu().click_denglu()
        time.sleep(2)
        self.page.me().get_id()
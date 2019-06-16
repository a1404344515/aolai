from page.page_denglu import DengLuPage
from page.page_me import MePage
from page.page_shouye import ShouYePage
from page.page_wo import WoPage


class Page:
    def __init__(self,driver):
        self.driver=driver
    def denglu(self):
        return DengLuPage(self.driver)
    def me(self):
        return MePage(self.driver)
    def shouye(self):
        return ShouYePage(self.driver)
    def wo(self):
        return WoPage(self.driver)

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class WoPage(BaseAction):
    a=By.ID,'com.yunmall.lc:id/gotologon'
    def click_denglu(self):
        self.click(self.a)
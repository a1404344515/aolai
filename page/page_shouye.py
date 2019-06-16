from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ShouYePage(BaseAction):
    a=By.XPATH,'//*[@text="我"]'
    def click_wo(self):
        self.click(self.a)